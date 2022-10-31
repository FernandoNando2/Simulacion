import statistics as sts
import Transformada as ti
from funciones import leer

# Ejercicio dados
with open("Dados.csv", "w") as archivo:
    archivo.write("Corrida,Datos,Media,Mediana,Moda,S,S^2")
with open("tiDados.csv", "r") as f:
    a , b = ti.leerTi(f)
n = leer("Numeros.csv")
j = 1
lanzamientos = 50
for i in range(1, 11):
    with open("Dados.csv", "a") as archivo:
        archivo.write(f"\n{i},{j}-{lanzamientos}")
    numeros = [ti.gTi(a, b, n.pop(0)) for i in range(50)]
    with open("Dados.csv", "a") as archivo:
        archivo.write(
            f",{sts.mean(numeros)},{sts.median(numeros)},{sts.mode(numeros)},{sts.pstdev(numeros):.4f},{sts.pvariance(numeros):.4f}")  # type: ignore
    j += 50
    lanzamientos += 50
