#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  _  __         _____                  
 | |/ /_      _|  ___|_  ___ __   __ _ 
 | ' /\ \ /\ / / |_  \ \/ / '_ \ / _` |
 | . \ \ V  V /|  _|  >  <| | | | (_| |
 |_|\_\ \_/\_/ |_|   /_/\_\_| |_|\__, |
                                 |___/ 
Created on Sun May 20 13:39:06 2018
@author: KwFung
"""
import numpy as np
import datetime
import warnings
from connection import Connection
from helpers import candlesparser
from models import svr
from modules import orders
from modules import positions
from modules import priceinfo
from modules import historicaldata
from sklearn.exceptions import DataConversionWarning

# for 1d array deprecation warning
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=DataConversionWarning)

# Load config
connection = Connection()
config = connection.config
instruments = config['INSTRUMENTS'].split(',')
day_range = config['DAY_RANGE'].split(',')
selected_range = config['SELECTED_RANGE']
granularity = config['GRANULARITY']
kernel = config['SVR_KERNEL']
limit_unit = int(config['LIMIT_UNIT'])
order_unit = int(config['ORDER_UNIT'])
min_profit = float(config['MIN_PROFIT'])

# Get current price
now = datetime.datetime.now()
print('************ {} ************\n'.format(str(now)))
price_info = priceinfo.getCurrentPrice(config['INSTRUMENTS'])
currencies = priceinfo.parsePriceInfo(price_info)

# Loop different day range
# Get last N days candles
regressors = {}
print('************ Regression ************\n')
for instrument in instruments:
    for day in day_range:
        data = historicaldata.getData(instrument, day, granularity)
        candles = data['candles']
        date_list = candlesparser.getDate(candles)
        x = candlesparser.getOrdinalDate(candles)
        x = np.vstack(x)
        y = candlesparser.getOHLC(candles)
        
        # Build random svr model and store it in dict
        result = svr.buildModel(x, y, instrument, kernel)
        if instrument in regressors.keys():
            regressors[instrument][day] = result
        else:
            regressors[instrument] = {}
            regressors[instrument][day] = result
            
# Get Account open position
position_res = positions.getOpenPosition()
print('************ Positions ************\n')
print('Get Account Open Position: {}\n'.format(position_res))
print('************ Results ************\n')


# Strategy
for instrument in instruments:
    # Regressor predict
    predict_wk = regressors[instrument][selected_range]['predict_wk']
    ten_day_mean = regressors[instrument][selected_range]['ten_day_mean']
    
    # Current Info
    tradeable = currencies[instrument]['tradeable']
    ask = currencies[instrument]['ask']
    bid = currencies[instrument]['bid']
    
    # Account current position
    # Instrument can be None when no previous position with current instrument
    instrument_list = list(filter(lambda pos : pos['instrument'] == instrument, position_res['positions']))
    instrument_pos = instrument_list[0] if len(instrument_list) > 0 else None
    long = instrument_pos['long'] if instrument_pos is not None else None
    average_price = float(long['averagePrice']) if long is not None else None
    units = int(long['units']) if long is not None else 0
        
    # Flag
    is_rising = predict_wk > ask
    below_mean = ten_day_mean > ask
    is_cheaper = average_price > ask if average_price is not None else below_mean
    below_limit = limit_unit >= order_unit + units
    make_profit = bid > average_price + min_profit if average_price is not None else False
    
    # Logic
    if tradeable:
        # Create Order
        if make_profit:
            # 'Sell' Logic
            # - sell all units when profit higher than min config
            diff = bid - average_price
            profit = diff * units
            order_res = orders.createOrder(str(-units), instrument)
            print('Trading bot sold all {}, around {} units, earn for {}'.format(instrument, units, profit))
        elif is_rising and is_cheaper and below_limit:
            # 'Buy' Logic
            # - Future trend, currency rising
            # - Cheaper than previous order 
            # - OR lower than 10 day average at first purchase
            # - Wont order too much on single currency

            # Create Order
            order_res = orders.createOrder(str(order_unit), instrument)
            print('Trading bot created order on {}, bought {} units.\n'.format(instrument, order_unit))
            # print('Order Creation: {}\n'.format(order_res))
        else:
            print('Trading bot wont take action on {} at this moment.\n'.format(instrument))
    else:
        print('{} currently not available, so cannot create order.\n'.format(instrument))
    


    
