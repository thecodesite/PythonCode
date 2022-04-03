#packages
import pandas as pd
import requests
import csv

import matplotlib.pyplot as plt
%matplotlib inline

#set ticker symbol
symbol = 'BTCUSDT'
tick_interval = '30m'

#get candles
def get_candles(start='', symbol='BTCUSDT', tick_interval='1d', limit=1000):
    
    base_url = 'https://api.binance.com/'
    endpoint = 'api/v3/klines?'
    
    if start:
        query = 'symbol=' + symbol + '&interval=' + tick_interval + '&startTime=' + str(start) +'&limit='+str(limit)
    else:
        query = 'symbol=' + symbol + '&interval=' + tick_interval +'&limit='+str(limit)
        
    candles = requests.get(base_url + endpoint + query).json()
    
    return candles, candles[-1][6]  # return candles and last colse time in a tuple
  
  
def get_all_candles_from_start(symbol, tick_interval):  # get each candle as a list
    
    start=1502942400000  # 17 de agosto de 2017
    _, last_time = get_candles(start='', symbol=symbol , tick_interval=tick_interval, limit=1)
    
    candles = []
    while start < last_time:
        i_candles, next_hop = get_candles(start, symbol, tick_interval)
        candles = candles + i_candles
        start = next_hop
        
    return candles
  
#create a datadrame  
candles = get_all_candles_from_start(symbol, tick_interval)
columns=['open_time','open', 'high', 'low','close','volume','close_time','quote','trades',
         'takers_buy_base','takers_buy_quote','ignore']
df = pd.DataFrame(candles, columns=columns)


#sort data by close_time
df = df.sort_values('close_time')
df.drop_duplicates(keep='last')
df = df.astype(float)
df.info()

#plotting
df['close'].plot(figsize=(20,10), label='BTCUSDT')
plt.title('Precio de BTC/USDT')
plt.legend()
plt.grid()

#convert index a datetime
df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')
df['close_time'] = df['close_time'].dt.tz_localize('utc').dt.tz_convert('Europe/Madrid')
df = df.set_index('close_time')







