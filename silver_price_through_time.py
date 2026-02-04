import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Silver Futures Historical Data.csv', parse_dates=['Date'])
df.sort_values('Date', inplace=True)
print(df.head())
print(df.info())
# Calculate 7-day and 14-day moving average
df['Moving Average (7)'] = df['Price'].rolling(window=7).mean()
df['Moving Average (14)'] = df['Price'].rolling(window=14).mean()
# plotting
plt.plot(df['Date'], df['Price'], label='Price')
plt.plot(df['Date'], df['Moving Average (7)'],
         label='7-Day Moving Average', color='orange')
plt.plot(df['Date'], df['Moving Average (14)'],
         label='14-Day Moving Average', color='green')

plt.xlabel('Date')
plt.ylabel('Price of Silver (USD)')
plt.title('Silver Price Through Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('silver_price_through_time.png', dpi=200)
plt.show()


# learning points to take away here:
# 1. How to read a CSV file using pandas and parse dates.
# 2. How to sort a DataFrame by a specific column.
# 3. How to calculate a moving average using the rolling() function in pandas.
# the general structure of the code is:
# data in
# columns created
# plots stacked
# then last port od call was to plt.show() to display the plot.
# if the plot is not showing then its likely that plt.show() is in the wrong place/ missing
