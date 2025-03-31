# 📊 Proyecto de Regresión Lineal y Cuadrática con POO y Visualización Animada

## 📌 Descripción del Proyecto
Este proyecto implementa **regresiones lineales y cuadráticas** utilizando **Programación Orientada a Objetos (POO)** en Python.  
Además, visualiza los datos con gráficos **interactivos y animados** utilizando `matplotlib`.

✔ **Regresión Lineal**: Usa el método de **mínimos cuadrados ponderados**.  
✔ **Regresión Cuadrática**: Resuelve un sistema de ecuaciones mediante **eliminación de Gauss**.  
✔ **Visualización**: Se generan **gráficos animados** mostrando cómo los modelos se ajustan a los datos.  
✔ **Modularización**: Código estructurado en **clases reutilizables** con buena encapsulación y herencia.

---

## 📁 Estructura del Código

📂 `proyecto/`  
 ├── 📜 `datos.py` → Manejo de datos experimentales  
 ├── 📜 `regresion_base.py` → Superclase de regresiones  
 ├── 📜 `regresion_Lineal.py` → Implementación de regresión lineal  
 ├── 📜 `regresion_cuadratica.py` → Implementación de regresión cuadrática  
 ├── 📜 `errores.py` → Cálculo de incertidumbre y error propagado  
 ├── 📜 `visualizacion.py` → Graficación y animaciones con `matplotlib`  
 ├── 📜 `ejemplo_lineal.py` → Ejecuta la regresión lineal con datos de prueba  
 ├── 📜 `ejemplo_cuadratica.py` → Ejecuta la regresión cuadrática con datos de prueba  
 └── 📜 `README.md` → **Este archivo con la documentación**  

---

## 📌 Requisitos Previos

🔹 **Python 3.8+**  
🔹 Instalar las siguientes bibliotecas antes de ejecutar el código:
```sh
pip install matplotlib numpy
```

---

## 🚀 Instrucciones de Instalación y Uso

1️⃣ **Clonar el repositorio**
```sh
git clone https://github.com/tu-usuario/proyecto-regresion.git
cd proyecto-regresion
```

2️⃣ **Ejecutar la regresión lineal**
```sh
python ejemplo_lineal.py
```

3️⃣ **Ejecutar la regresión cuadrática**
```sh
python ejemplo_cuadratica.py
```

✅ **Los resultados se mostrarán en la terminal y en gráficos animados.**  

---

## 📊 Ejemplo de Ejecución

### 📌 **Ejemplo de salida en la terminal (Regresión Lineal)**:
```
🟢 Resultados de la regresión lineal:
Delta: 10457952408901.25
b: -0.01108
m: 0.25659
sigma_b: 0.00143
sigma_m: 0.00089

Tiempo de ejecución de calcular_parametros: 0.00012 segundos
```

### 📌 **Ejemplo de salida en la terminal (Regresión Cuadrática)**:
```
🟢 Resultados de la regresión cuadrática:
a: -0.00981
b: 0.29114
c: -0.03968

Tiempo de ejecución de calcular_parametros: 0.00015 segundos
```

🔹 **Se abrirá un gráfico animado mostrando la curva ajustándose a los datos.**

---

## 🔢 Explicación de Métodos Numéricos Implementados

### 📌 **Regresión Lineal**
La regresión lineal se basa en la ecuación de mínimos cuadrados ponderados:

$$
m = \frac{\sum \left( \frac{x_i y_i}{\sigma_i^2} \right) - \left( \sum \frac{x_i}{\sigma_i^2} \right) \left( \sum \frac{y_i}{\sigma_i^2} \right)}
{\sum \frac{x_i^2}{\sigma_i^2} - \left( \sum \frac{x_i}{\sigma_i^2} \right)^2}
$$

$$
b = \frac{\sum \frac{y_i}{\sigma_i^2} - m \sum \frac{x_i}{\sigma_i^2}}{\sum \frac{1}{\sigma_i^2}}
$$

✔ **Se implementa en `regresion_Lineal.py`.**  

---

### 📌 **Regresión Cuadrática**
Para la regresión cuadrática, se resuelve un sistema de ecuaciones de la forma:

$$
Ax = B
$$

Donde la matriz de coeficientes \( A \) y el vector de términos independientes \( B \) están dados por:

$$
A =
\begin{bmatrix}
\sum x^4 & \sum x^3 & \sum x^2 \\
\sum x^3 & \sum x^2 & \sum x \\
\sum x^2 & \sum x & n
\end{bmatrix}
$$

$$
B =
\begin{bmatrix}
\sum yx^2 \\
\sum yx \\
\sum y
\end{bmatrix}
$$

Los coeficientes \( a, b, c \) se obtienen resolviendo el sistema con eliminación de Gauss.

✔ **Se implementa en `regresion_cuadratica.py`.**  

---

## 📊 Visualización de Resultados

✔ **Se generan gráficos de dispersión con las barras de error.**  
✔ **Se dibuja la recta o curva de regresión de manera animada.**  
✔ **Ejemplo de gráfico generado:**  
## Visualización de Resultados



![Gráfico de Resultados](grafica%20lineal.png)

---

## 🤝 Contribuciones
Si deseas contribuir con mejoras o reportar problemas:
1️⃣ **Haz un fork del repositorio**  
2️⃣ **Crea una rama (`git checkout -b nueva-mejora`)**  
3️⃣ **Envía un Pull Request**  

---

## 📩 Contacto
👤 **Diego Alejandro Molina Arteaga**  
📧 **diegoa.molinaa@uqvirtual.edu.co**  
🔗 [GitHub]((https://github.com/Diego2401join))

---
