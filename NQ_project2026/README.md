**NQ E-MINI Futures analysis**

A short Python project that downloads two years of E-mini Nasdaq data and calculates basic risk and trend indicators.

What the script does:

1) Downloads the data: The script downloads two years of daily prices (Open, High, Low, Close, Volume) for NQ=F, the Yahoo finance ticker for the e-mini futures contract, using finance.  
2) Calculates daily return: the percentage change of the closing price from one day to the next  
3) Measures volatility: the daily returns annualized with the square root of time  
4) Calculates moving averages: 20 days and 50 days of moving averages  of the closing price.  
5) Visualize results: the closing price and both moving averages on one chart.

Key concepts:  
Daily return:  
   
Return \= Pt+1 \- Pt / Pt where Pt is the closing price of day t

Annualized volatility 

annual volatility \= daily volatility x square root of 252

Moving averages (20 and 50 days)

The average of the last N closing prices, recalculated every day. It shows the trend line . 

How to run it ?

The script requires Python 3

Type in :   
python3 \-m pip install \-r requirements.txt   
python3 nq\_analysis.py

The script will print the first rows of data, the average daily return, the daily and annualized volatility, and the latest moving average values. It then saves and opens the chart.

Limitations

Continuous futures series: `NQ=F` follows the nearest contract and switches to the next one at each quarterly expiry (March, June, September, December). These rolls can create small artificial jumps in the price series and in the returns on those days.

Independence assumption: the square root of 252 rule assumes that daily returns are independent. In real markets, volatility tends to switch from calm periods to high volatility periods so the annualized figure is an approximation.

Moving averages: they are built from past prices, so they confirm a trend after it has started. They do not predict future prices.

Requirements: 

finance ; pandas ; matplotlib

