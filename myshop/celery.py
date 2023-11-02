import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = Celery('myshop')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)