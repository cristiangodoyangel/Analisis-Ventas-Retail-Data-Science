
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



# Creamos una nueva columna que representa el ingreso total por cada venta
# Si ya existe 'Total Amount', asumimos que es el ingreso. Si no, sería cantidad * precio_unitario
# df_1['Total Amount'] = df_1['Quantity'] * df_1['Unit Price']

# Normalizamos la columna de Total Amount entre 0 y 1
max_val = df_1['Total Amount'].max()
min_val = df_1['Total Amount'].min()
df_1['Total_Normalized'] = df_1['Total Amount'].apply(lambda x: (x - min_val) / (max_val - min_val))

# Clasificamos las ventas según su monto en categorías: 'Baja', 'Media', 'Alta'
def clasificar_venta(valor):
    if valor >= 200:
        return 'Alta'
    elif valor >= 100:
        return 'Media'
    else:
        return 'Baja'

df_1['Nivel_Venta'] = df_1['Total Amount'].apply(clasificar_venta)

print("\n")
print("========================================== Nivel de Venta ================================================")
print(df_1.loc[:, ["Total Amount", "Nivel_Venta"]])


# Agrupamos por categoría de producto y género del cliente (como ejemplo alternativo a "tienda")
agrupado = df_1.groupby(['Product Category', 'Gender'])

# Aplicamos funciones de agregación para obtener estadísticas por grupo
resumen_agrupado = agrupado['Total Amount'].agg(['sum', 'mean', 'count', 'min', 'max', 'std', 'var'])

# Mostramos los resultados
print("\n=============== Estadísticas de ventas por Producto y Género ===============")
print(resumen_agrupado.round(2))


# Calculamos la desviación de cada venta respecto a la media de su categoría de producto
# Esto nos dice qué tan por encima o por debajo está cada venta respecto al promedio de su grupo
def desviacion_personalizada(x):
    media = x['Total Amount'].mean()
    return x['Total Amount'] - media

df_1['Desviación_vs_Media'] = df_1.groupby('Product Category', group_keys=False).apply(desviacion_personalizada)

# se cumple Core 4
# git y commit