# GBPJPY_Moving_Average_Backtester ***(WORK IN PROGRESS)***

Moving average strategy used on the currency pair GBP/JPY.

# Logic

This Python script downloads the 1 day time series data for the currency pair GBP/JPY from Yahoo Finance, creates 20 day and 50 day moving averages, presents this data on a graph and iterates over the data via a for loop.

When price is above both moving averages and the 20 day moving average moves above the 50 day moving average, it will print the date this occurs and a "buy" signal.

When price is below both moving averages and the 20 day moving average moves below the 50 day moving average, it will print the date this occurs and a "sell" signal.

# Libraries used
**yfinance:**

- collects time series ticker data history from Yahoo Finance as a pandas DataFrame.

**Matplotlib:**

- plots the data for visualisation purposes.


**pandas:**

- exports yfinance data to .csv.


- manipulates the data to create moving averages.


- allows us to iterate over the time series data via a for loop.
