from dsa.Registro import Registro
from dsa.utils import limite_de_paginas, criar_paginas, permutar
from dsa.AlgoritmosOrdenacao import AlgoritmosOrdenacao
from collections import deque


class Experimentos:
    def __init__(self):
        self.paginas = deque()
        self.numero_registros = 0
        self.beta = []
        self.alpha = None
        self.resultado = None
        self.algoritmos = {
            "B": AlgoritmosOrdenacao.balanceadaMultiCaminhos,
            "P": AlgoritmosOrdenacao.polifasica,
            "C": AlgoritmosOrdenacao.cascata
        }

    def limpar_estrutura(self):
        self.paginas.clear()
        self.numero_registros = 0
        self.beta.clear()
        self.alpha = None
        self.resultado = None

    def ordenar(self, algoritmo, m, k, r, n, registros, verbose=True):
        self.limpar_estrutura()
        self.paginas = criar_paginas(k)
        self.paginas = self.gerar_sequencias(n, r, k, algoritmo)
        algoritmo_escolhido = self.algoritmos[algoritmo]
        algoritmo_escolhido(self, m, verbose)

    def gerar_sequencias(self, n, r, k, metodo):
        limite_paginas = limite_de_paginas(k, metodo)
        paginas = criar_paginas(k)
        sequencia = deque()
        arquivos_possiveis = permutar(n)
        contador_paginas = 0
        contador_sequencias = 0
        numero_registros = 0

        if r % limite_paginas == 0:
            sequencia.append(Registro(arquivos_possiveis[numero_registros]))
            numero_registros += 1
            paginas[contador_paginas].adicionar(sequencia, contador_paginas)
            sequencia = deque()
            r -= 1

        while contador_sequencias < r:
            if len(sequencia) == 0:
                sequencia.append(
                    Registro(arquivos_possiveis[numero_registros]))
                numero_registros += 1
                continue

            if sequencia[-1].valor < Registro(arquivos_possiveis[numero_registros]).valor:
                sequencia.append(
                    Registro(arquivos_possiveis[numero_registros]))
                numero_registros += 1
            else:
                paginas[contador_paginas].adicionar(
                    sequencia, contador_paginas)
                contador_paginas += 1
                contador_sequencias += 1
                contador_paginas %= limite_paginas
                sequencia = deque()

        self.numero_registros = numero_registros
        return paginas
