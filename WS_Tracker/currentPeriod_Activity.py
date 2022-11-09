import pandas as pd
from tabula import read_pdf
import tabula
from tabulate import tabulate


dfs = tabula.read_pdf("WS_Tracker\Performance_Statements\OCT22.pdf",pages="3", stream=True)

print(f"Found {len(dfs)} tables")
#dataFrame = pd.DataFrame(dfs)
# display each of the dataframes
counter= 0 
for df in dfs:
    if counter == 0:
        data = df
    counter+=1


#data.rename(columns=data.iloc[0]).drop(data.index[0])
#print(data)

data.columns = data.iloc[0]
data = data.reindex(data.index.drop(0)).reset_index(drop=True)
data.columns.name = None
print(data)
print(data["Balance ($)"].mean(numeric_only=True))