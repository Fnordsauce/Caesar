import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from currentPeriod_Activity import statementReader
import time
import tkinter as tk
from currentPeriod_Activity import statementReader
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

def chartData():
    root = tk.Tk()
    greeting = tk.Label(text="QQQ Porfolio Summary")
    greeting.pack()
    root.geometry("450x650")

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
        value = value / 1.35
        points.append(value)
        dates.append(x[-1])
    #Grab the dates from the intial plot
    # the figure that will contain the plot
    figure2 = plt.Figure(figsize=(13, 4), dpi=100)
    ax2 = figure2.add_subplot(111)
    line2 = FigureCanvasTkAgg(figure2, root)
    line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    QQQ.plot(kind='line', legend=True, ax=ax2, color='r', fontsize=10)
    
    ax2.set_title('YQQQ Porfolio Summary')

    root.mainloop()

    return
    #Date and PurchasePrice

chartData()
