# translations.py
# ملف الترجمات الشامل

translations = {
    'ar': {
        # قوائم التنقل
        'nav_store': 'المتجر',
        'nav_orders': 'طلباتي',
        'nav_profile': 'حسابي',
        'nav_cart': 'السلة',
        'nav_logout': 'خروج',
        'nav_login': 'دخول',
        'nav_register': 'تسجيل',
        
        # الصفحات الرئيسية
        'page_login': 'تسجيل الدخول',
        'page_register': 'إنشاء حساب جديد',
        'page_store': 'المتجر',
        'page_cart': 'السلة',
        'page_checkout': 'إكمال الشراء',
        'page_profile': 'حسابي الشخصي',
        'page_orders': 'طلباتي',
        
        # نماذج التسجيل
        'username': 'اسم المستخدم',
        'email': 'البريد الإلكتروني',
        'password': 'كلمة المرور',
        'confirm_password': 'تأكيد كلمة المرور',
        'login_btn': 'دخول',
        'register_btn': 'تسجيل',
        
        # رسائل الأخطاء
        'error_invalid_login': 'اسم المستخدم أو كلمة المرور غير صحيحة',
        'error_password_mismatch': 'كلمات المرور غير متطابقة',
        'error_user_exists': 'اسم المستخدم أو البريد الإلكتروني موجود بالفعل',
        
        # المنتجات
        'filter_category': 'تصفية حسب القسم',
        'all_categories': 'جميع الأقسام',
        'search_placeholder': 'ابحث عن منتج...',
        'product_price': 'السعر',
        'add_to_cart': 'أضف',
        'no_products': 'لا توجد منتجات متاحة حالياً',
        'product_details': 'تفاصيل المنتج',
        'quantity': 'الكمية',
        'in_stock': 'متوفر في المخزون',
        'out_of_stock': 'غير متوفر حالياً',
        
        # السلة والدفع
        'cart_empty': 'سلتك فارغة حالياً',
        'subtotal': 'السعر الأساسي',
        'shipping': 'الشحن',
        'tax': 'الضريبة',
        'total': 'الإجمالي',
        'free': 'مجاني',
        'continue_shopping': 'متابعة التسوق',
        'proceed_checkout': 'إكمال الشراء',
        'remove': 'حذف',
        
        # معلومات الدفع
        'delivery_info': 'معلومات التوصيل',
        'payment_method': 'طريقة الدفع',
        'shipping_company': 'شركة الشحن',
        'full_name': 'الاسم الكامل',
        'phone': 'رقم الهاتف',
        'address': 'العنوان',
        'additional_notes': 'ملاحظات إضافية',
        'order_summary': 'ملخص الطلب',
        'confirm_purchase': 'تأكيد الشراء',
        'back_to_cart': 'العودة للسلة',
        
        # تأكيد الطلب
        'order_confirmed': 'شكراً لك!',
        'order_received': 'تم استقبال طلبك بنجاح',
        'order_number': 'رقم الطلب',
        'order_status': 'حالة الطلب',
        'order_date': 'تاريخ الطلب',
        'view_all_orders': 'عرض جميع طلباتي',
        
        # الحساب الشخصي
        'my_account': 'حسابي الشخصي',
        'account_info': 'معلومات الحساب',
        'total_orders': 'إجمالي الطلبات',
        'pending_orders': 'طلبات معلقة',
        'completed_orders': 'طلبات مكتملة',
        'edit': 'تعديل',
        'delivery_addresses': 'عناوين التوصيل',
        'preferences': 'التفضيلات',
        'email_notifications': 'استقبال إشعارات البريد الإلكتروني',
        'sms_notifications': 'استقبال رسائل نصية',
        'account_created': 'تاريخ إنشاء الحساب',
        
        # مشاعر إيجابية
        'success_add_cart': 'تم إضافة المنتج إلى السلة',
        'success_order': 'تم استلام طلبك بنجاح',
        'welcome': 'مرحباً',
    },
    'en': {
        # Navigation menus
        'nav_store': 'Store',
        'nav_orders': 'My Orders',
        'nav_profile': 'My Account',
        'nav_cart': 'Cart',
        'nav_logout': 'Logout',
        'nav_login': 'Login',
        'nav_register': 'Sign Up',
        
        # Main pages
        'page_login': 'Login',
        'page_register': 'Create New Account',
        'page_store': 'Store',
        'page_cart': 'Shopping Cart',
        'page_checkout': 'Complete Purchase',
        'page_profile': 'My Account',
        'page_orders': 'My Orders',
        
        # Registration forms
        'username': 'Username',
        'email': 'Email',
        'password': 'Password',
        'confirm_password': 'Confirm Password',
        'login_btn': 'Login',
        'register_btn': 'Sign Up',
        
        # Error messages
        'error_invalid_login': 'Invalid username or password',
        'error_password_mismatch': 'Passwords do not match',
        'error_user_exists': 'Username or email already exists',
        
        # Products
        'filter_category': 'Filter by Category',
        'all_categories': 'All Categories',
        'search_placeholder': 'Search for a product...',
        'product_price': 'Price',
        'add_to_cart': 'Add',
        'no_products': 'No products available',
        'product_details': 'Product Details',
        'quantity': 'Quantity',
        'in_stock': 'In Stock',
        'out_of_stock': 'Out of Stock',
        
        # Cart and checkout
        'cart_empty': 'Your cart is empty',
        'subtotal': 'Subtotal',
        'shipping': 'Shipping',
        'tax': 'Tax',
        'total': 'Total',
        'free': 'Free',
        'continue_shopping': 'Continue Shopping',
        'proceed_checkout': 'Proceed to Checkout',
        'remove': 'Remove',
        
        # Payment information
        'delivery_info': 'Delivery Information',
        'payment_method': 'Payment Method',
        'shipping_company': 'Shipping Company',
        'full_name': 'Full Name',
        'phone': 'Phone Number',
        'address': 'Address',
        'additional_notes': 'Additional Notes',
        'order_summary': 'Order Summary',
        'confirm_purchase': 'Confirm Purchase',
        'back_to_cart': 'Back to Cart',
        
        # Order confirmation
        'order_confirmed': 'Thank You!',
        'order_received': 'Your order has been received',
        'order_number': 'Order Number',
        'order_status': 'Order Status',
        'order_date': 'Order Date',
        'view_all_orders': 'View All Orders',
        
        # Personal account
        'my_account': 'My Account',
        'account_info': 'Account Information',
        'total_orders': 'Total Orders',
        'pending_orders': 'Pending Orders',
        'completed_orders': 'Completed Orders',
        'edit': 'Edit',
        'delivery_addresses': 'Delivery Addresses',
        'preferences': 'Preferences',
        'email_notifications': 'Email Notifications',
        'sms_notifications': 'SMS Notifications',
        'account_created': 'Account Created',
        
        # Positive messages
        'success_add_cart': 'Product added to cart successfully',
        'success_order': 'Your order has been received',
        'welcome': 'Welcome',
    }
}
