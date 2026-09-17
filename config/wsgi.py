import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# Vercel-এর /tmp/db.sqlite3 ফাঁকা থাকলে অটো মাইগ্রেশন রান করার জন্য:
try:
    from django.core.management import call_command
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"Migration error: {e}")
