#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  _  __         _____                  
 | |/ /_      _|  ___|_  ___ __   __ _ 
 | ' /\ \ /\ / / |_  \ \/ / '_ \ / _` |
 | . \ \ V  V /|  _|  >  <| | | | (_| |
 |_|\_\ \_/\_/ |_|   /_/\_\_| |_|\__, |
                                 |___/ 
Created on Sat Jun  9 10:03:07 2018
@author: KwFung
"""

from connection import Connection
import oandapyV20.endpoints.accounts as accounts

def getSummary():    
    # Request
    connection = Connection()
    accountID = connection.config['ACCOUNT_ID']
    r = accounts.AccountSummary(accountID)
    return connection.API.request(r)