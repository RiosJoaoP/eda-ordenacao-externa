from dsa.AlgoritmosOrdenacao import balanceadaMultiCaminhos, polifasica, cascata
from collections import deque


class Experimentos:
    def __init__(self):
        self.paginas = deque()
        self.numero_registros = 0
        self.algoritmos = {
            "B": balanceadaMultiCaminhos,
            "P": polifasica,
            "C": cascata
        }

    def __str__(self):
        return "Não Implementado!"
