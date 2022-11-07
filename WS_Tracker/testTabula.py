import tabula
import pandas as pd

#Convert your file
df = tabula.read_pdf("Personal_Project\WS_Tracker\Performance_Statements\OCT22.pdf", pages='all')