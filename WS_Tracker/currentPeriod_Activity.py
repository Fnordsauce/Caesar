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
    print(df.size)
    print(df)
    counter+=1


print(df)