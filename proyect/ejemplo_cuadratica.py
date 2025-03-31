# ejemplo_cuadratica.py
from datos import DatosExperimentales
from regresion_cuadratica import RegresionCuadratica
from visualizacion import VisualizacionMatplotlib

# 📌 Datos experimentales para regresión cuadrática
datos_cuadraticos = [
    [0.5, 1.0],
    [1.0, 2.1],
    [1.5, 3.6],
    [2.0, 5.8],
    [2.5, 9.3],
    [3.0, 12.9]
]

datos_experimentales = DatosExperimentales(datos_cuadraticos)
x_i = datos_experimentales.obtener_columna(0)
y_i = datos_experimentales.obtener_columna(1)

modelo_cuadratico = RegresionCuadratica(x_i, y_i)
resultados_cuadratico = modelo_cuadratico.calcular_parametros()

# 📌 Generar animación en la regresión cuadrática
VisualizacionMatplotlib.graficar(
    x_i, y_i,
    coef_cuadraticos=(resultados_cuadratico["a"], resultados_cuadratico["b"], resultados_cuadratico["c"]),
    animacion=True # 🔥 Activa la animación
)

