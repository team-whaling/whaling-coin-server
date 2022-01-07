from django.urls import path,include
from rest_framework import routers
from .views import CryptoView

app_name = 'coins'

urlpatterns = [
    path(r'coins', CryptoView.as_view()),
]