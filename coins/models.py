from django.db import models
# Create your models here.

# Upbit에서 날짜랑 시간 두개로 나눠서 정보를 준다. 20220101, 171205 이런식.
class Cryptocurrency(models.Model):
    coin_code = models.CharField(max_length=10,primary_key=True)    # PK
    coin_name = models.CharField(max_length=12,null=False) # 한글이름
    coin_fullname = models.CharField(null=False)
    coin_image = models.URLField()
    cur_price = models.IntegerField(null=False)
    trade_date = models.CharField(max_length=10, null=False)
    trade_time = models.CharField(max_length=10, null=False)
    updated_date = models.IntegerField(null=False)
    updated_time = models.IntegerField(null=False)



