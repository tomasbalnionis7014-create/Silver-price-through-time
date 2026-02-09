# main.py
import pandas as pd
from data_loader import load_data
from analysis import mean_price, Moving_Average, daily_percentage_change
from plotter import plot_silver_price

# pandas display settings
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)

# load CSV
df = load_data(
    "C:/Users/tomas/silver-price-through-time/Silver Futures Historical Data.csv")

while True:
    options = [
        "1. Mean Price",
        "2. Moving Average",
        "3. Daily Percentage Change",
        "4. See The Plot",
        "5. Exit"
    ]
    print("\nPlease select an option:")
    for option in options:
        print(option)
    choice = input("Enter the number of your choice: ").strip()

    if choice == "1":
        print("\nMean Price:", mean_price(df))

    elif choice == "2":
        df_ma = Moving_Average(df.copy(), windows=[7, 14])
        df_to_show = df_ma[['Date', 'Price',
                            'Moving Average (7)', 'Moving Average (14)']]
        print("\n", df_to_show.head(10).to_string(
            index=False))  # <- clean output

    elif choice == "3":
        df_dpc = daily_percentage_change(df.copy())
        df_to_show = df_dpc[['Date', 'Price', 'Daily Percentage Change']]
        print("\n", df_to_show.head(10).to_string(
            index=False))  # <- clean output

    elif choice == "4":
        df_plot = Moving_Average(df.copy(), windows=[7, 14])
        plot_silver_price(df_plot)

    elif choice == "5":
        print("\nExiting the program.")
        break

    else:
        print("\nInvalid choice. Please try again.")
