from django.db import models
from django.utils import timezone
# Create your models here.

# Upbit에서 날짜랑 시간 두개로 나눠서 정보를 준다. 20220101, 171205 이런식.
class Cryptocurrency(models.Model):
    coin_code = models.CharField(max_length=10,primary_key=True)    # PK
    coin_name = models.CharField(max_length=12,null=False)
    coin_image = models.URLField()
    cur_price = models.IntegerField(null=False)
    trade_date = models.CharField(max_length=10, null=False)
    trade_time = models.CharField(max_length=10, null=False)
    updated_at = models.DateTimeField(auto_now=True,default=timezone.now)



