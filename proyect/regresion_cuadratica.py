# regresion_cuadratica.py
from regresion_base import RegresionBase, tiempo_ejecucion

class RegresionCuadratica(RegresionBase):
    """Clase que implementa la regresión cuadrática por el método de mínimos cuadrados."""

    @tiempo_ejecucion
    def calcular_parametros(self):
        """
        Calcula los coeficientes a, b y c de la ecuación cuadrática ajustada y los retorna.

        Retorna:
        - a, b, c: Coeficientes de la ecuación cuadrática ajustada (y = ax² + bx + c).
        """
        n = len(self.x)

        # 📌 Cálculo de sumatorias necesarias para la regresión cuadrática
        sum_x = sum(self.x)
        sum_x2 = sum(x**2 for x in self.x)
        sum_x3 = sum(x**3 for x in self.x)
        sum_x4 = sum(x**4 for x in self.x)
        sum_y = sum(self.y)
        sum_yx = sum(y * x for x, y in zip(self.x, self.y))
        sum_yx2 = sum(y * x**2 for x, y in zip(self.x, self.y))

        # 📌 Construcción de la matriz A del sistema Ax = B
        A = [
            [sum_x4, sum_x3, sum_x2],
            [sum_x3, sum_x2, sum_x],
            [sum_x2, sum_x, n]
        ]

        # 📌 Vector B del sistema Ax = B
        B = [sum_yx2, sum_yx, sum_y]

        # 📌 Resolviendo el sistema de ecuaciones
        coeficientes = self.resolver_sistema(A, B)

        # 📌 Resultados de la regresión cuadrática
        resultado = {"a": coeficientes[0], "b": coeficientes[1], "c": coeficientes[2]}

        print("\n🟢 Resultados de la regresión cuadrática:")
        for clave, valor in resultado.items():
            print(f"{clave}: {valor}")

        return resultado

    @staticmethod
    def resolver_sistema(A, B):
        """
        Resuelve un sistema de ecuaciones lineales de la forma Ax = B usando eliminación de Gauss.

        :param A: Matriz de coeficientes del sistema.
        :param B: Vector de términos independientes.
        :return: Lista con la solución del sistema (valores de a, b, c).
        """
        n = len(A)

        # 📌 Expansión de la matriz A con el vector B para la eliminación de Gauss
        for i in range(n):
            A[i].append(B[i])

        # 📌 Aplicación del método de eliminación de Gauss
        for i in range(n):
            pivote = A[i][i]
            for j in range(i, n + 1):
                A[i][j] /= pivote

            for k in range(i + 1, n):
                factor = A[k][i]
                for j in range(i, n + 1):
                    A[k][j] -= factor * A[i][j]

        # 📌 Sustitución hacia atrás para obtener los valores de los coeficientes
        x = [0] * n
        for i in range(n - 1, -1, -1):
            x[i] = A[i][n]
            for j in range(i + 1, n):
                x[i] -= A[i][j] * x[j]

        return x

