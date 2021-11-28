# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 19:31:28 2021

@author: chem_
"""
import time
import pyupbit
import numpy as np
import datetime
import sys
from playsound import playsound

def get_avg_open(ticker, interval, count):
    if count == 1:
        rows = pyupbit.get_ohlcv(ticker, interval, count)['open']
        avg = float(rows[-1])
        return avg
    else:
        rows = pyupbit.get_ohlcv(ticker, interval, count)['open']
        new = rows[:-1]
        a = float(sum(new))
        b = float(len(new))
        avg = a/b
        return avg

def get_avg_high(ticker, interval, count):
    if count == 1:
        rows = pyupbit.get_ohlcv(ticker, interval, count)['high']
        avg = float(rows[-1])
        return avg
    else:
        rows = pyupbit.get_ohlcv(ticker, interval, count)['high']
        new = rows[:-1]
        a = float(sum(new))
        b = float(len(new))
        avg = a/b
        return avg
    
def get_avg_low(ticker, interval, count):
    if count == 1:
        rows = pyupbit.get_ohlcv(ticker, interval, count)['low']
        avg = float(rows[-1])
        return avg
    else:
        rows = pyupbit.get_ohlcv(ticker, interval, count)['low']
        new = rows[:-1]
        a = float(sum(new))
        b = float(len(new))
        avg = a/b
        return avg

def get_avg_close(ticker, interval, count):
    if count == 1:
        rows = pyupbit.get_ohlcv(ticker, interval, count)['close']
        avg = float(rows[-1])
        return avg
    else:
        rows = pyupbit.get_ohlcv(ticker, interval, count)['close']
        new = rows[:-1]
        a = float(sum(new))
        b = float(len(new))
        avg = a/b
        return avg
    
def get_avg_volume(ticker, interval, count):
    if count == 1:
        rows = pyupbit.get_ohlcv(ticker, interval, count)['volume']
        avg = float(rows[-1])
        return avg
    else:
        rows = pyupbit.get_ohlcv(ticker, interval, count)['volume']
        new = rows[:-1]
        a = float(sum(new))
        b = float(len(new))
        avg = a/b
        return avg    

def get_avg_middle(ticker, interval, count):
    avg = get_avg_open(ticker, interval, count) + get_avg_high(ticker, interval, count) + get_avg_low(ticker, interval, count) + get_avg_close(ticker, interval, count)/4
    return avg

#x개 데이터 전 y개 데이터의 평균
def get_previous_avg_open(ticker, x, y):
    raw = []
    rows = pyupbit.get_ohlcv(ticker, interval, count=x+y)['open']
    for n in range(0, x+y):
        raw.append(rows[n])
        time.sleep(0.01)
    new = []
    for n in range(0, y):
        new.append(raw[n])
        time.sleep(0.01)
    a = sum(new)
    b = len(new)
    avg = a/b
    return avg

def get_previous_avg_high(ticker, x, y):
    raw = []
    rows = pyupbit.get_ohlcv(ticker, interval, count=x+y)['high']
    for n in range(0, x+y):
        raw.append(rows[n])
        time.sleep(0.01)
    new = []
    for n in range(0, y):
        new.append(raw[n])
        time.sleep(0.01)
    a = sum(new)
    b = len(new)
    avg = a/b
    return avg

def get_previous_avg_low(ticker, x, y):
    raw = []
    rows = pyupbit.get_ohlcv(ticker, interval, count=x+y)['low']
    for n in range(0, x+y):
        raw.append(rows[n])
        time.sleep(0.01)
    new = []
    for n in range(0, y):
        new.append(raw[n])
        time.sleep(0.01)
    a = sum(new)
    b = len(new)
    avg = a/b
    return avg

def get_previous_avg_close(ticker, x, y):
    raw = []
    rows = pyupbit.get_ohlcv(ticker, interval, count=x+y)['close']
    for n in range(0, x+y):
        raw.append(rows[n])
        time.sleep(0.01)
    new = []
    for n in range(0, y):
        new.append(raw[n])
        time.sleep(0.01)
    a = sum(new)
    b = len(new)
    avg = a/b
    return avg

def get_previous_avg_volume(ticker, x, y):
    raw = []
    rows = pyupbit.get_ohlcv(ticker, interval, count=x+y)['volume']
    for n in range(0, x+y):
        raw.append(rows[n])
        time.sleep(0.01)
    new = []
    for n in range(0, y):
        new.append(raw[n])
        time.sleep(0.01)
    a = sum(new)
    b = len(new)
    avg = a/b
    return avg

def get_previous_avg_middle(ticker, x, y):
    avg = get_previous_avg_open(ticker, x, y) + get_previous_avg_high(ticker, x, y) + get_previous_avg_low(ticker, x, y) + get_previous_avg_close(ticker, x, y) / 4
    return avg



#주어진 관심 코인 목록에 대해서 거래량 평균 딕셔너리 생성 후 직전 거래량과의 비율 가장 큰 코인 찾기
def top_vol_ratio_coin():
    dict_volume = {}
    for ticker in tickers:
        volume_1 = float(get_avg_volume(ticker, interval, count=1))
        volume_count = float(get_avg_volume(ticker, interval, count))
        dict_volume[ticker] = float(volume_1/volume_count)
        time.sleep(0.01)
    top_coin = max(dict_volume, key=dict_volume.get)
    return top_coin

def get_volume_ratio(ticker):
    volume_1 = get_avg_volume(ticker, interval, count=3)
    volume_count = get_avg_volume(ticker, interval, count)
    ratio = volume_1/volume_count
    return ratio

#직전 거래량 딕셔너리 생성하고 직전 거래량 가장 큰 코인 찾기
def find_popular_coin():
    last_volume_dict = {}
    for ticker in tickers:
        last_volume = float(get_avg_volume(ticker, interval, count=1))
        last_volume_dict[ticker] = last_volume
        time.sleep(0.01)
    top_coin = max(last_volume_dict, key=last_volume_dict.get)
    return top_coin

def get_avg_stair(ticker):
    a3 = get_avg_close(ticker, interval, count=4)
    a2 = get_previous_avg_close(ticker, 4, 3)
    a1 = get_previous_avg_close(ticker, 7, 3)
    if a3 > a2 and a2 >= a1:
        return "UP"
    else:
        return "DOWN"

def find_upcoin():
    first = {}
    for ticker in tickers:
        first[ticker] = get_avg_stair(ticker)
    second = []
    for ticker in tickers:
        first[ticker] = "UP"
        second.append(ticker)
        time.sleep(0.01)
    third = []
    for ticker in second:
        now = get_avg_close(ticker, interval, count=6)
        pre = get_previous_avg_close(ticker, 5, 5)
        if float(now/pre) > 1:
            third.append(ticker)
        time.sleep(0.01)
    return third

#관심 코인 목록 초기화
def remove_all(contents):
    while len(contents) > 0:
        del contents[0]
        if len(contents) == 0:
            break

#관심 코인 추가
def add_coin():
    name = input("추가할 코인 이름을 입력하시오. (ex. BTC) / (잘못 입력하셨다면 NO를 입력하세요.)  ==  ")
    if (name not in tickers_short) and ((name != "NO") or (name != "no")):
        return tickers_short.append(name)
    else:
        if name in tickers_short:
            print("이미 관심 코인 목록에 있습니다.")
        elif (name == "NO") or (name == "no"):
            print("관심 코인 추가를 강제 종료합니다.")

#관심 코인 삭제
def del_coin():
    name = input("삭제할 코인 이름을 입력하시오. (ex. BTC) / (잘못 입력하셨다면 NO를 입력하세요.)  ==  ")
    if (name in tickers_short) and ((name != "NO") or (name != "no")):
        return tickers_short.remove(name)
    else:
        if (name == "NO"):
            print("관심 코인 제거를 강제 종료합니다.")
        elif name not in tickers:
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
def get_ror(ticker, k=0.5):
    df = pyupbit.get_ohlcv(ticker, interval, count)
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
    target_price = get_avg_close(ticker, interval, count=3) + (get_avg_high(ticker, interval, count=10) - get_avg_low(ticker, interval, count=10)) * k
    return target_price

#구간 내 가장 높은 OHLC 조회
def get_highest_open(ticker):
    raw = pyupbit.get_ohlcv(ticker, interval, count)['open']
    raw_data = []
    for x in range(0, count):
        raw_data.append(raw[x])
        time.sleep(0.01)
    highest = max(raw_data)
    return highest

def get_highest_high(ticker):
    raw = pyupbit.get_ohlcv(ticker, interval, count)['high']
    raw_data = []
    for x in range(0, count):
        raw_data.append(raw[x])
        time.sleep(0.01)
    highest = max(raw_data)
    return highest

def get_highest_low(ticker):
    raw = pyupbit.get_ohlcv(ticker, interval, count)['low']
    raw_data = []
    for x in range(0, count):
        raw_data.append(raw[x])
        time.sleep(0.01)
    highest = max(raw_data)
    return highest

def get_highest_close(ticker):
    raw = pyupbit.get_ohlcv(ticker, interval, count)['close']
    raw_data = []
    for x in range(0, count):
        raw_data.append(raw[x])
        time.sleep(0.01)
    highest = max(raw_data)
    return highest

#구간 내 가장 낮은 OHLC 조회
def get_lowest_open(ticker, interval, count):
    raw = pyupbit.get_ohlcv(ticker, interval, count)['open']
    raw_data = []
    for x in range(0, count):
        raw_data.append(raw[x])
        time.sleep(0.01)
    lowest = min(raw_data)
    return lowest

def get_lowest_high(ticker, interval, count):
    raw = pyupbit.get_ohlcv(ticker, interval, count)['high']
    raw_data = []
    for x in range(0, count):
        raw_data.append(raw[x])
        time.sleep(0.01)
    lowest = min(raw_data)
    return lowest

def get_lowest_low(ticker, interval, count):
    raw = pyupbit.get_ohlcv(ticker, interval, count)['low']
    raw_data = []
    for x in range(0, count):
        raw_data.append(raw[x])
        time.sleep(0.01)
    lowest = min(raw_data)
    return lowest

def get_lowest_close(ticker, interval, count):
    raw = pyupbit.get_ohlcv(ticker, interval, count)['close']
    raw_data = []
    for x in range(0, count):
        raw_data.append(raw[x])
        time.sleep(0.01)
    lowest_close = min(raw_data)
    return lowest_close

def find_coin_for_trade():
    upcoins = find_upcoin()
    # print(upcoins)
    # print("")
    
    vol_ratio = {}
    for ticker in upcoins:
        vol_ratio[ticker] = get_avg_volume(ticker,interval, count=4)/get_avg_volume(ticker, interval, count)
    # print(vol_ratio)
    # print("")
    
    selected_upcoins = []
    for ticker in upcoins:
        # ticker_name = ticker
        if vol_ratio[ticker] > 1 and vol_ratio[ticker] < 2:
            selected_upcoins.append(ticker)
        else:
            # msg = "{}은 자격요건 1을 만족하지 않습니다.".format(ticker_name)
            # print(msg)
            time.sleep(0.001)
    # print(selected_upcoins)
    
    selects_for_trade = []
    for ticker in selected_upcoins:
        if selected_upcoins != []:
            dict_k_and_ror = {}
            for k in np.arange(0.01, 1.0, 0.01):
                ror = get_ror(ticker, k)
                dict_k_and_ror[k] = ror
                time.sleep(0.01)
        else:
            # msg = "자격요건 1을 만족하는 코인이 없습니다."
            # print(msg)
            time.sleep(0.001)
        max_k = max(dict_k_and_ror, key=dict_k_and_ror.get)
        current_price = get_current_price(ticker)
        target_price = get_target_price(ticker, max_k)
        # ticker_name = ticker
        if current_price > target_price:
            selects_for_trade.append(ticker)
        else:
            # msg = "{}은 자격요건 2를 만족하지 않습니다.".format(ticker_name)
            # print(msg)
            time.sleep(0.001)
    
    trade_list = []
    for ticker in selects_for_trade:
        ma3 = get_avg_close(ticker, interval, count=4)
        pre_ma3 = get_previous_avg_close(ticker, 4, 3)
        ratio = ma3 / pre_ma3
        # ticker_name = ticker
        if ratio > 1 and ratio < 2:
            trade_list.append(ticker)
        else:
            # msg = "{}은 자격요건 3을 만족하지 않습니다.".format(ticker_name)
            # print(msg)
            time.sleep(0.001)
    
    trade_dict = {}
    for ticker in trade_list:
        ma3 = get_avg_close(ticker, interval, count=4)
        pre_ma3 = get_previous_avg_close(ticker, 4, 3)
        ratio = ma3 / pre_ma3
        trade_dict[ticker] = ratio
    if trade_dict != {}:
        final_coin = max(trade_dict, key=trade_dict.get)
    else:
        time.sleep(0.001)
        
    if upcoins == []:
        return False
    elif selected_upcoins == []:
        return False
    elif selects_for_trade == []:
        return False
    elif trade_list == []:
        return False
    elif trade_dict == {}:
        return False
    elif final_coin[:3] == "KRW":
        return final_coin
    else:
        return False

# access & secret keys
access = "access"
secret = "secret"

print("관심 코인 목록을 설정합니다.")
print("")
print("====")
print("")
print("1. 전체 코인 목록에서 삭제하는 방식")
print("2. 직접 하나씩 추가하는 방식")
print("3. 기존 코인 목록 선택")
choice = int(input("1 or 2 or 3 ============ >  "))
print("")
print("====")
print("")

if choice == 1:
    tickers_short = []
    raw = pyupbit.get_tickers("KRW")
    length_of_raw = len(raw)
    for x in range(0, length_of_raw):
        tickers_short.append(raw[x][4:])
elif choice == 2:
    tickers_short = []
elif choice == 3:
    tickers_short = ["FLOW", "SAND", "MANA", "BTC", "MOC", "ETH", "ENJ", "WAXP", "AXS", "CHZ", "THETA", "BCH", "BTG", "BSV", "ETC"]
else:
    print("잘못된 입력입니다.")
    print("자동 매매 프로그램을 중단합니다.")
    sys.exit()

print("관심 코인 목록을 불러옵니다.")
print("====")

reset = input("관심 종목을 초기화 하시겠습니까?  Y or N  ==  ")
if  (reset == "Y") or (reset == "y"):
    remove_all(tickers_short)
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
    delete = input("관심 코인을 삭제하시겠습니니까?  Y or N  ==  ")
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

tickers = []
for x in range(0, len(tickers_short)):
    tickers.append("KRW-"+tickers_short[x])

print("")
print("====")
print("")
print(tickers)
print("")
print("====")
print("")
print("interval 값을 설정합니다.")
print("")
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
count = int(input("조회 데이터 양을 설정합니다. (max 200)  ==  "))
print("")
print("====")
print("")
interval_msg = "설정 interval은 {} 입니다.".format(interval)
count_msg = "설정 조회 데이터 수는 {} 입니다.".format(count)
print(interval_msg)
print(count_msg)
print("")
print("====")
print("")
goal_profit1 = float(input("stair = UP 일 때 목표 수익률 (ex.1.15)  ==  "))
print("")
print("====")
print("")
goal_profit2 = float(input("stair = UP 일 때 손절 수익률 (ex.0.85)  ==  "))
print("")
print("====")
print("")
goal_profit3 = float(input("stair = DOWN 일 때 목표 수익률 (ex.1.015)  ==  "))
print("")
print("====")
print("")
goal_profit4 = float(input("stair = DOWN 일 때 손절 수익률 (ex.0.90)  ==  "))
print("")
print("====")
print("")
goal_profit1_msg = "stair = UP 일 때의 설정 목표 수익률은 {} 입니다.".format(goal_profit1)
goal_profit2_msg = "stair = UP 일 때의 설정 손절 수익률은 {} 입니다.".format(goal_profit2)
goal_profit3_msg = "stair = DOWN 일 때의 설정 목표 수익률은 {} 입니다.".format(goal_profit3)
goal_profit4_msg = "stair = DOWN 일 때의 설정 손절 수익률은 {} 입니다.".format(goal_profit4)

print(goal_profit1_msg)
print(goal_profit2_msg)
print(goal_profit3_msg)
print(goal_profit4_msg)
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
            krw_balance_check_msg = "{} 현재 원화 잔고는 {}원 입니다.".format(now_time, krw_balance)
            
            if krw_balance > 5000:
                print(krw_balance_check_msg)
                print("")
                print("====")
                print("")
                print("관심 코인 분석을 시작합니다.")
                print("")
                print("====")
                print("")
                selected = find_coin_for_trade()               
                if selected != False:
                    print(selected)
                    current_price = get_current_price(selected)
                    avg_close = get_avg_close(selected, interval, count=10)
                    avg_close3 = get_avg_close(selected, interval, count=4)
                    lowest_close10 = get_lowest_close(selected, interval, count=10)
                    dict_k_and_ror = {}
                    for k in np.arange(0.01, 1.0, 0.01):
                        ror = get_ror(selected, k)
                        dict_k_and_ror[k] = ror
                        time.sleep(0.01)
                    max_k = max(dict_k_and_ror, key=dict_k_and_ror.get)
                
                    if current_price >= avg_close3*(1-max_k) and current_price <= avg_close3*(1+max_k):
                        upbit.buy_market_order(selected, krw_balance*0.995)
                        playsound("c:\\auto\\buy.mp3")
                        buy_msg = "{} 현재 {}을 {}원에 매수 진행했습니다.".format(now_time, selected, current_price)
                        print(buy_msg)
                        print("")
                        print("====")
                        print("")
                        time.sleep(0.01)

                    else:
                        print("조건에 부합하는 코인이 없어 매수를 진행하지 않습니다.")
                        print("")
                        print("재탐색을 시작합니다.")
                        print("")
                        print("====")
                        print("")
                        time.sleep(10)
                else:
                    print("조건에 부합하는 코인이 없어 매수를 진행하지 않습니다.")
                    print("")
                    print("재탐색을 시작합니다.")
                    print("")
                    print("====")
                    print("")
                    time.sleep(10)

            else:
                mine = str(my_coin())
                coin_balance = float(upbit.get_balance(mine[4:]))
                coin_balance_won = get_current_price(mine) * coin_balance
                coin_balance_check_msg = "{} 현재 코인 잔고는 {} {}개 / 원화 기준 {}원 입니다.".format(now_time, mine, coin_balance, coin_balance_won)
                print(coin_balance_check_msg)
                status = get_avg_stair(mine)
                status_msg = "추세는 {}".format(status)
                print("")
                print(status_msg)
                print("")
                print("====")
                print("")
                
                if coin_balance_won > 5000:
                    avg_buy_price = upbit.get_avg_buy_price(mine)
                    current_price_mine = get_current_price(mine)
                    ratio = current_price_mine / avg_buy_price
                    profit = (current_price_mine - avg_buy_price)*coin_balance
                    stair = get_avg_stair(mine)
                    avg_high_mine = get_avg_high(mine, interval, count=10)
                    avg_close_mine = get_avg_close(mine, interval, count=10)
                    avg_low_mine = get_avg_close(mine, interval, count=10)
                    dict_k_and_ror_mine = {}
                    for k in np.arange(0.01, 1.0, 0.01):
                        ror = get_ror(mine, k)
                        dict_k_and_ror_mine[k] = ror
                        time.sleep(0.01)
                    max_k_mine = max(dict_k_and_ror_mine, key=dict_k_and_ror_mine.get)
                    if stair == "UP" and ratio >= goal_profit1:
                        upbit.sell_market_order(mine, coin_balance*1)
                        playsound("c:\\auto\\sell.mp3")
                        sell_msg = "조건1 / {} 현재 {}을 {}원에 매도 진행했습니다. 손익 {}원".format(now_time, mine, current_price_mine, profit)
                        print(sell_msg)
                    elif stair == "UP" and ratio <= goal_profit2:
                        upbit.sell_market_order(mine, coin_balance*1)
                        playsound("c:\\auto\\sell.mp3")
                        sell_msg = "조건2 / {} 현재 {}을 {}원에 매도 진행했습니다. 손익 {}원".format(now_time, mine, current_price_mine, profit)
                        print(sell_msg)
                    elif stair == "DOWN" and ratio >= goal_profit3:
                        upbit.sell_market_order(mine, coin_balance*1)
                        playsound("c:\\auto\\sell.mp3")
                        sell_msg = "조건3 / {} 현재 {}을 {}원에 매도 진행했습니다. 손익 {}원".format(now_time, mine, current_price_mine, profit)
                        print(sell_msg)
                    elif stair == "DOWN" and ratio <= goal_profit4:
                        upbit.sell_market_order(mine, coin_balance*1)
                        playsound("c:\\auto\\sell.mp3")
                        sell_msg = "조건4 / {} 현재 {}을 {}원에 매도 진행했습니다. 손익 {}원".format(now_time, mine, current_price_mine, profit)
                        print(sell_msg)
                    else:
                        print("조건에 부합하지 않아 매도를 진행하지 않습니다.")
                        time.sleep(0.001)
                else:
                    time.sleep(0.001)

    except Exception as e:
        print(e)
        time.sleep(1)