import numpy as np
from cmath import sqrt
from funciones import leer
import math
from scipy import stats as st

l = leer('Numeros.csv')


# Generacion de la variable aleatoria con distribucion de Poisson
def gPoisson(lam: int, N: int = 0, T: float = 1) -> int:
    Tp = T * l.pop(0)
    if Tp >= math.exp(-lam):
        N += 1
        T = Tp
        return gPoisson(lam, N, T)
    else:
        return N

# Generacion de la variable aleatoria con distribucion Normal
def gNorm(mu: float, desv: float) -> float:
    x = 0.0
    n = 0.0
    for i in range(12):
        x += l.pop(0)
    n = (x-6)*desv + mu
    if n <= 0:
        return gNorm(mu, desv)
    return n

#Calculo intervalos
n = [gNorm(10,6.5) for i in range(100)]
inc = (abs(min(n)) + max(n)) / sqrt(len(n)).real
p = min(n)
intervalos = []
for i in range(10):
    intervalos.append([p, p + inc])
    p += inc

#Calculo Oi
Oi = np.zeros(int(sqrt(len(n)).real))
for j in range(len(intervalos)):
    for i in range(len(n)):
        if n[i] <= intervalos[j][1] and n[i] >= intervalos[j][0]:
            Oi[j] += 1

#Calculo de P(x)
Px = np.zeros(int(sqrt(len(n)).real))
for i in range(len(Px)):
    if i != len(Px) - 1:
        Px[i] = st.norm.cdf(intervalos[i][1], 10, 6.5) - st.norm.cdf(intervalos[i][0], 10, 6.5)
Px[len(Px) - 1] = 1 - sum(Px)

#Calculo de Ei
Ei = np.zeros(int(sqrt(len(n)).real))
for i in range(len(Ei)):
    Ei[i] = len(n) * Px[i]

#Calculo de Chi
print(st.chi2.isf(0.05, 100))

#Imprimir en csv
with open('Chi.csv', 'w') as c:
    c.write('Intervalo, P(x), Oi, Ei, Error\n')
    for i in range(len(intervalos)):
        c.write(f'{intervalos[i][0]} - {intervalos[i][1]}, {Px[i]}, {Oi[i]}, {Ei[i]}, {((Oi[i] - Ei[i])**2)/Ei[i]}\n')