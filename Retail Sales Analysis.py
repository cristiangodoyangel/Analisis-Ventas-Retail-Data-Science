
import numpy as np
import pandas as pd


# Importamos una bbdd en formato excel y lo guardamos en una variable.
path = r"C:\Users\StarMan\Desktop\DataScience\Proyecto\retail_sales_dataset.csv"
df_1 = pd.read_csv(path)

print(df_1.head())



