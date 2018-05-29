#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  _  __         _____                  
 | |/ /_      _|  ___|_  ___ __   __ _ 
 | ' /\ \ /\ / / |_  \ \/ / '_ \ / _` |
 | . \ \ V  V /|  _|  >  <| | | | (_| |
 |_|\_\ \_/\_/ |_|   /_/\_\_| |_|\__, |
                                 |___/ 
Created on Sat May 26 20:09:46 2018
@author: KwFung
"""
import connection
import oandapyV20.endpoints.positions as positions

def getOpenPosition():
    # Load config
    config = connection.loadConfig()
    accountID = config['ACCOUNT_ID']
    
    # Load account
    api = connection.init()

    # Request
    r = positions.OpenPositions(accountID)
    return api.request(r)

