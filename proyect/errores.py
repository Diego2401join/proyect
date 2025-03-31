# errores.py
import math
from regresion_Lineal import tiempo_ejecucion

class CalculoError:
    @staticmethod
    @tiempo_ejecucion
    def calcular_error_propagado(sigma_m):
        return (4 * math.pi ** 2) * sigma_m

