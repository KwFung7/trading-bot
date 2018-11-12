#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  _  __         _____                  
 | |/ /_      _|  ___|_  ___ __   __ _ 
 | ' /\ \ /\ / / |_  \ \/ / '_ \ / _` |
 | . \ \ V  V /|  _|  >  <| | | | (_| |
 |_|\_\ \_/\_/ |_|   /_/\_\_| |_|\__, |
                                 |___/ 
Created on Mon May 21 21:51:38 2018
@author: KwFung
"""
# SVR

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
from connection import Connection
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

def buildModel(x, y, instrument, kernel):
    print('Day range: {}'.format(len(x)))
    
    # mean for last N day
    connection = Connection()
    day_for_mean = int(connection.config['DAY_FOR_MEAN'])
    prev_data = y[-day_for_mean:]
    day_mean = np.mean(prev_data)
    print('Last {} days mean of OHLC: {}'.format(day_for_mean, day_mean))
    
    # Feature Scaling
    sc_x = StandardScaler()
    sc_y = StandardScaler()
    trans_x = sc_x.fit_transform(x)
    trans_y = sc_y.fit_transform(y)
    
    # Fitting SVR to the dataset
    regressor = SVR(kernel)
    regressor.fit(trans_x, trans_y)
    r_square = regressor.score(trans_x, trans_y)
    print('R square score: {}'.format(r_square))
    
    # Predicting a new result
    WEEK = 7
    MONTH = 30
    predict_wk = x[len(x) - 1] + WEEK
    predict_mth = x[len(x) - 1] + MONTH
    y_pred_wk = regressor.predict(sc_x.transform(np.vstack(np.array(predict_wk))))
    y_pred_wk = float(sc_y.inverse_transform(y_pred_wk)[0])
    y_pred_mth = regressor.predict(sc_x.transform(np.vstack(np.array(predict_mth))))
    y_pred_mth = float(sc_y.inverse_transform(y_pred_mth)[0])
    print('Predict {} for {} days: {}'.format(instrument, WEEK, y_pred_wk))
    print('Predict {} for {} days: {}'.format(instrument, MONTH, y_pred_mth))
    
    '''
    # Visualising the SVR results (for higher resolution and smoother curve)
    x_grid = np.arange(min(trans_x), max(trans_x), 0.01)
    x_grid = x_grid.reshape((len(x_grid), 1))
    plt.scatter(trans_x, trans_y, s = 5, c = 'red')
    plt.plot(x_grid, regressor.predict(x_grid), c = 'blue')
    plt.title('Forex Forecast (SVR)')
    plt.xlabel('Datetime')
    plt.ylabel(instrument)
    plt.show()
    '''
    print('\n')
    
    return {
        "score": r_square,
        "predict_wk": y_pred_wk,
        "predict_mth": y_pred_mth,
        "day_mean": day_mean
    }
