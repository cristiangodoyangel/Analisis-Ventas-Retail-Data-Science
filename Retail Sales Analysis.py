
import numpy as np
import pandas as pd


# Importamos una bbdd en formato excel y lo guardamos en una variable.
path = r"C:\Users\StarMan\Desktop\DataScience\Proyecto\retail_sales_dataset.csv"
df_1 = pd.read_csv(path)

print("\n")
print("================================================ Ventas Retail =================================================")
print("\n")


print("================================== Comprobación de carga exitosa del dataset ===================================")

print(df_1.head(10))

print("\n")
print("=============================================== Ultimas 5 filas ================================================")
print(df_1.tail(5))

print("\n")
print("=============================================== Información del dataset ================================================")
print(df_1.info())

print("\n")
print("=========================================== Resumen estadístico del dataset ============================================")
print(df_1.describe().T.round(1))


