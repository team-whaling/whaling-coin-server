from django.shortcuts import render
from rest_framework import generics
from .models import Cryptocurrency
from .serializers import CryptoSerializer

# 모든 정보 다 넘겨주면 되니까?
class CryptoView(generics.ListAPIView):
    serializer_class = CryptoSerializer
    def get_queryset(self):
        quaryset = Cryptocurrency.objects.all()
        coincode = self.request.query_params.getlist('coin_code',None)
        if len(coincode) == 0:
            coincode = None
        if coincode is not None:
            quaryset = quaryset.filter(coin_code__in=coincode)
        return quaryset
