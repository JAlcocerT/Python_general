#Quandl has many data sources to get different types of data.
# However, some are free and some are paid. Wiki is the free data source of Quandl
# to get the data of the end of the day prices of 3000+ US equities.

#The quandl get method takes this stock market data as input and returns
# the open, high, low, close, volume, adjusted values and other information.

#Only available till 27-March-2018

# Import the quandl
import quandl

# To get your API key, sign up for a free Quandl account.
# Then, you can find your API key on Quandl account settings page.
QUANDL_API_KEY = 'pt6RoDdsiYV5bZjh8skX'

# This is to prompt you to change the Quandl Key
if QUANDL_API_KEY == 'REPLACE-THIS-TEXT-WITH-A-REAL-API-KEY':
 raise Exception("Please provide a valid Quandl API key!")

# Set the start and end date
start_date = '1970-01-01'
end_date = '2015-03-01'
# Set the ticker name
ticker = 'PG'
# Feth the data
data = quandl.get('WIKI/'+ticker, start_date=start_date,
 end_date=end_date, api_key=QUANDL_API_KEY)

# Print the first 5 rows of the dataframe
data.head()

import matplotlib.pyplot as plt

# Define the figure size for the plot
plt.figure(figsize=(10, 7))
# Plot the adjusted close price
data['Adj. Close'].plot()
# Define the label for the title of the figure
plt.title("Adjusted Close Price of %s" % ticker, fontsize=16)
# Define the labels for x-axis and y-axis
plt.ylabel('Price', fontsize=14)
plt.xlabel('Year', fontsize=14)
# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()