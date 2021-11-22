

# Yahoo recently has become an unstable data source.
# If it gives an error, you may run the cell again, or try yfinance
import pandas as pd

#If the stock market data fetching fails from yahoo finance using
# the pandas_datareader then you can use yfinance package to fetch the data.


from pandas_datareader import data
# Set the start and end date
start_date = '1990-01-01'
end_date = '2021-05-01'
# Set the ticker
ticker = 'AMZN'
# Define the ticker list
tickers_list = ['AAPL', 'IBM', 'MSFT', 'WMT']

# Get the data

# Feth the data
for ticker in tickers_list:
 data[ticker] = data.get_data_yahoo(ticker, start_date, end_date)
# Print first 5 rows of the data
data.head()


import matplotlib.pyplot as plt
#%matplotlib inline
data['Adj Close'].plot()
plt.show()


# Plot the adjusted close price
data['Adj Close'].plot(figsize=(10, 7))
# Define the label for the title of the figure
plt.title("Adjusted Close Price of %s" % ticker, fontsize=16)
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
# Show the plot
plt.show()