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
from connection import Connection
import oandapyV20.endpoints.positions as positions

def getOpenPosition():
    # Load config
    connection = Connection()
    accountID = connection.config['ACCOUNT_ID']

    # Request
    r = positions.OpenPositions(accountID)
    return connection.API.request(r)

