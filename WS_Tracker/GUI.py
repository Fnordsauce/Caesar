import tkinter as tk
from currentPeriod_Activity import statementReader
window = tk.Tk()

greeting = tk.Label(text="QQQ Porfolio Summary")
greeting.pack()
window.geometry("450x650")


PricingData = statementReader()

packedData = tk.Label(PricingData)
packedData.pack()









window.mainloop()
