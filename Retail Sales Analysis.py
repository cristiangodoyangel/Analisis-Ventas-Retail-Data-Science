
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
print("=========================================== Información del dataset ============================================")
print(df_1.info())

print("\n")
print("======================================= Resumen estadístico del dataset ========================================")
print(df_1.describe().T.round(1))

print("\n")
print("========================================= Tipos de datos del dataset ===========================================")
print(df_1.dtypes)

print("\n")
print("===================================== Cantidad de productos por categoría ======================================")
print(df_1["Product Category"].value_counts())

print("\n")
print("============================================== Categorías únicas ===============================================")
# El core nos pide contar las "Tiendas" únicas, pero el dataset no tiene una columna de "Tiendas", lo hice con Product Category.
print(df_1["Product Category"].unique())


print("\n")
print("====================================== Ventas con preicio mayores a 150 =======================================")
print(df_1[df_1["Total Amount"] > 150])
# El core nos pide filtrar ventas menores a 0.5 precio unitario, pero no existen, para ser mas coherente hice el anterior.superior a 150 y este menor a 100
print("\n")
print("======================================= Ventas con precio menores a 100 =======================================")
print(df_1[df_1["Total Amount"] < 100])

#Utilizando el método query(), filtra el DataFrame para mostrar las filas donde el producto sea Electronics y las ventas sean mayores a 30.
print("\n")
print("=================================== Ventas de Electronics con precio mayor a 30 ===============================")
cond1 = df_1["Product Category"] == "Electronics"
cond2 = df_1["Total Amount"] > 30
print(df_1[cond1 & cond2])

print("\n")
print("============================================ Ventas por Producto ==============================================")
print(df_1.loc[:, ["Product Category", "Total Amount"]])

print("\n")
print("========================================== Ventas por Género (filtrado) ========================================")
# el Core pide Tienda, pero el dataset no tiene una columna de "Tiendas", lo hice con Gender.
print(df_1.loc[4:10, ["Gender", "Product Category"]])

print("\n")
print("======================= Muestra del Dataset (5 primeras filas y 3 primeras columnas) ===========================")
print(df_1.iloc[:5, :3])