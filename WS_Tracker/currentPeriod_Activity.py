import pandas as pd
import tabula
from tabula import read_pdf
import tabula
from tabulate import tabulate

def statementReader():
    dfs = tabula.read_pdf("Caesar_Project\Caesar\WS_Tracker\Performance_Statements\OCT22.pdf",stream=True, multiple_tables=True, pages="3", encoding="utf-8")


    count = 0
    for df in dfs:
        if count == 0:
            data = df
        count+=1
    data.columns = data.iloc[0]
    data = data.reindex(data.index.drop(0)).reset_index(drop=True)
    data.columns.name = None
    #print(data)
    key = "QQQ"
    targetArr = []
    targetPrice = []
    for index, row in data.iterrows():
    #print(row["Date Transaction Description"])
        if key in row["Date Transaction Description"]:
            targetArr.append(row["Date Transaction Description"])
            targetPrice.append(row["Charged ($)"])

    #print(targetArr)
    targetAmount = []
    for sen in targetArr:
        sen = sen.split()
        for index, word in enumerate(sen):
            if word == 'Bought':
                targetAmount.append(sen[index+1])
    #print(targetNum)
    targetReturn = []
    appendList = []
    print(targetAmount, targetPrice)
    for (b, c) in zip(targetAmount, targetPrice):
        appendList.append(key)
        appendList.append(b)
        appendList.append(c)
        targetReturn.append(appendList)
        appendList = []

    return targetReturn 


factory = statementReader()
print(factory)
