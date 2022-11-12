import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from currentPeriod_Activity import statementReader
import time
import tkinter as tk
from tkinter import *
from currentPeriod_Activity import statementReader
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

def chartData():
    root = tk.Tk()
    greeting = tk.Label(text="QQQ Porfolio Summary")
    greeting.grid(row = 0, column = 0,)
    root.geometry("1500x500")

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
    line2.get_tk_widget().grid(row = 1, column = 0,)
    xLine = QQQ.plot(kind='line', legend=True, ax=ax2, color='r', fontsize=10)
    ax2.scatter(dates, points)
    #ax2.line()
    #going to use the points array 
    PointAVE = sum(points) / len(points)
    #Grabbing Dates Column
    ax2.axhline(y = PointAVE, color = 'g', linestyle = '--')
    
    #ax2.line[]
    ax2.set_title('QQQ Porfolio Summary')

    #XXX---------------------------------------- OVERVIEW TAB -------------------------------------XXX

    overViewFrame = Frame(root, width=500)
    overViewFrame.grid(row = 1, column = 1,)
    titleLabel = Label(overViewFrame, text="Overview of Account")
    titleLabel.pack()



    root.mainloop()

    return
    #Date and PurchasePrice

chartData()
