#### Intro
Using Oanda API for forex currency data and order creation.
Data fetched from API used for machine learning model training (SVR).

#### Direct run
> python ./tradingbot.py

#### Cron Job
Suppose to run with cron job every hour:
`0 * * * 1-5 cd /opt/trading-bot && /usr/bin/python3.6 ./tradingbot.py >> output.log 2>&1`

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

# Model
GRANULARITY=D
TREE_NUMBER=500
SVR_KERNEL=rbf
```
