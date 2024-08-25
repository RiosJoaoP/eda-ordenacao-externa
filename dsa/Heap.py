from heapq import heappush, heappop


class Heap:
    def __init__(self):
        self.heap = []

    def inserir(self, item):
        heappush(self.heap, item)

    def remover(self):
        return heappop(self.heap)

    def primeiro(self):
        try:
            return self.heap[0]
        except:
            return None

    def estaVazio(self):
        return (len(self.heap) == 0)

    def desmarcarTudo(self):
        for registro in self.heap:
            registro.removerFlag()

    def marcarTudo(self):
        for registro in self.heap:
            registro.marcar()
