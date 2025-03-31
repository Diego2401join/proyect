# ejemplo_lineal.py
from datos import DatosExperimentales, datos_manuales
from regresion_Lineal import RegresionLineal
from visualizacion import VisualizacionMatplotlib

datos_experimentales = DatosExperimentales(datos_manuales)
x_i, sigma_x = datos_experimentales.obtener_columna(4), datos_experimentales.obtener_columna(5)
y_i, sigma_i = datos_experimentales.obtener_columna(0), datos_experimentales.obtener_columna(1)

modelo_lineal = RegresionLineal(x_i, y_i, sigma_i)
resultados_lineal = modelo_lineal.calcular_parametros()

# 📌 Generar animación en la regresión lineal
VisualizacionMatplotlib.graficar(
    x_i, y_i,
    m=resultados_lineal["m"], b=resultados_lineal["b"],
    error_x=sigma_x, error_y=sigma_i,
    animacion=True# 🔥 Activa la animación
)
