# Import the quandl
import quandl

# To get your API key, sign up for a free Quandl account.
# Then, you can find your API key on Quandl account settings page.
QUANDL_API_KEY = 'pt6RoDdsiYV5bZjh8skX'

# Define the ticker list
import pandas as pd
tickers_list = ['AAPL', 'IBM', 'MSFT', 'WMT']

# Import pandas
data = pd.DataFrame(columns=tickers_list)

# Set the start and end date
start_date = '1980-01-01'
end_date = '2021-06-06'


# Feth the data
for ticker in tickers_list:
 data[ticker] = quandl.get('WIKI/' + ticker, start_date=start_date,
 end_date=end_date, api_key=QUANDL_API_KEY)['Adj. Close']
# Print first 5 rows of the data
data.head()


import matplotlib.pyplot as plt
# Plot all the close prices
data.plot(figsize=(10, 7))
# Show the legend
plt.legend()
# Define the label for the title of the figure
plt.title("Adjusted Close Price", fontsize=16)
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()