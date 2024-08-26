from collections import deque
from dsa.Heap import Heap


class AlgoritmosOrdenacao:

    @staticmethod
    def obterMaiorPagina(problema):
        return max(problema.paginas, key=len)

    @staticmethod
    def obterMenorPagina(problema, preenchidos):
        return min(preenchidos, key=lambda x: x.obterContagemSequencias())

    @staticmethod
    def intercalar(problema, preenchidos, final):
        heap = Heap()
        for pagina in preenchidos:
            if not pagina.estaVazia():
                heap.inserir(pagina.remover())

        nova_sequencia = deque()
        num_escritas = 0

        while heap.heap:
            item = heap.remover()
            if not problema.paginas[item.indice].estaBloqueada():
                heap.inserir(problema.paginas[item.indice].remover())
            nova_sequencia.append(item)
            num_escritas += 1

        final.adicionar(nova_sequencia, final.indice)
        return num_escritas

    @staticmethod
    def intercalarPolifasica(problema, menor_pagina, preenchidos, final):
        heap = Heap()
        num_escritas = 0

        while not menor_pagina.estaVazia():
            for pagina in preenchidos:
                heap.inserir(pagina.remover())

            nova_sequencia = deque()

            while heap.heap:
                item = heap.remover()
                if not problema.paginas[item.indice].estaBloqueada():
                    heap.inserir(problema.paginas[item.indice].remover())
                nova_sequencia.append(item)
                num_escritas += 1
            final.adicionar(nova_sequencia, final.indice)

            [pagina.ativar() for pagina in preenchidos if pagina.estaBloqueada()]

        return num_escritas

    @staticmethod
    def estaOrdenado(problema):
        contagem = 0
        for pagina in problema.paginas:
            if not pagina.estaVazia():
                if pagina.obterContagemSequencias() == 1:
                    contagem += 1
                else:
                    return False

        return contagem == 1

    @staticmethod
    def calcularAlpha(problema, registros_processados):
        return round(registros_processados / problema.numero_registros, 2)

    @staticmethod
    def calcularBeta(problema, blocos, m):
        contagem_sequencias = sum(pagina.obterContagemSequencias()
                                  for pagina in blocos)
        beta = (1 / (m * contagem_sequencias)) * problema.numero_registros
        return round(beta, 2)

    @staticmethod
    def imprimir_resultados(problema, preenchidos, contador, m, verbose=True):
        beta = AlgoritmosOrdenacao.calcularBeta(problema, preenchidos, m)

        if verbose:
            print(f"fase {contador} {beta}")
            for pagina in preenchidos:
                print(f"{pagina.indice + 1}: ", end="")
                pagina.imprimir()
                print()

        problema.beta.append(round(beta, 2))

    @staticmethod
    def algumaPaginaVazia(paginas):
        return any(pagina.estaVazia() for pagina in paginas)

    @staticmethod
    def todasPaginasVazias(paginas):
        return all(pagina.estaVazia() for pagina in paginas)

    # --------------------- Algoritmos ---------------------

    @staticmethod
    def balanceadaMultiCaminhos(problema, m, r, k, verbose=True, salvar=False):
        contador = 0
        escritas = 0

        while not AlgoritmosOrdenacao.estaOrdenado(problema):
            preenchidos = [
                pagina for pagina in problema.paginas if not pagina.estaVazia()]
            nao_preenchidos = [
                pagina for pagina in problema.paginas if pagina.estaVazia()]

            AlgoritmosOrdenacao.imprimir_resultados(
                problema, preenchidos, contador, m, verbose)

            while not preenchidos[0].estaVazia():
                for pagina in nao_preenchidos:
                    if AlgoritmosOrdenacao.estaOrdenado(problema) or preenchidos[0].estaVazia():
                        break
                    escritas += AlgoritmosOrdenacao.intercalar(
                        problema, preenchidos, pagina)
                    [pagina.ativar()
                     for pagina in preenchidos if pagina.estaBloqueada()]

            contador += 1

        preenchidos = [
            pagina for pagina in problema.paginas if not pagina.estaVazia()]
        AlgoritmosOrdenacao.imprimir_resultados(
            problema, preenchidos, contador, m, verbose)
        problema.paginaFinal = preenchidos
        problema.result_alpha = AlgoritmosOrdenacao.calcularAlpha(
            problema, escritas)
        if verbose:
            print(f"final {problema.result_alpha}")

    @staticmethod
    def polifasica(problema, m, r, k, imprimir=True, salvar=False):
        contador = 0
        escritas = 0.0
        while not AlgoritmosOrdenacao.estaOrdenado(problema):
            preenchidos = [
                pagina for pagina in problema.paginas if not pagina.estaVazia()]
            nao_preenchidos = [
                pagina for pagina in problema.paginas if pagina.estaVazia()]
            menor_pagina = AlgoritmosOrdenacao.obterMenorPagina(
                problema, preenchidos)

            AlgoritmosOrdenacao.imprimir_resultados(
                problema, preenchidos, contador, m, imprimir)

            escritas += AlgoritmosOrdenacao.intercalarPolifasica(
                problema, menor_pagina, preenchidos, nao_preenchidos[0])
            [pagina.ativar() for pagina in preenchidos if pagina.estaBloqueada()]

            contador += 1

        preenchidos = [
            pagina for pagina in problema.paginas if not pagina.estaVazia()]
        AlgoritmosOrdenacao.imprimir_resultados(
            problema, preenchidos, contador, m, imprimir)
        problema.paginaFinal = preenchidos
        problema.result_alpha = AlgoritmosOrdenacao.calcularAlpha(
            problema, escritas)
        if imprimir:
            print(f"final {problema.result_alpha}")
        if salvar:
            with open('./outputs/polifasica.txt', 'a') as file:
                file.write(f"{r}-{k}-{problema.result_alpha}\n")

    @staticmethod
    def cascata(problema, m, r, k, imprimir=True, salvar=False):
        contador = 0
        escritas = 0.0

        while not AlgoritmosOrdenacao.estaOrdenado(problema):
            preenchidos = [
                pagina for pagina in problema.paginas if not pagina.estaVazia()]
            nao_preenchidos = [
                pagina for pagina in problema.paginas if pagina.estaVazia()]
            final = nao_preenchidos[0]

            AlgoritmosOrdenacao.imprimir_resultados(
                problema, preenchidos, contador, m, imprimir)

            maior_pagina = AlgoritmosOrdenacao.obterMaiorPagina(problema)

            while not maior_pagina.estaVazia():
                escritas += AlgoritmosOrdenacao.intercalar(
                    problema, preenchidos, final)
                [pagina.ativar()
                 for pagina in preenchidos if pagina.estaBloqueada()]

                nao_preenchidos = [
                    pagina for pagina in problema.paginas if pagina.estaVazia()]
                if nao_preenchidos:
                    final = nao_preenchidos[0]

            contador += 1

        preenchidos = [
            pagina for pagina in problema.paginas if not pagina.estaVazia()]
        problema.paginaFinal = preenchidos
        AlgoritmosOrdenacao.imprimir_resultados(
            problema, preenchidos, contador, m, imprimir)
        problema.result_alpha = AlgoritmosOrdenacao.calcularAlpha(
            problema, escritas)
        if imprimir:
            print(f"final {problema.result_alpha}")
