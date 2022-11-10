import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from currentPeriod_Activity import statementReader
import time
def closing_price(ticker):
    Asset = pd.DataFrame(yf.download(ticker, period="2y",interval="1wk")['Adj Close'])     
    return Asset

QQQ = closing_price("QQQ")
points = []
dates = []
PurchaseARR = statementReader()

for x in PurchaseARR:
    price = float(x[2][1:])
    amount = float(x[1][1:])
    pp = 1.00 / amount
    value = pp * price
    value = value / 1.4
    points.append(value)
    dates.append(x[-1])
#Grab the dates from the intial plot


plt.rcParams["figure.figsize"] = [15, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.plot(QQQ,color='red')
plt.scatter(dates, points)
plt.title("QQQ | Price History | Portfolio Purchase Points")
plt.xlabel("Date")
plt.ylabel("Price (USD$)")
plt.legend({'Purchase Point', '1wk Closing Price'})
plt.show()


plt.close()
#Date and PurchasePrice


