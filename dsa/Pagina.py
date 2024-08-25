from collections import deque
from dsa.Registro import Registro


class Pagina:
    def __init__(self, indice):
        self.registros = deque()
        self.bloqueada = False
        self.indice = indice

    def obterIndicePagina(self):
        return self.indice

    def obterMenorSubsequencia(self):
        preenchidos = [subseq for subseq in self.registros if len(subseq) > 0]
        if len(preenchidos) > 1:
            menor = preenchidos[0]
            for i in range(1, len(preenchidos)):
                if len(preenchidos[i]) < len(menor):
                    menor = preenchidos[i]
            return menor

    def obter(self, indice):
        if self.registros[indice] is not None:
            return self.registros[indice]
        return -1

    def remover(self):
        if len(self.registros) < 1:
            print(self.registros)
        item = self.registros[0].popleft()
        if len(self.registros[0]) < 1:
            self.bloqueada = True
        return item

    def removerSequencia(self):
        return self.registros.popleft()

    def ativar(self):
        self.registros.popleft()
        self.bloqueada = False

    def estaBloqueada(self):
        return self.bloqueada

    def definir(self, indice, valor):
        if len(self.registros) > indice:
            self.registros[indice] = valor

    def adicionar(self, sequencia, indice):
        for elem in sequencia:
            elem.definirIndice(indice)
        self.registros.append(sequencia)

    def obterContagemSequencias(self):
        return len(self.registros)

    def __str__(self):
        return str(self.registros)

    def imprimir(self):
        for sequencia in self.registros:
            print("{ ", end="")
            sequencia_print = ""
            for i in range(len(sequencia)):
                sequencia_print += f"{sequencia[i]} "
            print(sequencia_print, end="")
            print("}", end="")

    def __repr__(self):
        return str(self.registros)

    def estaVazia(self):
        return len(self.registros) < 1

    def __len__(self):
        qtdRegistros = 0
        for sequencia in self.registros:
            qtdRegistros += len(sequencia)
        return qtdRegistros
