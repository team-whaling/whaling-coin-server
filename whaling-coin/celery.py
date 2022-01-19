from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# 기본 장고파일 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whaling-coin.settings')
app = Celery('whaling-coin')
app.config_from_object('django.conf:settings', namespace='CELERY')
#등록된 장고 앱 설정에서 task 불러오기
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# crontab()에 인자를 안주면 기본 매 1분마다 실행한다.
app.conf.beat_schedule = {
    'Update-api-every-minutes-crontab' : {
        'task' : 'coins.tasks.update_api',
        'schedule' : crontab(),
    },
    'Finishing-vote-every-minutes' : {
        'task' : 'votes.tasks.check_finish',
        'schedule' : crontab(),
    },
    'Tracking-vote-every-minutes' : {
        'task' : 'votes.tasks.tracking',
        'schedule' : crontab(),
    }
}