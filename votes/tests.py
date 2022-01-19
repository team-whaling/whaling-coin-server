from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import *
from coins.models import Cryptocurrency
import pytz
import datetime
from django.core.exceptions import ObjectDoesNotExist

def check_finish():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Seoul')).replace(tzinfo=None,microsecond=0,second=0)
    ongoing_votes = VoteVote.objects.filter(state=1)
    for vote in ongoing_votes:
        # 투표 마감 기한이 됐으면
        if vote.finished_at <= current_time:
            print("투표 끝났네!")
            vote.state = 2
            vote.save()


votes = VoteVote.objects.all()
for vote in votes:
    choices = vote.votechoice_set.all()  # 이 투표에 투표한 행위들 모두 수정해주기.
    for choice in choices:
        if choice.choice == 1:  # 정답인 경우
            print("고래밥 지급")
            participant = choice.participant
            participant.point += vote.earned_point  # 고래밥 지급
            choice.is_answer = True  # 정답 여부 추가

            # 적중률 계산
            part_choices = participant.votechoice_set.all()
            right_answer = 0
            wrong_answer = 0
            for part_choice in part_choices:
                if part_choice.is_answer:
                    right_answer += 1
                else:
                    wrong_answer += 1
            participant.acc_percent = right_answer / (right_answer + wrong_answer) * 100
            participant.save()  # 유저에게 고래밥 지급

        else:
            choice.is_answer = False