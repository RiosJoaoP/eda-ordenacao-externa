from collections import deque
from dsa.Pagina import Pagina

import math
import numpy as np
import random


def limite_de_paginas(k, algoritmo):
    return math.floor(k/2) if algoritmo == "B" else k-1


def criar_paginas(k):
    paginas = deque()
    for i in range(k):
        paginas.append(Pagina(i))

    return paginas


def permutar(n):
    return list(np.random.permutation(n))


def criar_registros_aleatorios(n):
    registros = random.sample(range(1, 10001), n)
    random.shuffle(registros)
    return registros
