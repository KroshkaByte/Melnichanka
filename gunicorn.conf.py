import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "melnichanka.settings")

application = get_wsgi_application()

bind = "0.0.0.0:8000"
