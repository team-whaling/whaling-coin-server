from .models import Cryptocurrency
from rest_framework import serializers

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ['coin_code', 'coin_name', 'coin_image', 'cur_price', 'trade_date', 'trade_time',
                  'coin_fullname', 'updated_date','updated_time']
