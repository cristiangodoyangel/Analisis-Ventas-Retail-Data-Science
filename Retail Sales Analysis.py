import numpy as np

def cargar_datos("https://drive.google.com/file/d/1hGkCT1u3b1FzGSSLi5bL2XAIpTy2IBK3/view?usp=drive_link"):
    # Carga los datos del archivo CSV utilizando NumPy
    datos = np.genfromtxt(ruta_archivo, delimiter=',', skip_header=1)
    return datos

if __name__ == "__main__":
    ruta_archivo = '../data/retail_sales.csv'
    datos = cargar_datos(ruta_archivo)
    print(datos)