import math
from scipy import stats as st


class Pseudo:

    def __init__(self, x0, g, k, c):
        self.x0 = x0
        self.g = g
        self.k = k
        self.c = c
        self.m = int(math.pow(2, self.g))
        self.a = 1 + (4 * self.k)
        self.l = []
        self.archivo = open("Numeros.csv", "w")

    def gLineal(self):
        for i in range(self.m):
            ri = self.x0 / (self.m - 1)
            self.x0 = ((self.a * self.x0) + self.c) % self.m
            self.l.append(ri)
            with open("Numeros.csv", "a") as self.archivo:
                self.archivo.write(str(ri) + "\n")

    def pMedias(self, a):
        p = 0
        z = abs(st.norm.ppf(a / 2))
        li = (1 / 2) - (z * (1 / math.sqrt(12.0 * self.m)))
        ls = (1 / 2) + (z * (1 / math.sqrt(12.0 * self.m)))
        for i in self.l:
            p += i
        p /= self.m
        if li <= p <= ls:
            msg = f"Los datos generados cumplen con la prueba de medias. Limite inferior: {li} Media: {p} Limite superior {ls} "
            return True, msg
        else:
            msg = f"Los datos generados NO cumplen con la prueba de medias. Limite inferior: {li} Media: {p} Limite superior {ls} "
            return False, msg

    def pVarianza(self, a):
        gl = self.m - 1
        p = 0
        var = 0
        for i in self.l:
            p += i
        p /= self.m
        for i in self.l:
            var += math.pow((i - p), 2)
        var /= gl
        ls = st.chi2.isf(a / 2, gl) / (12 * gl)
        li = st.chi2.isf(1 - a / 2, gl) / (12 * gl)
        if li <= var <= ls:
            msg = f"Los datos generados cumplen con la prueba de varianza. Limite inferior: {li} Varianza: {var} Limite superior {ls} "
            return True, msg
        else:
            msg = f"Los datos generados NO cumplen con la prueba de varianza. Limite inferior: {li} Varianza: {p} Limite superior {ls} "
            return False, msg

    def pUniformidad(self, a):
        m = int(math.sqrt(self.m)) + 1  # type: ignore
        gl = m - 1
        chi = st.chi2.isf(a, gl)
        anchoClase = 1 / m
        estChi = 0
        freqEsperada = int(self.m / m + 1)
        intervalos = [[], [], []]
        for i in range(m):
            intervalos[0].append(i * anchoClase)
            intervalos[1].append((i + 1) * anchoClase)
            intervalos[2].append(0)
        for i in self.l:
            for j in range(m):
                if intervalos[0][j] <= i < intervalos[1][j]:
                    intervalos[2][j] += 1
                    break
                elif i == 1:
                    intervalos[2][m - 1] += 1
                    break
        for i in range(m):
            estChi += math.pow((freqEsperada - intervalos[2][i]), 2) / freqEsperada
        if estChi < chi:
            msg = f"Los datos generados cumplen con la prueba de uniformidad. Valor estadistico chi (tablas): {chi} Valor calculado Chi: {estChi}"
            return True,msg
        else:
            msg = f"Los datos generados NO cumplen con la prueba de uniformidad. Valor estadistico chi (tablas): {chi} Valor calculado Chi: {estChi}"
            return False, msg

    def pIndependencia(self, a):
        corridas = []
        c0 = 1
        n = self.m
        n0 = 0
        n1 = 0
        for i in self.l:
            if i >= 1/2:
                corridas.append(1)
                n1 += 1
            else:
                corridas.append(0)
                n0 += 1
        actual = corridas[0]
        for i in range(self.m):
            if corridas[i] != actual:
                c0 += 1
                actual = corridas[i]
        valorEsp = ((2 * n0 * n1) / n) + (1 / 2)
        var = (2 * n0 * n1 * (2 * n0 * n1 - n)) / (math.pow(n, 2) * (n - 1))
        z0 = (c0 - valorEsp) / (math.sqrt(var))
        z = abs(st.norm.ppf(a / 2))
        if (-1)*z < z0 < z:
            msg = f"Los datos generados cumplen con la prueba de independencia. Valor estadistico Z0 (tablas): {z} Valor calculado Z0: {z0}"
            return True,msg
        else:
            msg = f"Los datos generados NO cumplen con la prueba de independencia. Valor estadistico Z0 (tablas): {z} Valor calculado Z0: {z0}"
            return False, msg
