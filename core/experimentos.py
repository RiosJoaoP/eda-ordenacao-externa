from dsa.Experimentos import Experimentos
import numpy as np
import itertools


def gerar_experimentos():
    k = list(range(4, 13, 2))
    m = [3] + list(range(15, 61, 15))
    i = list(range(11))
    j = list(range(10, 1001, 10))
    temp = [list(x)[0] * list(x)[1] for x in itertools.product(i, j)]
    r = []
    for valor in temp:
        if valor <= 5000 and valor != 0:
            r.append(valor)

    return k, m, r
