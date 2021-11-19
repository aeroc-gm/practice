# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 23:38:04 2021

@author: chem_
"""
import time
import pyupbit
import numpy as np
import datetime
import sys

# access & secret keys
access = str(input("access key를 입력하세요  ==  "))
secret = str(input("secret key를 입력하세요  ==  "))

print("관심 코인 목록을 설정합니다.")
print("1. 전체 코인 목록에서 제거하는 방식")
print("2. 직접 하나씩 추가하는 방식")
choice = int(input("1 or 2 ============ >  "))

if choice == 1:
    favorites = []
    tickers = pyupbit.get_tickers("KRW")
    length_of_tickers = len(pyupbit.get_tickers("KRW"))
    for x in range(0, length_of_tickers):
        favorites.append(tickers[x][4:])
elif choice == 2:
    favorites = []
else:
    print("잘못된 입력입니다.")
    print("자동 매매 프로그램을 중단합니다.")
    sys.exit()

print("기존 관심 코인 목록을 불러옵니다.")
print("====")
print(favorites)


#주어진 interval, count에 대해서 시가 평균 구하기
def get_avg_open(ticker, interval, count):
    trading_open = []
    for x in range(0, count):
        trading_open.append(pyupbit.get_ohlcv(ticker, interval, count)['open'][x])
        time.sleep(0.05)
    result1 = sum(trading_open)
    result2 = len(trading_open)
    result3 = result1 / result2
    return result3

#주어진 interval, count에 대해서 고가 평균 구하기
def get_avg_high(ticker, interval, count):
    trading_high = []
    for x in range(0, count):
        trading_high.append(pyupbit.get_ohlcv(ticker, interval, count)['high'][x])
        time.sleep(0.05)
    result1 = sum(trading_high)
    result2 = len(trading_high)
    result3 = result1 / result2
    return result3

#주어진 interval, count에 대해서 저가 평균 구하기
def get_avg_low(ticker, interval, count):
    trading_low = []
    for x in range(0, count):
        trading_low.append(pyupbit.get_ohlcv(ticker, interval, count)['low'][x])
        time.sleep(0.05)
    result1 = sum(trading_low)
    result2 = len(trading_low)
    result3 = result1 / result2
    return result3

#주어진 interval, count에 대해서 종가 평균 구하기
def get_avg_close(ticker, interval, count):
    trading_close = []
    for x in range(0, count):
        trading_close.append(pyupbit.get_ohlcv(ticker, interval, count)['close'][x])
        time.sleep(0.05)
    result1 = sum(trading_close)
    result2 = len(trading_close)
    result3 = result1 / result2
    return result3

#주어진 interval, count에 대해서 거래량 평균 구하기
def get_avg_volume(ticker, interval, count):
    trading_volume = []
    for x in range(0, count):
        trading_volume.append(pyupbit.get_ohlcv(ticker, interval, count)['volume'][x])
        time.sleep(0.05)
    result1 = sum(trading_volume)
    result2 = len(trading_volume)
    result3 = result1 / result2
    return result3

#주어진 관심 코인 목록에 대해서 시가 평균 딕셔너리 생성
def avg_open_dict(favorites, interval, count):
    dict_tickers_open = {}
    for favorites in fn_favorites:
        open_open = get_avg_open(favorites, interval, count)
        dict_tickers_open[favorites] = open_open
        time.sleep(0.05)
    return dict_tickers_open

#주어진 관심 코인 목록에 대해서 고가 평균 딕셔너리 생성
def avg_high_dict(favorites, interval, count):
    dict_tickers_high = {}
    for favorites in fn_favorites:
        high = get_avg_high(favorites, interval, count)
        dict_tickers_high[favorites] = high
        time.sleep(0.05)
    return dict_tickers_high

#주어진 관심 코인 목록에 대해서 저가 평균 딕셔너리 생성
def avg_low_dict(favorites, interval, count):
    dict_tickers_low = {}
    for favorites in fn_favorites:
        low = get_avg_low(favorites, interval, count)
        dict_tickers_low[favorites] = low
        time.sleep(0.05)
    return dict_tickers_low

#주어진 관심 코인 목록에 대해서 종가 평균 딕셔너리 생성
def avg_close_dict(favorites, interval, count):
    dict_tickers_close = {}
    for favorites in fn_favorites:
        close = get_avg_close(favorites, interval, count)
        dict_tickers_close[favorites] = close
        time.sleep(0.05)
    return dict_tickers_close

#주어진 관심 코인 목록에 대해서 거래량 평균 딕셔너리 생성
def avg_volume_dict(favorites, interval, count):
    dict_tickers_volume = {}
    for favorites in fn_favorites:
        volume = get_avg_volume(favorites, interval, count)
        dict_tickers_volume[favorites] = volume
        time.sleep(0.05)
    return dict_tickers_volume

#관심 코인 목록 초기화
def remove_all(contents):
    while len(contents) > 0:
        del contents[0]
        if len(contents) == 0:
            break

#관심 코인 추가
def add_coin():
    name = input("추가할 코인 이름을 입력하시오. ex. BTC  ==  / 잘못 입력하셨다면 NO를 입력하세요.")
    if (name not in favorites) and ((name != "NO") or (name != "no")):
        return favorites.append(name)
    else:
        if name in favorites:
            print("이미 관심 코인 목록에 있습니다.")
        elif (name == "NO") or (name == "no"):
            print("관심 코인 추가를 강제 종료합니다.")

#관심 코인 삭제
def del_coin():
    name = input("삭제할 코인 이름을 입력하시오. ex. BTC  ==  / 잘못 입력하셨다면 NO를 입력하세요.")
    if (name in favorites) and ((name != "NO") or (name != "no")):
        return favorites.remove(name)
    else:
        if (name == "NO"):
            print("관심 코인 제거를 강제 종료합니다.")
        elif name not in favorites:
            print("관심 코인 목록에 없는 코인입니다.")
            
#코인 현재가 조회
def get_current_price(ticker):
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

#조건에 의해 매수한 코인 조회
def my_coin():
    balances_contents = []
    x = 0
    for x in range(0, len(upbit.get_balances())):
        balances_contents.append(upbit.get_balances()[x]['currency'])
    balances_contents.remove("KRW")
    balances_contents.remove("SRN")
    return str("KRW-"+balances_contents[0])

#best k
def get_ror(coin, k=0.5):
    df = pyupbit.get_ohlcv(coin, interval, count)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.005
    df['ror'] = np.where(df['high'] > df['target'],
                          df['close'] / df['target'] - fee,
                          1)

    ror = df['ror'].cumprod()[-2]
    return ror

#변동성 돌파 전략으로 목표 매수가 조회
def get_target_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval, count)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

reset = input("관심 종목을 초기화 하시겠습니까?  Y or N  ==  ")
if  (reset == "Y") or (reset == "y"):
    remove_all(favorites)
elif (reset == "N") or reset == "n":
    print("")
    print("====")
    print("")
    print("다음 단계로 넘어갑니다.")
    print("")
    print("====")
    print("")
while True:
    add = input("관심 코인을 추가하시겠습니까?  Y or N  ==  ")
    if (add == "Y") or add == "y":
        add_coin()
    elif (add == "N") or (add == "n"):
        print("")
        print("====")
        print("")
        print("다음 단계로 넘어갑니다.")
        print("")
        print("====")
        print("")
        break
while True:
    delete = input("관심 코인을 제거하시겠습니니까?  Y or N  ==  ")
    if (delete  == "Y") or (delete  == "y"):
        del_coin()
    elif (delete  == "N") or (delete  == "n"):
        print("")
        print("====")
        print("")
        print("다음 단계로 넘어갑니다.")
        print("")
        print("====")
        print("")  
        break

print("수정된 관심 코인 목록을 불러옵니다.")

fn_favorites = []
for x in range(0, len(favorites)):
    fn_favorites.append("KRW-"+favorites[x])

print(favorites)
print("")
print("====")
print("")
print(fn_favorites)
print("")
print("====")
print("")
print("interval 값을 설정합니다.")
print("1. minutes1")
print("2. minutes3")
print("3. minutes5")
print("4. minutes10")
print("5. minutes15")
print("6. minutes30")
print("7. minutes60")
print("8. minutes240")
print("9. day")
print("10. week")
print("11. month")
interval_input = int(input("번호를 입력해 interval을 설정하세요. 번호  ==  "))
if interval_input == 1:
    interval = 'minutes1'
elif interval_input == 2:
    interval = 'minutes3'
elif interval_input == 3:
    interval = 'minutes5'
elif interval_input == 4:
    interval = 'minutes10'
elif interval_input == 5:
    interval = 'minutes15'
elif interval_input == 6:
    interval = 'minutes30'
elif interval_input == 7:
    interval = 'minutes60'
elif interval_input == 8:
    interval = 'minutes240'
elif interval_input == 9:
    interval = 'day'
elif interval_input == 10:
    interval = 'week'
elif interval_input == 11:
    interval = 'month'
print("")
print("====")
print("")
count = int(input("조회 데이터 양을 설정합니다. max 200  "))
print("")
print("====")
print("")
print(interval)
print(count)
print("")
print("====")
print("")

check = input("자동 매매를 시작할까요?  Y or N  ==  ")
if (check == "Y") or (check == "y"):
    #로그인
    upbit = pyupbit.Upbit(access, secret)
    print("")
    print("====")
    print("")
    print("autotrade start")
    print("")
    print("====")
    print("")
elif (check == "N") or (check == "n"):
    sys.exit()

while True:
    try:
        now = datetime.datetime.now()
        now_time = now.replace(microsecond=0)
        start_time = now - datetime.timedelta(hours=6)
        end_time = now + datetime.timedelta(hours=6)
        
        if start_time < now < end_time:
            krw_balance = float(upbit.get_balance("KRW"))
                        
            if krw_balance > 5000:
                krw_balance_check_msg = "{} 현재 원화 잔고는 {}원 입니다.".format(now_time, krw_balance)
                print(krw_balance_check_msg)
                print("")
                print("====")
                print("")
                print("관심 코인 분석을 시작합니다.")
                print("")
                print("====")
                print("")
                
                volume_count_1 = []
                for favorites in fn_favorites:
                    volume_count_1.append(get_avg_volume(favorites, interval, count=1))
                # print(volume_count_1)
                
                volume_count_initial = []
                for favorites in fn_favorites:
                    volume_count_initial.append(get_avg_volume(favorites, interval, count))
                # print(volume_count_initial)
                
                volume_ratio = []
                for x in range(0, len(fn_favorites)):
                    volume_ratio.append((volume_count_1[x])/(volume_count_initial[x]))
                # print(ratio)
                
                volume_ratio_dict = {}
                for favorites in fn_favorites:
                    volume_ratio_dict[favorites] = volume_ratio[fn_favorites.index(favorites)]
                    time.sleep(0.05)
                
                # print(volume_ratio_dict)
                # print("")
                # print("====")
                # print("")
                
                #top_volume_ratio_coin은 직전 거래량이 평균 거래량 보다 가장 높은 코인
                top_volume_ratio_coin = max(volume_ratio_dict, key=volume_ratio_dict.get)
                msg_for_volume = "{} 현재 평균 대비 거래량이 가장 많은 코인은 {} 입니다.".format(now_time, top_volume_ratio_coin)
                print(msg_for_volume)
                print("")
                print("====")
                print("")
                
                # volume_ratio_dict[top_volume_ratio]는 top_volume_ratio로 선정된 코인의 volume_ratio
                msg_for_vol_ratio = "비율은 {} 입니다.".format(volume_ratio_dict[top_volume_ratio_coin])
                print(msg_for_vol_ratio)
                print("")
                print("====")
                print("")
                selected_coin = top_volume_ratio_coin
                selected_coin_vol_ratio = volume_ratio_dict[top_volume_ratio_coin]
                
                close_count_1 = get_avg_close(selected_coin, interval, count=1)
                close_count_initial = get_avg_close(selected_coin, interval, count)
                close_ratio = (close_count_1)/(close_count_initial)
                                            
                current_price = get_current_price(selected_coin)
                
                dict_k_and_ror = {}
                for k in np.arange(0.01, 1.0, 0.01):
                    ror = get_ror(selected_coin, k)
                    dict_k_and_ror[k] = ror
                    time.sleep(0.04)
                
                max_k = max(dict_k_and_ror, key=dict_k_and_ror.get)
                
                target_price = get_target_price(selected_coin, max_k)
                target_price_msg = "목표 매수가는 {} 원 입니다.".format(target_price)
                print(target_price_msg)
                print("")
                print("====")
                print("")                
                
                if  (float(selected_coin_vol_ratio) > 2.5) and (target_price < current_price):
                # if  (selected_coin_vol_ratio > 2.5) and (close_ratio < 1.05) and (close_ratio > 0.95) and (target_price < current_price):
                    upbit.buy_market_order(selected_coin, krw_balance*0.995)
                    buy_msg = "{} 현재 {}을 {}원에 매수 진행했습니다.".format(now_time, selected_coin, current_price)
                    print(buy_msg)
                    print("")
                    print("====")
                    print("")
                    
                    # coin_of_mine = str(my_coin())
                    # my_coin_balance = float(upbit.get_balance(coin_of_mine[4:]))
                    # my_coin_balance_bywon = (get_current_price(coin_of_mine)) * (my_coin_balance)
                    # coin_balance_check_msg1 = "{} 현재 코인 잔고는 코인 기준 {} 개 / 원화 기준 {} / {}원 입니다.".format(now_time, my_coin_balance, coin_of_mine, my_coin_balance_bywon)
                    # print(coin_balance_check_msg1)
                    # print("")
                    # avg_buy_price = upbit.get_avg_buy_price(coin_of_mine)
                    # coin_balance_check_msg2 = "매수 평균가는 {} 입니다.".format(avg_buy_price)
                    # print(coin_balance_check_msg2)
                    # print("")
                    # print("====")
                    # print("")
                else:
                    print("조건에 부합하지 않아 코인 매수를 진행하지 않습니다.")
                    print("")
                    print("60초 후 재탐색을 시작합니다.")
                    print("")
                    print("====")
                    print("")
                    time.sleep(60)
                    
            else:
                coin_of_mine = str(my_coin())
                my_coin_balance = float(upbit.get_balance(coin_of_mine[4:]))
                my_coin_balance_bywon = (get_current_price(coin_of_mine)) * (my_coin_balance)
                coin_balance_check_msg1 = "{} 현재 코인 잔고는 코인 기준 {} 개 / 원화 기준 {} / {}원 입니다.".format(now_time, my_coin_balance, coin_of_mine, my_coin_balance_bywon)
                print(coin_balance_check_msg1)
                print("")
                avg_buy_price = upbit.get_avg_buy_price(coin_of_mine)
                coin_balance_check_msg2 = "매수 평균가는 {} 입니다.".format(avg_buy_price)
                print(coin_balance_check_msg2)
                print("")
                print("====")
                print("")
                if my_coin_balance_bywon > 5000:
                    # coin_of_mine = str(my_coin())
                    # my_coin_balance = float(upbit.get_balance(coin_of_mine[4:]))
                    # my_coin_balance_bywon = (get_current_price(coin_of_mine)) * (my_coin_balance)                    
                    current_price_mine = get_current_price(coin_of_mine)
                    if (((avg_buy_price)*1.015) <= current_price_mine) or (((avg_buy_price)*0.97) >= current_price_mine):
                        now_price = get_current_price(coin_of_mine)
                        upbit.sell_market_order(coin_of_mine, my_coin_balance*1)
                        sell_msg = "{} 현재 {}을 {}원에 매도 진행했습니다.".format(now_time, coin_of_mine, now_price)
                        print(sell_msg)
                        print("")
                        print("====")
                        print("")
                        print("다음 거래 준비를 위해 10초간 휴식 시간을 가집니다.")
                        time.sleep(10)
                    else:
                        current_msg = "코인의 현재 가격은 {} 원 입니다.".format(current_price_mine)
                        print(current_msg)
                        print("")
                        print("조건에 부합하지 않아 코인 매도를 진행하지 않습니다.")
                        print("")
                        print("1초 후 조건을 다시 확인합니다.")
                        print("")
                        print("====")
                        print("")
                        time.sleep(1)
            
    except Exception as e:
        print(e)
        time.sleep(1)