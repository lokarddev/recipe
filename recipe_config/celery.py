from __future__ import absolute_import
import os
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_config.settings')
app = Celery()

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'click_an_hour': {
        'task': 'recipe_app.tasks.click_to_model',
        'schedule': 10,
    }
}
