from fractions import Fraction
from io import TextIOWrapper
# Funcion peek para previsualizar caracteres sin consumir.


def peek(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line


# Funcion para leer tablas de probabilidades de un archivo csv con formato especificado.
'''Devuelve dos listas, una almacena el valor de la variable aleatoria y la otra su probabilidad.'''


def leerTi(f : TextIOWrapper) -> tuple:
    if f.closed:
        return 0, 0
    else:
        a = []
        b = []
        if peek(f)[0] == '#':
            f.readline()
        while peek(f)[0] != ';':
            l = [float(Fraction(i)) for i in f.readline().split(",")]
            a.append(round(l[0]))
            b.append(l[1])
        f.readline()
        if peek(f) == "":
            f.close()
        return a, b


# Funcion para generar la Transformada Inversa y devuelve el valor aleatorio correspondiente.
def gTi(a : list[float], b : list[float], pseudo : float) -> float:
    a = a.copy()
    b = b.copy()
    li = 0
    ls = b.pop(0)
    for i in a:
        if li <= pseudo < ls:
            return i
        elif pseudo == 1:
            return a[-1]
        else:
            li = ls
            ls = ls + b.pop(0)
    return 0.0
