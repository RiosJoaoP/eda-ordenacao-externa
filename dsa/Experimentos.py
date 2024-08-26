from dsa.Registro import Registro
from dsa.utils import limite_de_paginas, criar_paginas, criar_registros_aleatorios
from dsa.AlgoritmosOrdenacao import AlgoritmosOrdenacao
from collections import deque
from dsa.FildaDePrioridade import FilaDePrioridade


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

    def ordenar(self, algoritmo, m, k, r, n, verbose=True):
        self.limpar_estrutura()
        self.paginas = criar_paginas(k)
        registros = criar_registros_aleatorios(n)
        self.gerar_sequencias(
            registros, m, limite_de_paginas(k, algoritmo))
        algoritmo_escolhido = self.algoritmos[algoritmo]
        algoritmo_escolhido(self, m, r, k, verbose, salvar=True)

    def registros_alocados(self, sequencias):
        i = 0

        for sequencia in sequencias:
            for _ in sequencia:
                i += 1

        return i

    def gerar_sequencias(self, registros, m, limite_de_paginas):
        n = len(registros)

        fila_de_prioridade = FilaDePrioridade()

        sequencia_atual = 0

        sequencias = [deque()]
        marcados = []

        for registro in registros[:m]:
            fila_de_prioridade.inserir(registro)

        sequencias[sequencia_atual].append(fila_de_prioridade.excluir())

        i = m

        while self.registros_alocados(sequencias) < n:

            if len(fila_de_prioridade.fila) < m:
                if i == n:
                    registros_restantes = len(fila_de_prioridade.fila)
                    if len(marcados) > 0:
                        fila_de_prioridade = FilaDePrioridade()
                        for marcado in marcados:
                            fila_de_prioridade.inserir(marcado)
                        sequencias.append(deque())
                        sequencia_atual += 1
                    for _ in range(registros_restantes):
                        sequencias[sequencia_atual].append(
                            fila_de_prioridade.excluir())
                    break
                else:
                    try:
                        fila_de_prioridade.inserir(registros[i])
                    except:
                        break

            item_atual = fila_de_prioridade.excluir()

            if len(sequencias[sequencia_atual]) == 0:
                sequencias[sequencia_atual].append(item_atual)
            else:
                if sequencias[sequencia_atual][-1] <= item_atual:
                    sequencias[sequencia_atual].append(item_atual)
                else:
                    marcados.append(item_atual)
                    fila_de_prioridade.inserir(float("inf"))

            if len(marcados) == m:
                fila_de_prioridade = FilaDePrioridade()
                for valor in marcados:
                    fila_de_prioridade.inserir(valor)
                marcados = []
                sequencias.append(deque())
                sequencia_atual += 1

        for i in range(len(sequencias)):
            registros = deque()
            for valor in sequencias[i]:
                registros.append(Registro(valor))

            sequencias[i] = registros

        num_registros = 0

        for i in range(limite_de_paginas):
            try:
                self.paginas[i].adicionar(sequencias[i], i)
                num_registros += len(sequencias[i])
            except:
                pass

        self.numero_registros = num_registros
