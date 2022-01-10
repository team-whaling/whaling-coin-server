from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Cryptocurrency
import pytz
import datetime
import requests

# API 호출 정리
def call_api(url, **params):
    response = requests.get(url, params=params)
    return response.json()

def get_tickers():  # 전체 티커 다 가져오는 함수. 혹시 몰라서 영문명도 땡겨옴
    url = "https://api.upbit.com/v1/market/all" # 여기서 KRW-BTC, 비트코인, bitcoin 다 갖고옴
    markets = call_api(url)
    tickers = []
    korean_name = []
    english_name = []
    for x in markets:
        if x['market'].startswith("KRW"):
            tickers.append(x['market'])
            korean_name.append(x['korean_name'])
            english_name.append(x['english_name'])
    return tickers, korean_name, english_name

def get_price():    # 우리 디비에 들어갈 정보들 다 가져오는 함수
    tickers, ko_name, eng_name = get_tickers()
    url = "https://api.upbit.com/v1/ticker"
    data = call_api(url,markets=tickers)
    ret = []
    index = 0
    for x in data:
        response = {
            "coin_code" : x['market'][4:],
            "coin_name" : ko_name[index],
            "cur_price" : x['trade_price'],
            "trade_date" : x['trade_date_kst'],
            "trade_time" : x['trade_time_kst']
        }
        index += 1
        ret.append(response)
    return ret

@shared_task
def update_api():   # 없으면 생성, 있으면 가격 업데이트.
    api_data = get_price()
    print("Update CryptoCurrrency")
    kst_time = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    ymd = int(kst_time.strftime('%Y%m%d'))  # 업데이트 된 시간을 날짜랑 시간으로 나눠서
    hm = int(kst_time.strftime('%H%M'))
    for data in api_data:
        try:
            crypto = Cryptocurrency.objects.get(coin_code = data['coin_code'])
            crypto.cur_price = data['cur_price']
            crypto.trade_date = data['trade_date']
            crypto.trade_time = data['trade_time']
            crypto.updated_date = ymd
            crypto.updated_time = hm
            crypto.save()
        except Cryptocurrency.DoesNotExist: # 객체가 존재하지 않을 경우 생성
            Cryptocurrency.objects.create(coin_code = data['coin_code'],
                                          coin_name = data['coin_name'],
                                          coin_fullname = data['coin_name'] + '(' + data['coin_code'] + ')',
                                          cur_price = data['cur_price'],
                                          trade_date = data['trade_date'],
                                          trade_time = data['trade_time'],
                                          updated_date = ymd,
                                          updated_time = hm)