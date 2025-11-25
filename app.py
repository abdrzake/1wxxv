from flask import Flask, render_template, request, redirect, session, jsonify, url_for
# Use session-based language selection using the translations dict
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from translations import translations
import os


def create_app():
    app = Flask(__name__)
    # Keep secret key configurable via env for production
    app.secret_key = os.environ.get('SECRET_KEY', 'your_secret_key_123')


    # Helper: session-based language selection and translation function
    def get_lang():
        lang = session.get('lang', 'ar')
        return lang if lang in translations else 'ar'

    def t(key):
        lang = get_lang()
        return translations.get(lang, {}).get(key, translations.get('ar', {}).get(key, key))

    @app.context_processor
    def inject_helpers():
        return {
            't': t,
            'lang': get_lang(),
            'translations': translations
        }

    # ---------- Database helpers ----------
    DB_PATH = os.path.join(os.path.dirname(__file__), 'ecommerce.db')

    def get_db_connection():
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db():
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY, username TEXT UNIQUE, email TEXT UNIQUE, password TEXT, created_at TIMESTAMP)''')
        c.execute('''CREATE TABLE IF NOT EXISTS products
                     (id INTEGER PRIMARY KEY, name TEXT, description TEXT, price REAL, image TEXT, stock INTEGER, category TEXT, created_at TIMESTAMP)''')
        c.execute('''CREATE TABLE IF NOT EXISTS cart
                     (id INTEGER PRIMARY KEY, user_id INTEGER, product_id INTEGER, quantity INTEGER, added_at TIMESTAMP)''')
        c.execute('''CREATE TABLE IF NOT EXISTS orders
                     (id INTEGER PRIMARY KEY, user_id INTEGER, total_price REAL, status TEXT, created_at TIMESTAMP)''')
        c.execute('''CREATE TABLE IF NOT EXISTS order_items
                     (id INTEGER PRIMARY KEY, order_id INTEGER, product_id INTEGER, quantity INTEGER, price REAL)''')
        conn.commit()
        conn.close()
        add_sample_products()

    def add_sample_products():
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT COUNT(*) as cnt FROM products')
        if c.fetchone()['cnt'] == 0:
            products = [
                ('كمبيوتر محمول', 'كمبيوتر محمول عالي الأداء Intel i7 مع 16GB RAM و SSD 512GB', 1200, '/static/laptop.jpg', 10, 'الكترونيات'),
                ('هاتف ذكي', 'هاتف ذكي 5G بشاشة AMOLED 120Hz وكاميرا 108MP احترافية', 800, '/static/phone.jpg', 20, 'الكترونيات'),
                ('سماعات بلوتوث', 'سماعات لاسلكية بجودة صوت عالية مع تقنية Noise Cancelling', 150, '/static/headphones.jpg', 30, 'الكترونيات'),
                ('كاميرا احترافية', 'كاميرا DSLR بدقة 24 ميجابكسل وعدسات احترافية متعددة', 1500, '/static/camera.jpg', 5, 'الكترونيات'),
                ('ساعة ذكية', 'ساعة ذكية تتبع اللياقة البدنية مع مراقب ضربات القلب', 300, '/static/watch.jpg', 15, 'الكترونيات'),
                ('قارئ كتب إلكتروني', 'جهاز قراءة كتب بشاشة E-ink عالية الدقة', 250, '/static/ereader.jpg', 8, 'الكترونيات'),
                ('جهاز لوحي', 'جهاز لوحي 10 بوصة بمعالج قوي وبطارية طويلة الأمد', 500, '/static/tablet.jpg', 12, 'الكترونيات'),
                ('ماوس لاسلكي', 'ماوس دقيق مع بطارية قابلة للشحن وتصميم مريح', 50, '/static/mouse.jpg', 40, 'الملحقات'),
                ('لوحة مفاتيح ميكانيكية', 'لوحة مفاتيح للألعاب بإضاءة RGB قابلة للتخصيص', 120, '/static/keyboard.jpg', 18, 'الملحقات'),
                ('حامل هاتف', 'حامل قابل للتعديل للهواتف والأجهزة اللوحية بأحجام مختلفة', 25, '/static/holder.jpg', 50, 'الملحقات'),
                ('كابل USB-C', 'كابل شحن وتبادل بيانات سريع معتمد من الشركات الكبرى', 15, '/static/cable.jpg', 100, 'الملحقات'),
                ('محطة شحن', 'محطة شحن متعددة الأجهزة بتقنية الشحن السريع', 80, '/static/charger.jpg', 20, 'الملحقات'),
            ]
            for p in products:
                c.execute('INSERT INTO products (name, description, price, image, stock, category, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)',
                          (p[0], p[1], p[2], p[3], p[4], p[5], datetime.now()))
            conn.commit()
        conn.close()

    # Run DB init on startup
    init_db()

    # ---------- Routes (kept logic, cleaned) ----------
    @app.route('/')
    def index():
        return redirect(url_for('store'))

    @app.route('/set-language/<lang>')
    def set_language(lang):
        if lang in translations:
            session['lang'] = lang
        return redirect(request.referrer or url_for('store'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE username = ?', (username,))
            user = c.fetchone()
            conn.close()
            if user and check_password_hash(user['password'], password):
                session['username'] = username
                session['user_id'] = user['id']
                return redirect(url_for('store'))
            else:
                return render_template('login.html', error=t('error_login'))
        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = request.form.get('username')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')
            if password != confirm_password:
                return render_template('register.html', error=t('password_mismatch'))
            try:
                conn = get_db_connection()
                c = conn.cursor()
                hashed = generate_password_hash(password)
                c.execute('INSERT INTO users (username, email, password, created_at) VALUES (?, ?, ?, ?)',
                          (username, email, hashed, datetime.now()))
                conn.commit()
                conn.close()
                return redirect(url_for('login'))
            except sqlite3.IntegrityError:
                return render_template('register.html', error=t('user_exists'))
        return render_template('register.html')

    @app.route('/store')
    def store():
        conn = get_db_connection()
        c = conn.cursor()
        category = request.args.get('category', 'all')
        search = request.args.get('search', '')
        if category == 'all' and not search:
            c.execute('SELECT * FROM products')
        elif search:
            c.execute('SELECT * FROM products WHERE name LIKE ? OR description LIKE ?', (f'%{search}%', f'%{search}%'))
        else:
            c.execute('SELECT * FROM products WHERE category = ?', (category,))
        products = c.fetchall()
        c.execute('SELECT DISTINCT category FROM products')
        categories = [r[0] for r in c.fetchall()]
        # cart count only for logged-in users
        cart_count = 0
        if 'user_id' in session:
            c.execute('SELECT SUM(quantity) as cnt FROM cart WHERE user_id = ?', (session['user_id'],))
            row = c.fetchone()
            cart_count = row['cnt'] if row and row['cnt'] is not None else 0
        conn.close()
        return render_template('store.html', products=products, categories=categories, cart_count=cart_count, username=session.get('username'))

    @app.route('/product/<int:product_id>')
    def product_detail(product_id):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM products WHERE id = ?', (product_id,))
        product = c.fetchone()
        conn.close()
        if not product:
            return redirect(url_for('store'))
        return render_template('product_detail.html', product=product, username=session.get('username'))

    @app.route('/add-to-cart/<int:product_id>', methods=['POST'])
    def add_to_cart(product_id):
        if 'username' not in session:
            return jsonify({'error': 'يجب تسجيل الدخول أولاً'}), 401
        quantity = int(request.form.get('quantity', 1))
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM cart WHERE user_id = ? AND product_id = ?', (session['user_id'], product_id))
        existing = c.fetchone()
        if existing:
            c.execute('UPDATE cart SET quantity = quantity + ? WHERE user_id = ? AND product_id = ?', (quantity, session['user_id'], product_id))
        else:
            c.execute('INSERT INTO cart (user_id, product_id, quantity, added_at) VALUES (?, ?, ?, ?)', (session['user_id'], product_id, quantity, datetime.now()))
        conn.commit()
        conn.close()
        return jsonify({'success': 'تم إضافة المنتج إلى السلة'})

    @app.route('/cart')
    def cart():
        if 'username' not in session:
            return redirect(url_for('login'))
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('''SELECT c.id, p.id as pid, p.name, p.price, c.quantity, p.image FROM cart c JOIN products p ON c.product_id = p.id WHERE c.user_id = ?''', (session['user_id'],))
        cart_items = c.fetchall()
        total = sum(item['price'] * item['quantity'] for item in cart_items)
        conn.close()
        return render_template('cart.html', cart_items=cart_items, total=total, username=session['username'])

    @app.route('/remove-from-cart/<int:cart_id>', methods=['POST'])
    def remove_from_cart(cart_id):
        if 'username' not in session:
            return jsonify({'error': 'يجب تسجيل الدخول أولاً'}), 401
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('DELETE FROM cart WHERE id = ? AND user_id = ?', (cart_id, session['user_id']))
        conn.commit()
        conn.close()
        return jsonify({'success': 'تم حذف المنتج من السلة'})

    @app.route('/checkout', methods=['GET', 'POST'])
    def checkout():
        if 'username' not in session:
            return redirect(url_for('login'))
        conn = get_db_connection()
        c = conn.cursor()
        if request.method == 'POST':
            c.execute('SELECT SUM(c.quantity * p.price) as total FROM cart c JOIN products p ON c.product_id = p.id WHERE c.user_id = ?', (session['user_id'],))
            total = c.fetchone()['total'] or 0
            c.execute('INSERT INTO orders (user_id, total_price, status, created_at) VALUES (?, ?, ?, ?)', (session['user_id'], total, 'قيد المعالجة', datetime.now()))
            order_id = c.lastrowid
            c.execute('''SELECT c.product_id, c.quantity, p.price FROM cart c JOIN products p ON c.product_id = p.id WHERE c.user_id = ?''', (session['user_id'],))
            cart_items = c.fetchall()
            for product_id, quantity, price in cart_items:
                c.execute('INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?)', (order_id, product_id, quantity, price))
            c.execute('DELETE FROM cart WHERE user_id = ?', (session['user_id'],))
            conn.commit()
            conn.close()
            return redirect(url_for('order_confirmation', order_id=order_id))
        c.execute('SELECT SUM(c.quantity * p.price) as total FROM cart c JOIN products p ON c.product_id = p.id WHERE c.user_id = ?', (session['user_id'],))
        total = c.fetchone()['total'] or 0
        conn.close()
        return render_template('checkout.html', total=total, username=session['username'])

    @app.route('/order-confirmation/<int:order_id>')
    def order_confirmation(order_id):
        if 'username' not in session:
            return redirect(url_for('login'))
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM orders WHERE id = ? AND user_id = ?', (order_id, session['user_id']))
        order = c.fetchone()
        if not order:
            conn.close()
            return redirect(url_for('store'))
        c.execute('''SELECT oi.id, p.name, oi.quantity, oi.price FROM order_items oi JOIN products p ON oi.product_id = p.id WHERE oi.order_id = ?''', (order_id,))
        order_items = c.fetchall()
        conn.close()
        return render_template('order_confirmation.html', order=order, order_items=order_items, username=session['username'])

    @app.route('/orders')
    def orders():
        if 'username' not in session:
            return redirect(url_for('login'))
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM orders WHERE user_id = ? ORDER BY created_at DESC', (session['user_id'],))
        user_orders = c.fetchall()
        conn.close()
        return render_template('orders.html', orders=user_orders, username=session['username'])

    @app.route('/profile')
    def profile():
        if 'username' not in session:
            return redirect(url_for('login'))
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],))
        user = c.fetchone()
        conn.close()
        return render_template('profile.html', user=user, username=session['username'])

    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login'))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)