# main.py
import argparse
import pandas as pd
from .data_loader import load_data
from .analysis import mean_price, Moving_Average, daily_percentage_change
from .plotter import plot_silver_price
from pathlib import Path

# pandas display settings
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)

# load CSV
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / 'data' / 'silver.csv'
df = load_data(DATA_PATH)

parser = argparse.ArgumentParser(description='Silver Price Analysis Tool')

parser.add_argument("--mean", action="store_true",
                    help="Calculate and display the mean price of silver.")
parser.add_argument("--ma", nargs='+', type=int,
                    help="Calculate and display moving averages for specified windows (e.g., --ma 7 14).")
columns_to_show = ['Date', 'Price']
parser.add_argument("--dpc", action="store_true",
                    help="Calculate and display daily percentage change.")
args = parser.parse_args()


if args.mean:
    print("\nMean Price:", mean_price(df))
if args.ma:
    df_ma = Moving_Average(df.copy(), windows=args.ma)

    columns_to_show = ['Date', 'Price']
    for window in args.ma or []:
        columns_to_show.append(f'Moving Average ({window})')
    df_to_show = df_ma[columns_to_show]
    print("the moving averages for the specified window are:")
    print("\n", df_to_show.head(10).to_string(index=False))

if args.dpc:
    df_dpc = daily_percentage_change(df.copy())
    df_to_show = df_dpc[['Date', 'Price', 'Daily Percentage Change']]
    print("\n", df_to_show.head(10).to_string(index=False))


if not any(vars(args).values()):
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
