
def leer(path : str) -> list[float]:
    l = []
    with open(path, 'r') as f:
        for n in f.readlines():
            l.append(float(n))
    return l