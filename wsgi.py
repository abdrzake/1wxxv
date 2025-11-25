"""
WSGI entry point for production servers
Used by Heroku, Render, and other deployment platforms
"""
import os
from app import app

# إعدادات الإنتاج
if __name__ != "__main__":
    os.environ['FLASK_ENV'] = 'production'
    app.config['DEBUG'] = False

if __name__ == "__main__":
    app.run()
