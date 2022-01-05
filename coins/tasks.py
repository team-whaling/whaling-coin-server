from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Cryptocurrency

@shared_task()
def update_api():
    print("Update CryptoCurrrency")


