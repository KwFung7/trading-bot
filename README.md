#### Intro
Using Oanda API for forex currency data and order creation.
Data fetched from API used for machine learning model training (SVR).

#### Direct run
> python ./tradingbot.py

#### Cron Job
Suppose to run with cron job everyday night:
`0 23 * * 1-5 /usr/bin/python tradingbot.py >> output.log 2>&1` 
