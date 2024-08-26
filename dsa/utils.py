from collections import deque
from dsa.Pagina import Pagina

import math


def limite_de_paginas(k, algoritmo):
    return math.floor(k/2) if algoritmo == "B" else k-1


def criar_paginas(k):
    paginas = deque()
    for i in range(k):
        paginas.append(Pagina(i))

    return paginas
