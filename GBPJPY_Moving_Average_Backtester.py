import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


gbpjpy = yf.Ticker("GBPJPY=X") 

# download daily data from start to today
gbpjpy_data = gbpjpy.history(period="max", interval="1d")

# save to CSV
gbpjpy_data.to_csv("GBPJPY_data.csv")

# calculate 20 day moving average using the "Close" price
gbpjpy_data["MA20"] = gbpjpy_data["Close"].rolling(window=20).mean()

# calculate 50 day moving average using the "Close" price
gbpjpy_data["MA50"] = gbpjpy_data["Close"].rolling(window=50).mean()

# calculate true range (tr) to create average true range (atr)
tr_elements = pd.concat([(gbpjpy_data["High"] - gbpjpy_data["Low"]),
         (gbpjpy_data["High"] - gbpjpy_data["Close"].shift(1).abs()),
         (gbpjpy_data["Low"] - gbpjpy_data["Close"].shift(1).abs())], axis=1)

tr = tr_elements.max(axis=1)

# calculate atr
atr = tr.ewm(alpha=1/14, adjust=False).mean()

# plot two graphs in one window
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# plot close price and moving averages
gbpjpy_data[["Close", "MA20", "MA50"]].plot(ax=ax1)
ax1.set_title("GBPJPY Close Price, 20 Day & 50 Day Moving Average")
ax1.set_ylabel("Price (JPY)")

# plot atr
atr.plot(color="red", ax=ax2)
ax2.set_title("Average True Range, 14 Day Period")
ax2.set_xlabel("Date")

# present plotted data
plt.show()



# changes to "buy" or "sell". Used so signals are only printed when the cross overs occur
last_signal = None  

# to store buy and sell data from for loop
buy_dict = {}
sell_dict = {}

#for loop to iterate over close data to determine a buy or sell singal
for index, row in gbpjpy_data.iterrows():
    buy_signal = row["Close"] > row["MA20"] and row["MA20"] > row["MA50"]
    sell_signal = row["Close"] < row["MA20"] and row["MA20"] < row["MA50"]


    if buy_signal and last_signal != "buy":
        #update below code to include what's in the to do list below
        buy_signal_timestamp = index
        price_buy = row["Close"]  #price as which signal is given
        buy = "buy"
        print(buy_signal_timestamp, (price_buy, buy))
        last_signal = "buy"
        buy_dict[index]= buy

        
    elif sell_signal and last_signal != "sell":
        #update below code to include what's in the to do list below
        sell_signal_timestamp = index
        price_sell = row["Close"] #price as which signal is given
        sell = "sell"
        print(sell_signal_timestamp, [price_sell, sell])
        last_signal = "sell"
        sell_dict[index]= sell


#to do:
"""***CURRENTLY MISSING ACCOUNT METRICS AND RISK MANAGEMENT RULES***:
     - set take profit to 2:1
     - if risk is more than 1.5% of account balance do not take trade
     - if value of account is less than a certain amount don"t take a trade
     - if take profit is hit, close 50% of the position and move stop loss to breakeven
     - if stop loss is hit, close the position

Output metric:
- PnL
- Win rate
- Max Drawdown
- Sharpe Ratio
"""