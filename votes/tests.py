from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import *
from coins.models import Cryptocurrency
import pytz
import datetime
from django.core.exceptions import ObjectDoesNotExist

votevote = VoteVote.objects.filter(state='tracked')
for vote in votevote:
    choices = vote.votechoice_set.all()  # 이 투표에 투표한 행위들 모두 수정해주기.
    for choice in choices:
        participant = choice.participant
        # 적중률 계산
        part_choices = participant.votechoice_set.all()
        right_answer = 0
        wrong_answer = 0
        null_answer = 0
        for part_choice in part_choices:
            if part_choice.is_answer is None: # 투표 결과를 알 수 없을 때
                null_answer += 1
            elif part_choice.is_answer:
                right_answer += 1
            else:
                wrong_answer += 1

        participant.acc_percent = right_answer / (right_answer + wrong_answer) * 100
        print("{} : {}".format(participant.nickname, participant.acc_percent))
        print("null : {}".format(null_answer))


