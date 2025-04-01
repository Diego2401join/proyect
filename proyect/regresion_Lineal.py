# regresion_lineal.py
import math
from time import time
from regresion_base import RegresionBase, tiempo_ejecucion

class RegresionLineal(RegresionBase):
    
    @tiempo_ejecucion
    def calcular_parametros(self):
        sum_1_sigma2 = sum(1 / (s ** 2) for s in self._sigma)
        sum_x2_sigma2 = sum((xi ** 2) / (si ** 2) for xi, si in zip(self._x, self._sigma))
        sum_x_sigma2 = sum(xi / (si ** 2) for xi, si in zip(self._x, self._sigma))
        sum_y_sigma2 = sum(yi / (si ** 2) for yi, si in zip(self._y, self._sigma))
        sum_xy_sigma2 = sum((xi * yi) / (si ** 2) for xi, yi, si in zip(self._x, self._y, self._sigma))

        Delta = sum_1_sigma2 * sum_x2_sigma2 - (sum_x_sigma2) ** 2

        b = (1 / Delta) * (sum_x2_sigma2 * sum_y_sigma2 - sum_x_sigma2 * sum_xy_sigma2)
        m = (1 / Delta) * (sum_1_sigma2 * sum_xy_sigma2 - sum_x_sigma2 * sum_y_sigma2)

        sigma_b2 = (1 / Delta) * sum_x2_sigma2
        sigma_b = math.sqrt(sigma_b2)

        sigma_m2 = (1 / Delta) * sum_1_sigma2
        sigma_m = math.sqrt(sigma_m2)

        resultado = {"Delta": Delta, "b": b, "m": m, "sigma_b": sigma_b, "sigma_m": sigma_m}
        
        print("\n🟢 Resultados de la regresión lineal:")
        for clave, valor in resultado.items():
            print(f"{clave}: {valor}")

        return resultado
