from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv()

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'melnichanka.settings')

broker_user = os.getenv('RABBITMQ_DEFAULT_USER')
broker_pass = os.getenv('RABBITMQ_DEFAULT_PASS')
broker_url = f"amqp://{broker_user}:{broker_pass}@rabbitmq:5672//"

app = Celery('melnichanka', broker=broker_url)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
