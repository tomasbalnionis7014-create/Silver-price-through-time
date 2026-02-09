
def mean_price(df):
    return df['Price'].mean()


def Moving_Average(df, windows=[7, 14]):
    for window in windows:
        df[f'Moving Average ({window})'] = df['Price'].rolling(
            window=window).mean()
    return df


def daily_percentage_change(df):
    df['Daily Percentage Change'] = df['Price'].pct_change() * 100
    return df
