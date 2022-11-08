import pandas as pd
import tabula
from tabula import read_pdf
dfs = tabula.read_pdf("WS_Tracker\Performance_Statements\OCT22.PDF",stream=True, multiple_tables=True, pages="3", encoding="utf-8")


count = 0
for df in dfs:
    if count == 0:
        data = df
    count+=1
data.columns = data.iloc[0]
data = data.reindex(data.index.drop(0)).reset_index(drop=True)
data.columns.name = None
print(data)