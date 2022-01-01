from django.shortcuts import render
from rest_framework import generics
from .models import Cryptocurrency
from .serializers import CryptoSerializer

# 모든 정보 다 넘겨주면 되니까?
class CryptoView(generics.ListAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptoSerializer
