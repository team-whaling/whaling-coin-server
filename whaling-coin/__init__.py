from __future__ import absolute_import

# 이 문장은 shared_task를 위해 장고가 시작될 때 app이
from .celery import app as celery_app

__all__ = ('celery_app',)
