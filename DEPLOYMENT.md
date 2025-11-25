# نشر متجرك الإلكتروني 🚀

## الطرق المتاحة لنشر التطبيق:

### الطريقة 1: استخدام Heroku (الأسهل والأشهر) ⭐

#### المتطلبات:
1. حساب على [Heroku](https://www.heroku.com)
2. تثبيت Heroku CLI

#### الخطوات:

```bash
# 1. تثبيت Heroku CLI
# من الموقع: https://devcenter.heroku.com/articles/heroku-cli

# 2. تسجيل الدخول
heroku login

# 3. إنشاء تطبيق جديد
heroku create your-app-name

# 4. رفع الملفات
git push heroku main

# 5. الرابط سيكون:
# https://your-app-name.herokuapp.com
```

---

### الطريقة 2: استخدام PythonAnywhere ⭐⭐

#### المتطلبات:
1. حساب على [PythonAnywhere](https://www.pythonanywhere.com)

#### الخطوات:

1. اذهب إلى https://www.pythonanywhere.com
2. انشئ حساب مجاني
3. افتح Console وأدخل أوامر:

```bash
# نسخ المشروع
git clone https://github.com/your-username/ecommerce.git
cd ecommerce

# تثبيت المكتبات
pip install -r requirements.txt
```

4. أضف web app جديدة من Dashboard
5. اختر Flask وPython 3.10
6. عدّل WSGI file بهذا الكود:

```python
import sys
path = '/home/your-username/ecommerce'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

7. الرابط سيكون: `https://your-username.pythonanywhere.com`

---

### الطريقة 3: استخدام Render ⭐⭐

#### المتطلبات:
1. حساب على [Render](https://render.com)
2. مشروع على GitHub

#### الخطوات:

1. اذهب إلى https://render.com
2. اضغط "New +" ثم اختر "Web Service"
3. ربط حسابك على GitHub
4. اختر المشروع
5. اختر البيئة: Python
6. أدخل الأوامر:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`

---

### الطريقة 4: استخدام AWS أو Azure (متقدمة)

يمكنك استخدام خدمات السحابة الكبرى مثل AWS EC2 أو Azure App Service.

---

## الملفات المطلوبة للنشر:

### 1. ملف `Procfile` (لـ Heroku)

```
web: gunicorn app:app
```

### 2. ملف `runtime.txt` (لـ Heroku)

```
python-3.9.16
```

### 3. تحديث `requirements.txt`

```
Flask==3.0.0
Werkzeug==3.0.0
gunicorn==20.1.0
```

---

## اختبار التطبيق محلياً قبل النشر:

```bash
# تثبيت gunicorn
pip install gunicorn

# تشغيل التطبيق
gunicorn app:app

# سيكون متاح على: http://localhost:8000
```

---

## نصائح أمان قبل النشر:

1. **غير secret_key في app.py**:
```python
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key')
```

2. **استخدم متغيرات البيئة**:
```bash
export SECRET_KEY="your-secure-key"
export DATABASE_URL="your-database-url"
```

3. **أضف `.gitignore`**:
```
*.pyc
__pycache__/
.env
ecommerce.db
*.sqlite3
venv/
```

---

## الخطوات السريعة للنشر على Heroku:

```bash
# 1. إنشاء مشروع git
git init
git add .
git commit -m "Initial commit"

# 2. إنشاء تطبيق على Heroku
heroku create ecommerce-store

# 3. رفع المشروع
git push heroku main

# 4. فتح الموقع
heroku open
```

**الرابط سيكون شيء مثل:**
```
https://ecommerce-store.herokuapp.com
```

---

## مراقبة التطبيق بعد النشر:

```bash
# عرض السجلات
heroku logs --tail

# إعادة تشغيل
heroku restart

# فتح console
heroku run bash
```

---

## اختبر التطبيق:

بعد النشر:
1. زر الرابط الذي حصلت عليه
2. جرب تسجيل حساب جديد
3. أضف منتجات للسلة
4. أكمل عملية الشراء

---

**أي طريقة تفضل؟ سأساعدك بخطوات التفاصيل!** 🚀
