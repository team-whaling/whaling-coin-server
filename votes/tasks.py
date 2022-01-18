from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import VoteVote
from coins.models import Cryptocurrency
import pytz
import datetime

# 투표 끝났는지 확인하는 함수g
@shared_task
def check_finish():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Seoul')).replace(tzinfo=None,microsecond=0,second=0)
    ongoing_votes = VoteVote.objects.filter(state=1)
    for vote in ongoing_votes:
        # 투표 마감 기한이 됐으면
        if vote.finished_at == current_time:
            vote.state = 2
            vote.save()

# Commnet에 따라서 가격 계산하기
def calc_coinprice(text, price, percent):
    if text is 'up':    # 오른 가격
        return price + price * float(percent) / 100.0
    elif text is 'down':    # 내린 가격
        return price - (price * float(percent) / 100.0)

@shared_task
def tracking():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Seoul')).replace(tzinfo=None, microsecond=0, second=0)
    finsihed_votes = VoteVote.objects.filter(state=2)
    for vote in finsihed_votes:
        # Tracking 날짜가 되었으면
        if vote.tracked_at == current_time:
            vote.state = 3
            vote.save()
            coin = Cryptocurrency.objects.get(coin_code=vote.coin)
            final_price = coin.cur_price
            vote.finished_price = final_price
            answer_price = calc_coinprice(vote.comment, vote.created_price, vote.range)