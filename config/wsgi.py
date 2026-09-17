import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

# Auto Migrate & Auto Create Superuser
try:
    from django.core.management import call_command
    from django.contrib.auth import get_user_model


    call_command('migrate', interactive=False)

    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin1234')
        print("Superuser created successfully!")
except Exception as e:
    print(f"Error during auto setup: {e}")
