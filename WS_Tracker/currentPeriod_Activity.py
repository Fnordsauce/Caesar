import pandas as pd
from tabula import read_pdf
dfs = tabula.read_pdf("Personal_Project\WS_Tracker\Performance_Statements\OCT22.pdf", multiple_tables=True, pages="all", encoding="utf-8")

