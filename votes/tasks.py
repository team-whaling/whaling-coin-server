from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import VoteVote
from coins.models import Cryptocurrency
import pytz
import datetime

# 투표 끝났는지 확인하는 함수
@shared_task
def check_finish():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Seoul')).replace(tzinfo=None,microsecond=0,second=0)
    ongoing_votes = VoteVote.objects.filter(state=1)
    for vote in ongoing_votes:
        # 투표 마감 기한이 됐으면
        if vote.finished_at == current_time:
            vote.state = 2
            vote.save()


@shared_task
def tracking():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Seoul')).replace(tzinfo=None, microsecond=0, second=0)
    finsihed_votes = VoteVote.objects.filter(state=2)
    for vote in finsihed_votes:
        # Tracking 날짜가 되었으면
        if vote.tracked_at == current_time:
            vote.state = 3
            coin = Cryptocurrency.objects.get(coin_code=vote.coin)
            final_price = coin.cur_price
            price = vote.created_price
            vote.finished_price = final_price
            expect = 1  # 1 : YES가 정답, 2 : NO가 정답.
            # Commnet에 따라서 가격 계산하기
            if vote.comment is 'up': # 오른다?
                expect_price = price + price * float(vote.range) / 100.0
                if expect_price >= final_price: # 예상 이상으로 올랐으면
                    expect = 1
                else:
                    expect = 2

            elif vote.comment is 'down':
                expect_price = price - price * float(vote.range) / 100.0
                if expect_price <= final_price: # 예상 이상으로 내렸으면
                    expect = 1
                else:
                    expect = 2

            # 오른다고 예상했는데 오른 경우랑 내린다고 예상했는데 내린 경우 제외하고는 False.
            if vote.pos_participants >= vote.neg_participants and expect == 1:
                vote.is_answer = True
            elif vote.pos_participants <= vote.neg_participants and expect == 2:
                vote.is_answer = True
            else:
                vote.is_answer = False

            choices = vote.votechoice.all() # 이 투표에 투표한 것들 모두 수정해주기.
            for choice in choices:
                if choice.choice == expect: # 정답인 경우
                    choice.participant.point += vote.earned_point   # 고래밥 지급
                    choice.is_answer = True # 정답 여부 추가
                else:
                    choice.is_answer = False
