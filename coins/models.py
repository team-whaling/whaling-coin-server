from django.db import models
# Create your models here.

class DateModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)    # save될 때마다 날짜 갱신

class Coin(DateModel):
    coin_code = models.CharField(max_length=10,primary_key=True)    # PK
    coin_name = models.CharField(max_lenght=12,null=False)
    coin_image = models.URLField(null=False)
    cur_price = models.IntegerField(null=False)

