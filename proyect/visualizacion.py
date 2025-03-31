import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class VisualizacionMatplotlib:
    @staticmethod
    def graficar(x, y, m=None, b=None, error_x=None, error_y=None, coef_cuadraticos=None, animacion=False):
        """Genera una gráfica con regresión lineal y/o cuadrática en Matplotlib.
        - Si `animacion=True`, se muestra una animación de la línea o curva ajustándose a los puntos experimentales.
        """
        fig, ax = plt.subplots(figsize=(8, 6))

        # Graficar puntos experimentales
        ax.scatter(x, y, color='blue', label="Datos Experimentales")

        # Graficar barras de error si existen
        if error_x is not None and error_y is not None:
            ax.errorbar(x, y, xerr=error_x, yerr=error_y, fmt='o', capsize=5, label="Barras de Error")

        # Crear línea vacía para animación
        line, = ax.plot([], [], 'r', lw=2, label='Regresión')

        # Función de inicialización de la animación
        def init():
            line.set_data([], [])
            return line,

        # ✅ Definir animación para REGRESIÓN LINEAL
        if m is not None and b is not None:
            x_vals = np.linspace(min(x), max(x), 100)
            y_vals = m * x_vals + b

            def update(frame):
                line.set_data(x_vals[:frame], y_vals[:frame])
                return line,

        # ✅ Definir animación para REGRESIÓN CUADRÁTICA
        elif coef_cuadraticos is not None:
            a, b_quad, c = coef_cuadraticos
            x_vals = np.linspace(min(x), max(x), 100)
            y_vals = a * (x_vals ** 2) + b_quad * x_vals + c

            def update(frame):
                line.set_data(x_vals[:frame], y_vals[:frame])
                return line,

        # Configuración de la gráfica
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Ajuste de Regresión')
        ax.legend()
        ax.grid()

        # ✅ Activar animación si `animacion=True`
        if animacion:
            ani = animation.FuncAnimation(fig, update, frames=len(x_vals), init_func=init, blit=True, interval=30)
            plt.show()
        else:
            # Si no se usa animación, graficar la línea completa de inmediato
            if m is not None and b is not None:
                ax.plot(x_vals, y_vals, 'r', label='Regresión Lineal')
            elif coef_cuadraticos is not None:
                ax.plot(x_vals, y_vals, 'g', linestyle='dashed', label='Regresión Cuadrática')
            plt.show()



