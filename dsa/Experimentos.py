from dsa.Registro import Registro
from dsa.utils import limite_de_paginas, criar_paginas, criar_registros_aleatorios
from dsa.AlgoritmosOrdenacao import AlgoritmosOrdenacao
from collections import deque
from dsa.FildaDePrioridade import FilaDePrioridade


class Experimentos:
    def __init__(self):
        self.paginas = deque()
        self.numero_registros = 0
        self.algoritmos = {
            "B": AlgoritmosOrdenacao.balanceadaMultiCaminhos,
            "P": AlgoritmosOrdenacao.polifasica,
            "C": AlgoritmosOrdenacao.cascata
        }

    def __str__(self):
        return "Não Implementado!"
