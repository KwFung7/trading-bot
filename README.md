#### Intro
Using Oanda API for forex currency data and order creation.
Data fetched from API used for machine learning model training (SVR).

![alt text](https://s3-ap-southeast-1.amazonaws.com/kwfxng-portfolio-image/tradingbot-code-1.png "Demo Image 1")

![image](https://s3-ap-southeast-1.amazonaws.com/kwfxng-portfolio-image/tradingbot-code-2.gif)

#### Direct run
> /usr/bin/python3.6 ./tradingbot.py

#### Cron Job
Suppose to run with cron job every hour:
`0 * * * 1-5 cd /opt/trading-bot && /usr/bin/python3.6 ./tradingbot.py >> output.log 2>&1`

#### Library install
`sudo pip3 install xxxx`

#### Config format
```
[ENV]
MODE=TEST

[TEST]
# Account
TYPE=practice
ACCOUNT_ID=xxx-xxx-xxxxxxx-xxx
AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Order
INSTRUMENTS=USD_HKD,EUR_HKD,GBP_HKD,CHF_HKD
DAY_RANGE=100,500
SELECTED_RANGE=100
LIMIT_UNIT=10000
ORDER_UNIT=500
MIN_PROFIT=0.03
DAY_FOR_MEAN=5
LIMIT_MARGIN=1000
CUT_LOSS_PERCENT=0.97

# Model
GRANULARITY=D
TREE_NUMBER=500
SVR_KERNEL=rbf
```

#### Config usage
- Account
    - TYPE: can be 'practice' or 'live'
    - ACCOUNT_ID: Oanda account id with 16 digit
    - AUTH_TOKEN: token for authentication, get it from Oanda

- Order
    - INSTRUMENTS: type of currency for trading, separated with comma e.g. USD_HKD,EUR_HKD
    - DAY_RANGE: day range for data used in regression, can be multiple e.g. 100,500 
    - SELECTED_RANGE: selected day range for data used in actual prediction
    - LIMIT_UNIT: limit maximum order unit for single currency
    - ORDER_UNIT: set order unit for single trade and single currency
    - MIN_PROFIT: allow selling only when minimum profit meet
    - DAY_FOR_MEAN: number of day for calculating mean value, which affect the buy decision
    - LIMIT_MARGIN: bot can stop the trade when the available margin less than this value
    - CUT_LOSS_PERCENT: bot can stop the loss when bid price lower than current percentage
    
- Model
    - GRANULARITY: check https://developer.oanda.com/, it mean 1 day candlestick for 'D'
    - TREE_NUMBER: for random forest used (DEPRECATED)
    - SVR_KERNEL: for support vector regression kernel    
