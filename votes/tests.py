from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import VoteVote
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

def tracking():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Seoul')).replace(tzinfo=None, microsecond=0, second=0)
    finsihed_votes = VoteVote.objects.filter(state=2)
    for vote in finsihed_votes:
        # Tracking 날짜가 되었으면
        if vote.tracked_at <= current_time:
            print("투표 트래킹!")
            vote.state = 3
            coin = Cryptocurrency.objects.get(coin_code=vote.coin.coin_code)
            final_price = coin.cur_price
            price = vote.created_price
            vote.finished_price = final_price
            answer = 1  # 1 : YES가 정답, 2 : NO가 정답.

            # Commnet에 따라서 가격 계산하기
            if vote.comment == 'up': # 오른다?
                expect_price = price + price * float(vote.range) / 100.0
                print("expect price : ", expect_price)
                print("final price : ", final_price)
                if expect_price <= final_price: # 예상 이상으로 올랐으면
                    answer = 1
                else:
                    answer = 2
                print("answer : ", answer)

            elif vote.comment == 'down':
                expect_price = price - price * float(vote.range) / 100.0
                if expect_price >= final_price: # 예상 이상으로 내렸으면
                    answer = 1
                else:
                    answer = 2


            # 오른다고 예상했는데 오른 경우랑 내린다고 예상했는데 내린 경우 제외하고는 False.
            if vote.pos_participants >= vote.neg_participants and answer == 1:
                vote.is_answer = True
            elif vote.pos_participants <= vote.neg_participants and answer == 2:
                vote.is_answer = True
            else:
                vote.is_answer = False

            choices = vote.votechoice_set.all() # 이 투표에 투표한 행위들 모두 수정해주기.
            for choice in choices:
                if choice.choice == answer: # 정답인 경우
                    print("고래밥 지급")
                    try:
                        participant = choice.participant
                        participant.point += vote.earned_point   # 고래밥 지급
                        participant.save()  # 유저에게 고래밥 지급
                    except ObjectDoesNotExist:
                        pass
                    choice.is_answer = True # 정답 여부 추가
                else:
                    choice.is_answer = False
                choice.save()   # 변경 사항 저장

        vote.save() # 투표 모델 변경된것 저장

check_finish()
tracking()