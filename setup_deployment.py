#!/usr/bin/env python
"""
نظيف وإعداد التطبيق للنشر
Run: python setup_deployment.py
"""

import os
import sys
import shutil
from pathlib import Path

def create_files():
    """إنشاء الملفات المطلوبة"""
    files = {
        'Procfile': 'web: gunicorn app:app\n',
        'runtime.txt': 'python-3.9.16\n',
        '.gitignore': get_gitignore_content(),
    }
    
    for filename, content in files.items():
        if not os.path.exists(filename):
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ تم إنشاء: {filename}")
        else:
            print(f"⏭️  موجود بالفعل: {filename}")

def get_gitignore_content():
    """محتوى ملف .gitignore"""
    return """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Environments
.env
.venv
env/
venv/
ENV/

# Database
*.db
*.sqlite3
ecommerce.db

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
"""

def check_requirements():
    """التحقق من requirements.txt"""
    required_packages = [
        'Flask==3.0.0',
        'Werkzeug==3.0.0',
        'gunicorn==20.1.0'
    ]
    
    if not os.path.exists('requirements.txt'):
        with open('requirements.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(required_packages) + '\n')
        print("✅ تم إنشاء: requirements.txt")
    else:
        print("✅ موجود: requirements.txt")

def init_git():
    """تهيئة مستودع Git"""
    if not os.path.exists('.git'):
        os.system('git init')
        print("✅ تم تهيئة Git repository")
    else:
        print("✅ موجود: .git")

def print_next_steps():
    """طباعة الخطوات التالية"""
    print("\n" + "="*50)
    print("🚀 الخطوات التالية:")
    print("="*50)
    print("""
1. تسجيل الدخول إلى Heroku:
   $ heroku login

2. إنشاء تطبيق جديد:
   $ heroku create your-app-name

3. إضافة الملفات:
   $ git add .
   $ git commit -m "Initial commit"

4. رفع التطبيق:
   $ git push heroku main

5. فتح الموقع:
   $ heroku open

اختبر محلياً قبل النشر:
   $ pip install gunicorn
   $ gunicorn app:app
   # افتح http://localhost:8000
    """)

def main():
    """التشغيل الرئيسي"""
    print("🔧 إعداد التطبيق للنشر...\n")
    
    create_files()
    check_requirements()
    
    print("\n📝 إضافة ملفات إلى Git...")
    os.system('git add .')
    
    print_next_steps()
    print("\n✅ تم الإعداد بنجاح!")

if __name__ == '__main__':
    main()
