from .models import Cryptocurrency
from rest_framework import serializers

class CryptoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ['coin_code', 'coin_name', 'coin_image', 'cur_price', 'coin_fullname',
                  'full_updated_time','updated_date','updated_time']
