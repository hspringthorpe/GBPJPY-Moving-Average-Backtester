import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

gbpjpy = yf.Ticker("GBPJPY=X") 

# download daily data from start to today [update the end date to the current date]
gbpjpy_close_data = gbpjpy.history(period="max", interval="1d")

# save to CSV for your repo
gbpjpy_close_data['Close'].to_csv("GBPJPY_close.csv") # <------- CHANGE THIS TO gbpjpy_data.to_csv("gbpjpy_data.csv") to import OHLC data

# calculate 20 day moving average using the 'Close' price
gbpjpy_close_data['MA20'] = gbpjpy_close_data['Close'].rolling(window=20).mean()

# calculate 50 day moving average using the 'Close' price
gbpjpy_close_data['MA50'] = gbpjpy_close_data['Close'].rolling(window=50).mean()


# plot the data
gbpjpy_close_data[['Close', 'MA20', 'MA50']].plot(figsize=(12, 6))
plt.title("GBPJPY Close Price, 20 Day & 50 Day Moving Average")  
plt.ylabel("Price (JPY)")
plt.xlabel("Date")
# present the data
plt.show()



"""to do: implement actual buy and order decisions and not just a print"""

# changes to "buy" or "sell". Used so signals are only printed when the cross overs occur
last_signal = None  

#for loop to iterate over close data to determine a buy o rsell singal
for index, row in gbpjpy_close_data.iterrows():
    buy = row['Close'] > row['MA20'] and row['MA20'] > row['MA50']
    sell = row['Close'] < row['MA20'] and row['MA20'] < row['MA50']
    
    if buy and last_signal != "buy":
        print(index, "buy")
        last_signal = "buy"
    elif sell and last_signal != "sell":
        print(index, "sell")
        last_signal = "sell"


"""***CURRENTLY MISSING RISK MANAGEMENT RULES WHICH ARE***:
     - set take profit to 2:1
     - if risk is more than 1.5% of account balance do not take trade
     - if value of account is less than a certain amount don't take a trade
     - if take profit is hit, close 50% of the position and move stop loss to breakeven
     - if stop loss is hit, close the position

Output metric:
- PnL
- Win rate
- Max Drawdown
- Sharpe Ratio
"""