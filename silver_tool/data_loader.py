def load_data(file_path):
    import pandas as pd
    df = pd.read_csv(file_path, parse_dates=['Date'])
    df.sort_values('Date', inplace=True)
    return df
