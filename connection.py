#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  _  __         _____                  
 | |/ /_      _|  ___|_  ___ __   __ _ 
 | ' /\ \ /\ / / |_  \ \/ / '_ \ / _` |
 | . \ \ V  V /|  _|  >  <| | | | (_| |
 |_|\_\ \_/\_/ |_|   /_/\_\_| |_|\__, |
                                 |___/ 
Created on Sun May 20 13:59:59 2018
@author: KwFung
"""
import configparser
from oandapyV20 import API

class Connection:
    config = {}
    API = None

    def __init__(self):
        # Load config
        config = configparser.ConfigParser()
        config.read('config.ini')
        mode = config['ENV']['MODE']
        Connection.config = config[mode]
        
        # Load API
        environment = Connection.config['TYPE']
        access_token = Connection.config['AUTH_TOKEN']
        Connection.API = API(access_token, environment)
