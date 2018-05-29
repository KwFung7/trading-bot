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

def loadConfig():
    # Load config
    config = configparser.ConfigParser()
    config.read('config.ini')
    mode = config['ENV']['MODE']
    return config[mode]

def init():
    config = loadConfig()
    environment = config['TYPE']
    access_token = config['AUTH_TOKEN']
    return API(access_token, environment)
