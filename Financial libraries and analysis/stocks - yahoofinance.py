import yfinance as yf
import matplotlib.pyplot as plt

intraday_data = yf.download(tickers="MSFT",
 period="5d",
 interval="1m",auto_adjust=True)

# The valid frequencies are 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
#The frequency of data. The valid intervals are 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
#The name of the tickers you want the data for. If you want data for multiple tickers then separate them by space
intraday_data.head()

#fundamental data

# Set the ticker as MSFT
msft = yf.Ticker("MSFT")
#You can fetch the latest price to book ratio and price to earnings ratio as shown below.
# get price to book
pb = msft.info['priceToBook']
#pe = msft.info['regularMarketPrice']/msft.info['epsTrailingTwelveMonths']
print('Price to Book Ratio is: %.2f' % pb)
#print('Price to Earnings Ratio is: %.2f' % pe)

# show revenues
revenue = msft.financials.loc['Total Revenue']
plt.bar(revenue.index, revenue.values)
plt.ylabel("Total Revenues")
plt.show()


# show income statement
print(msft.financials)
# show balance heet
msft.balance_sheet
# show cashflow
msft.cashflow
# show other info
print(msft.info)

