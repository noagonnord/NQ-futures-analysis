import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from pathlib import Path
ticker = 'NQ=F'
period = '2y'

data = yf.Ticker(ticker).history(period=period)
if data.empty:
    raise SystemExit("Oops programm failed, try again in a few minutes")

data = data[["Open","High","Low","Close","Volume"]]

print(data.head())
print()
print(f"Number of day in cotaion {len(data)}")
print(f"Periode: from, {data.index[0].date()}, to {data.index[-1].date()}")

price = data["Close"]
data["Return"] = price.pct_change()
daily_volatility = data["Return"].std()
annual_volatility = daily_volatility * 252**0.5

mean_return = data["Return"].mean()
print(data[["Close","Return"]].head())
print(f"Mean daily return: {mean_return:.3%}")
print(f"Daily volatility:  {daily_volatility:.2%}")
print(f"Annual volatility: {annual_volatility:.2%}")

data["MA20"] = price.rolling(window=20).mean()
data["MA50"] = price.rolling(window=50).mean()

print()
print(data[["Close", "MA20", "MA50"]].tail())

last_ma20 = data["MA20"].iloc[-1]
last_ma50 = data["MA50"].iloc[-1]

print()
if last_ma20 > last_ma50:
    print("The 20 day MA is above the 50 day MA: recent prices are higher than the long term average.")
else:
    print("The 20 day MA is below the 50 day MA: recent prices are lower than the long term average.")

plt.figure(figsize=(12, 6))

plt.plot(data.index, data["Close"], label="Close price", color="#686553", linewidth=1.2)
plt.plot(data.index, data["MA20"], label="20-day moving average", color="#2c9200", linewidth=2)
plt.plot(data.index, data["MA50"], label="50-day moving average", color="#b134eb", linewidth=2)

plt.title(f"E-mini Nasdaq-100 futures ({ticker}): price and moving averages\n"
          f"Annualized volatility: {annual_volatility:.1%}")
plt.xlabel("Date")
plt.ylabel("Price (index points)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

chart_path = Path(__file__).parent / "nq_chart.png"
plt.savefig(chart_path, dpi=150)
plt.show()