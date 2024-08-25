import heapq


class FilaDePrioridade(object):
    def __init__(self):
        self.fila = []

    def estaVazia(self):
        return len(self.fila) == 0

    def inserir(self, valor):
        heapq.heappush(self.fila, valor)

    def excluir(self):
        try:
            return heapq.heappop(self.fila)
        except IndexError:
            print()
            exit()
