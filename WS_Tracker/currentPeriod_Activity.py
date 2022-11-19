import pandas as pd
import tabula
from tabula import read_pdf
import tabula
from tabulate import tabulate
import os
import PyPDF2
def statementReader(sec_names):
    

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
        sec_data = []
        for sec in sec_names:
            key = sec
            targetArr = []
            targetPrice = []
            tempo = ""
            tempo1 = ""
            for index, row in data.iterrows():
                #print(index, row)
                if next(df.iterrows())[1] is not None:
                    row1 = next(df.iterrows())
                if key in row["Date Transaction Description"]:
                    tempo = row["Date Transaction Description"] 
                    tempo1 = tempo + row1["Date Transaction Description"]
                    targetArr.append(tempo)
                    targetPrice.append(row["Charged ($)"])
                        
                    
            print()
            #print(key, targetArr)
            print(key, targetArr, targetPrice)
            targetAmount = []
            targetAmountDates = []
            temp = ""
            print("TARGET",targetArr)
            for sen in targetArr:
                sen = sen.split()
                for index, word in enumerate(sen):
                    temp = sen[0]
                    #print(key, temp, word)
                    if word == 'Bought':
                        targetAmount.append(sen[index+1])
                        targetAmountDates.append(temp)
                    temp = " "
            #print(targetNum)
            print(key, targetAmount, targetPrice, targetAmountDates)
            appendList = []
            
            for (b, c, d) in zip(targetAmount, targetPrice, targetAmountDates):
                if not targetAmount and targetPrice:
                    continue
                print(key, targetAmount, targetPrice, targetAmountDates)
                appendList.append(key)
                appendList.append(b)
                appendList.append(c)
                appendList.append(d)
                sec_data.append(appendList)
                appendList = []
            
    print(sec_data)
    return targetReturn 

securties = ["QQQ","VOOG"]
factory = statementReader(securties)
