#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  _  __         _____                  
 | |/ /_      _|  ___|_  ___ __   __ _ 
 | ' /\ \ /\ / / |_  \ \/ / '_ \ / _` |
 | . \ \ V  V /|  _|  >  <| | | | (_| |
 |_|\_\ \_/\_/ |_|   /_/\_\_| |_|\__, |
                                 |___/ 
Created on Sun May 20 19:32:21 2018
@author: KwFung
"""
# Random Forest Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

def buildModel(x, y, treeNum):
    # Fitting Random Forest Regression to the dataset
    regressor = RandomForestRegressor(n_estimators = treeNum, random_state = 0)
    regressor.fit(x, y)

    # Predicting a new result

    # Visualising the Random Forest Regression results (higher resolution)
    x_grid = np.arange(min(x), max(x), 0.01)
    x_grid = x_grid.reshape((len(x_grid), 1))
    plt.scatter(x, y, s = 5, c = 'red')
    plt.plot(x_grid, regressor.predict(x_grid), color = 'blue')
    plt.title('Forex Forecast (Random Forest Regression)')
    plt.xlabel('Datetime')
    plt.ylabel('USD/HKD')
    plt.show()
    
    return regressor
