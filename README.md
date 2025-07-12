# 🛍️ Análisis de Ventas Minoristas con Python y Pandas


# 🛒 Retail Sales Analysis - Data Science Project

> Exploración, visualización y análisis avanzado de datos de ventas retail con Python.  
> Proyecto realizado como parte de la formación en ciencia de datos.

---

## 📊 Descripción del Proyecto

Este proyecto tiene como objetivo analizar un conjunto de datos de ventas minoristas utilizando técnicas de análisis exploratorio de datos (EDA), visualización avanzada y categorización. El análisis busca responder preguntas clave sobre comportamiento de compras, categorías más vendidas, variaciones por género, tendencias en el tiempo, y más.

---

## 📁 Dataset

- **Archivo:** `retail_sales_dataset.csv`  
- **Origen:** Almacenado en Google Drive o localmente.  
- **Columnas principales:**
  - `Date` – Fecha de la transacción
  - `Product Category` – Categoría del producto
  - `Gender` – Género del comprador
  - `Quantity` – Cantidad comprada
  - `Price per Unit` – Precio unitario
  - `Total Amount` – Precio total de la venta

---

## 🔍 Análisis Realizado

### ✅ Parte I: Carga y Exploración Inicial
- Carga del CSV usando `pandas`
- Verificación de las primeras y últimas filas
- Tipos de datos y valores únicos por columna
- Estadísticas descriptivas generales

### ✅ Parte II: Filtrados y Consultas
- Ventas mayores a $150 y menores a $100
- Filtrado por categoría (`Electronics`) y total vendido
- Ventas por género y producto

### ✅ Parte III: Transformaciones
- Normalización de `Total Amount`
- Clasificación de ventas en niveles: `Baja`, `Media`, `Alta`
- Cálculo de desviación respecto a la media por categoría

### ✅ Parte IV: Visualización Avanzada
- Histogramas, boxplots y scatter plots
- Series temporales de ventas
- Comparaciones por género y categoría
- Subplots personalizados con `matplotlib`
- Heatmap de correlación entre variables numéricas

---

## 📈 Visualizaciones Destacadas

| Gráfico                          | Descripción                              |
|----------------------------------|------------------------------------------|
| 📊 Histograma                    | Distribución de montos de venta          |
| 📦 Boxplot por Producto          | Identificación de outliers por categoría |
| 📆 Línea Temporal                | Tendencia de ventas en el tiempo         |
| 🔥 Heatmap de Correlación        | Relación entre variables numéricas       |
| 🧑‍🤝‍🧑 Scatter Género vs Monto      | Comportamiento por tipo de cliente       |

---

## 🧮 Tecnologías Utilizadas

- `Python 3.x`
- `NumPy`
- `Pandas`
- `Matplotlib`
- `Seaborn`
- `Jupyter Notebook / Google Colab`

---

## 🛠 Estructura del Código

```python
# 1. Carga y descripción
df = pd.read_csv('retail_sales_dataset.csv')

# 2. Transformaciones
df['Total_Normalized'] = ...
df['Nivel_Venta'] = ...

# 3. Agrupaciones y estadísticas
df.groupby([...])...

# 4. Visualizaciones
plt.hist(...)
sns.boxplot(...)
sns.heatmap(...)
```

## 🧠 Modelos Utilizados
Regresión Logística

K-Nearest Neighbors (KNN)

Árbol de Decisión

Random Forest ✅

XGBoost

LightGBM

El modelo final seleccionado fue Random Forest, logrando una precisión del 100% sobre el conjunto de prueba (verificada sin data leakage).

## 👥 Autor
Cristian Andrés Godoy Angel
El Pastor

🪪 Licencia
Este proyecto se distribuye bajo la licencia MIT.
Puedes utilizarlo libremente para fines académicos, comerciales o personales, siempre y cuando se mencione la autoría.
