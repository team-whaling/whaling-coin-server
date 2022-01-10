from django.test import TestCase
import pytz
from datetime import datetime,timedelta
# Create your tests here.

kst_time = datetime.now(pytz.timezone('Asia/Seoul')).replace(tzinfo=None,microsecond=0,second=0)
utc_time = datetime.now(pytz.timezone('UTC')).replace(tzinfo=None,microsecond=0,second=0)
time = kst_time-utc_time
print(kst_time, utc_time)
utc_time += timedelta(hours=9)
if kst_time == utc_time:
    print("t")
else:
    print("false")
ymd = int(kst_time.strftime('%Y%m%d%H%M'))
hm = int(kst_time.strftime('%H%M'))
print(ymd,hm)
print(type(ymd))