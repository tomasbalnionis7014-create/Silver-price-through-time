# Silver Price Through Time

## Project overview
A Python CLI tool to analyze historical silver prices.
Features include calculating moving averages, daily percent changes, and basic statistics (mean, median, etc.).
Designed for quick analysis without manually opening spreadsheets.
## features
- CLI interface with interactive menu
- command- line for quick operations
- --ma (days) = calculates movving average over (days)
- --mean calculates mean silver price
- --dpc is the daily percent change
- ## installation
- git clone https://github.com/<your-username>/silver-price-through-time.git
- cd silver-price-through-time
- python -m venv venv
- source venv/Scripts/activate   # Windows
- pip install -r requirements.txt  # if you have any dependencies like pandas, matplotlib
## usage
-interactive menu u run: python -m silver_tool.main
-and for cli flags mode:
-python -m silver_tool.main --mean
-python -m silver_tool.main --ma 30
-python -m silver_tool.main --dpc

- ## files
-  `silver_price_through_time.py` — main script
- `Silver Futures Historical Data.csv` — data
- `silver_price_through_time.png` — plot
