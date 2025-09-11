# GBPJPY_Moving_Average_Backtester ***(WORK IN PROGRESS)***

Backtest of a moving average strategy used on the currency pair GBP/JPY.

My aim is to create a moving average backtester by running through a set of data and using performance metrics to deteremine the success of the strategy.

# Current Logic

This Python script downloads the 1 day time series data for the currency pair GBP/JPY from Yahoo Finance, creates 20 day and 50 day moving averages, presents this data on a graph and iterates over the data via a for loop.

When price is above both moving averages and the 20 day moving average moves above the 50 day moving average, it will print the date this occurs and a "buy" signal.

When price is below both moving averages and the 20 day moving average moves below the 50 day moving average, it will print the date this occurs and a "sell" signal.

# Libraries used
**yfinance:**

- Collects time series ticker data history from Yahoo Finance as a pandas DataFrame.

**Matplotlib:**

- Plots the data for visualisation purposes.


**pandas:**

- Exports yfinance data to .csv.


- Manipulates the data to create moving averages.


- Allows to iterate over the time series data via a for loop.


**NumPy:**

- Will be used on the data from pandas to highlight performance of stratgey.
