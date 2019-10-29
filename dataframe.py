import pandas as pd 
import openpyxl
data = pd.read_csv("tottus.csv")
df =data[['category', 'subcate', 'NAME', 'UNIDAD', 'PRECIO', 'PREC']]
df.to_excel('tottus2.xlsx')