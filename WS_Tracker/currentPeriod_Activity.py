import pandas as pd
import tabula
from tabula import read_pdf
import tabula
from tabulate import tabulate
import os
import PyPDF2
def statementReader():
    targetReturn = []
    for filename in os.listdir("Caesar_Project\Caesar\WS_Tracker\Performance_Statements"):
        f = os.path.join("Caesar_Project\Caesar\WS_Tracker\Performance_Statements", filename)
        # checking if it is a file
        if os.path.isfile(f):
            PATH = f
        reader = PyPDF2.PdfFileReader(PATH)
        search_term = 'Activity - Current period'
        for page_number in range(0, reader.numPages):
            page = reader.getPage(page_number)
            page_content = page.extractText()   
            if search_term in page_content:
                page = page_number + 1
                break

            
        dfs = tabula.read_pdf(PATH,
        stream=True,
        multiple_tables=True,
        pages=page,
        encoding="utf-8")

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
        targetAmountDates = []
        temp = ""
        for sen in targetArr:
            sen = sen.split()
            for index, word in enumerate(sen):
                temp = sen[0]
                if word == 'Bought':
                    targetAmount.append(sen[index+1])
                    targetAmountDates.append(temp)
                temp = " "
        #print(targetNum)
        
        appendList = []
        for (b, c, d) in zip(targetAmount, targetPrice, targetAmountDates):
            appendList.append(key)
            appendList.append(b)
            appendList.append(c)
            appendList.append(d)
            targetReturn.append(appendList)
            appendList = []
        
    
    return targetReturn 


factory = statementReader()
