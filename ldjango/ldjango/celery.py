from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
"""
Run command under the directory of your project. Namely one level up

$ celery -A ldjango worker -l info // run a async task

$ celery -A ldjango beat -l info -S django // start the celery beat service using the django scheduler

// start redis
$ /etc/init.d/redis-server start
"""
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ldjango.settings')

app = Celery('ldjango')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

