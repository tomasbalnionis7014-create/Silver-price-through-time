import matplotlib.pyplot as plt

from analysis import Moving_Average


def plot_silver_price(df):
    if 'Moving Average (7)' not in df.columns or 'Moving Average (14)' not in df.columns:
        df = Moving_Average(df, windows=[7, 14])
    plt.plot(df['Date'], df['Price'], label='Price')
    plt.plot(df['Date'], df['Moving Average (7)'],
             label='7-Day Moving Average', color='orange')
    plt.plot(df['Date'], df['Moving Average (14)'],
             label='14-Day Moving Average', color='green')

    plt.xlabel('Date')
    plt.ylabel('Price of Silver (USD)')
    plt.title('Silver Price Through Time with Moving Averages')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
