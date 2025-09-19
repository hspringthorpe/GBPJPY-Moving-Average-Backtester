# GBPJPY-Moving-Average-Backtester ***(WORK IN PROGRESS)***

Backtest of a moving average strategy used on the currency pair GBP/JPY.

My aim is to create a moving average backtester by running through a set of data and using performance metrics to determine the success of the strategy.

# Current Logic

This Python script downloads the 1 day time series data for the currency pair GBP/JPY from Yahoo Finance, creates 20 day, 50 day moving averages and an average true range. Two graphs are then presented in one window, one showing the price of GBP/JPY along with the moving averages while the other shows the average true range. A for loop then iterates over the time series data to print buy and sell signals.

When price is above both moving averages and the 20 day moving average moves above the 50 day moving average, it will print the date, the price this occurs and a "buy" signal.

When price is below both moving averages and the 20 day moving average moves below the 50 day moving average, it will print the date, the price this occurs and a "sell" signal.

# Libraries used
**yfinance:**

- Collects time series ticker data history from Yahoo Finance as a pandas DataFrame.

**Matplotlib:**

- Plots the data for visualisation purposes.


**pandas:**

- Exports yfinance data to .csv.


- Manipulates the data to create moving averages.


- Allows iteration over the time series data via a for loop.


**NumPy:**

- Will be used on the iterated data to highlight the performance of strategy.
