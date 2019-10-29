import pandas as pd 
data = pd.read_csv("tottus.csv")
data[['category', 'subcate', 'NAME', 'UNIDAD', 'PRECIO', 'PREC']]