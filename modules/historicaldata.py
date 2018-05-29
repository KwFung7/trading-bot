#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  _  __         _____                  
 | |/ /_      _|  ___|_  ___ __   __ _ 
 | ' /\ \ /\ / / |_  \ \/ / '_ \ / _` |
 | . \ \ V  V /|  _|  >  <| | | | (_| |
 |_|\_\ \_/\_/ |_|   /_/\_\_| |_|\__, |
                                 |___/ 
Created on Sun May 20 02:55:12 2018
@author: KwFung
"""
import connection
import oandapyV20.endpoints.instruments as instruments

def getData(instrument, day, granularity):    
    # Load account
    api = connection.init()
    
    # Request
    params = {"count": day, "granularity": granularity}
    r = instruments.InstrumentsCandles(instrument, params)
    return api.request(r)




