from django.test import TestCase
import pytz
import datetime
# Create your tests here.


kst_time = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
ymd = int(kst_time.strftime('%Y%m%d%H%M'))
hm = int(kst_time.strftime('%H%M'))
print(ymd,hm)
print(type(ymd))