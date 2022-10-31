from Pseudo import Pseudo
import math
from gui import x0, g, k, c, alfa


# Parametros iniciales para generar los numeros pseudo-aleatorios

"""x0 = 6
g = 13
k = 15
c = 8191
alfa = 0.05"""

# Se generan los pseudo y se les aplican cada una de las pruebas correspondientes
print("")
n = Pseudo(x0, g, k, c)
n.gLineal()
print(n.pMedias(alfa)[1])
print(n.pVarianza(alfa)[1])
print(n.pUniformidad(alfa)[1])
print(n.pIndependencia(alfa)[1])
print("")
