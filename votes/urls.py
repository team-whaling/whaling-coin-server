from django.urls import path,include
from .views import TestVoteView

app_name = 'votes'

urlpatterns = [
    # path('votes/', TestVoteView.as_view())
]