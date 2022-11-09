import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def closing_price(ticker):
    Asset = pd.DataFrame(yf.download(ticker, period="2y",interval="1wk")['Adj Close'])     
    return Asset

QQQ = closing_price("GOGO")
print(QQQ)
plt.plot(QQQ,color='red')
plt.show()
#Date and PurchasePrice