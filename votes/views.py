from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import VoteVote
from .serializers import TestVoteSerializer

# 모든 정보 다 넘겨주면 되니까?
class TestVoteView(generics.ListAPIView):
    serializer_class = TestVoteSerializer
    queryset = VoteVote.objects.all()
