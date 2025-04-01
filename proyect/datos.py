# datos.py
class DatosExperimentales:
    
    def __init__(self, datos): #estado inicial de objeto 
        self._datos = datos

    def obtener_columna(self, indice):
        return [fila[indice] for fila in self._datos]

#Datos manuales
datos_manuales = [
    [0.61350, 0.001291, 1.563667, 0.003512, 2.445053, 0.010983],
    [0.53100, 0.001155, 1.452000, 0.001000, 2.108304, 0.002904],
    [0.41550, 0.000577, 1.290000, 0.001000, 1.664100, 0.002580],
    [0.33050, 0.000577, 1.149667, 0.000577, 1.321733, 0.001328],
    [0.24125, 0.000957, 1.001000, 0.002646, 1.002001, 0.005297]
]
