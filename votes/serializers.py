from .models import VoteVote
from rest_framework import serializers

class TestVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoteVote
        fields = '__all__'
