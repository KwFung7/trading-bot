#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  _  __         _____                  
 | |/ /_      _|  ___|_  ___ __   __ _ 
 | ' /\ \ /\ / / |_  \ \/ / '_ \ / _` |
 | . \ \ V  V /|  _|  >  <| | | | (_| |
 |_|\_\ \_/\_/ |_|   /_/\_\_| |_|\__, |
                                 |___/ 
Created on Tue May 22 23:46:41 2018
@author: KwFung
"""
import json
from connection import Connection
import oandapyV20.endpoints.orders as orders

def createOrder(units, instrument):
    # Load config
    connection = Connection()
    accountID = connection.config['ACCOUNT_ID']
    
    # Load json
    with open('orderbody.json', 'r') as f:
        data = json.load(f)
        
    # set units and instrument
    data['order']['units'] = units
    data['order']['instrument'] = instrument
    print('Create Order Request: {}\n'.format(data))
    
    # Request
    r = orders.OrderCreate(accountID, data)
    return connection.API.request(r)
