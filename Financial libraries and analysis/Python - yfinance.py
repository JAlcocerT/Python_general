# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def hello():
    """Print "Hello World" and return None."""
    print("Hello World")
    
    hello()
    
import pandas as pd
import yfinance as yf

apple= yf.Ticker("aapl")
Amazon = yf.Ticker("AMZN") 


# show actions (dividends, splits)
apple.actions

# show dividends
apple.dividends

# show splits
apple.splits

info_apple=apple.info

print(apple.info)

#All company information is contained under the info dictionary.
# Therefore, we can parse the dictionary to extract the elements that we are
# interested in:
    
   # 1) Company Sector 
print(Amazon.info['sector']) 
 #2) Price Earnings Ratio 
print(Amazon.info['trailingPE'])
 #3) Company Beta 
print(Amazon.info['beta'])

#There are so many other things available within info. We can see all
# of them by printing the keys of info:
print(Amazon.info.keys()) 
 


#Retrieving Historical Maket Prices:
    
Amazon = yf.Ticker("AMZN")
print(Amazon.history(period="max"))    
Amazon_history=Amazon.history(period="max")

#ou can also pass a lower range. The valid options are 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y and ytd.



#Alternatively, we can define our own start and end dates:

import datetime 
start = datetime.datetime(2012,5,31) 
end = datetime.datetime(2013,1,30) 
Amazon = yf.Ticker("AMZN") 
print(Amazon.history(start=start, end=end))


#In addition, we can also download historical prices for more than one stock simultaneously:
    
df = yf.download("AMZN MSFT", start="2019-01-01", end="2020-01-01",group_by="ticker") 
print(df) 
print(df.AMZN)

df.AMZN['Close'].plot(title="Amzon")


tsla_df = yf.download('TSLA', 
                      start='2019-01-01', 
                      end='2019-12-31', 
                      progress=False)
tsla_df.head()

#We can download the stock prices of multiple assets at once, by providing a list 
#(such as [‘TSLA', ‘FB', ‘MSFT']) as the tickers argument. Additionally, we can set
# auto_adjust = True , so all the presented prices are adjusted for potential 
#corporate actions, such as splits.




ticker = yf.Ticker('TSLA')
tsla_df = ticker.history(period="max")
tsla_df['Close'].plot(title="TSLA's stock price")


import yfinance as yf
ticker = yf.Ticker('AMZN')
tsla_df = ticker.history(period="max")
tsla_df['Close'].plot(title="TSLA's stock price")




