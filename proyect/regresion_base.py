from abc import ABC, abstractmethod
import time

# Decorador para medir tiempo de ejecución
def tiempo_ejecucion(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {fin - inicio:.5f} segundos")
        return resultado
    return wrapper

class RegresionBase(ABC):
    """Clase base para modelos de regresión."""
    def __init__(self, x, y, sigma=None):
        self._x = x
        self._y = y
        self._sigma = sigma  # Puede ser None en la regresión cuadrática

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def sigma(self):
        return self._sigma

    @abstractmethod
    def calcular_parametros(self):
        """Método abstracto que deben implementar las subclases."""
        pass

