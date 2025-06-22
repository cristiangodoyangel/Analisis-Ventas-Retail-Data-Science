# 🛍️ Análisis de Ventas Minoristas con Python y Pandas

Este proyecto forma parte de mi formación en ciencia de datos. El objetivo es aplicar técnicas de análisis exploratorio, transformación de datos, agregación y funciones personalizadas usando Python y la librería Pandas sobre un dataset de ventas retail.

---

## 📁 Dataset

El dataset utilizado contiene información sobre ventas minoristas, con variables como:

- `Product Category` (categoría del producto)
- `Gender` (género del cliente)
- `Total Amount` (monto total de la venta)
- Entre otras columnas relevantes

---

## 🧾 Objetivos del Proyecto

- Realizar una **exploración inicial** del dataset
- Aplicar **limpieza y transformación de datos**
- Generar **agrupaciones y estadísticas descriptivas**
- Implementar **funciones personalizadas con `apply()`**
- Clasificar ventas y normalizar columnas para análisis comparativo

---

## 🔎 Exploración de Datos

- Se visualizan las primeras y últimas filas del dataset.
- Se examinan los tipos de datos, valores únicos y estadísticas generales.
- Se realizan filtros por condiciones específicas (e.g. ventas mayores a 150).

---

## 🧹 Transformación de Datos

- Se normaliza la columna `Total Amount` a un rango de 0 a 1.
- Se crea una nueva columna `Nivel_Venta` que clasifica cada venta como:
  - `Alta` (≥ 200)
  - `Media` (100–199)
  - `Baja` (< 100)

```python
def clasificar_venta(valor):
    if valor >= 200:
        return 'Alta'
    elif valor >= 100:
        return 'Media'
    else:
        return 'Baja'
