from collections import deque
from dsa.Heap import Heap


def intercalar(problema, preenchidos, final, menor_pagina=None, polifasica=False):

    heap = Heap()
    num_escritas = 0
    nova_sequencia = deque()

    if polifasica:
        while not menor_pagina.estaVazia():
            for pagina in preenchidos:
                heap.inserir(pagina.remover())

            while heap.heap:
                item = heap.remover()
                if not problema.paginas[item.indice].estaBloqueada():
                    heap.inserir(problema.paginas[item.indice].remover())
                nova_sequencia.append(item)
                num_escritas += 1
            final.adicionar(nova_sequencia, final.indice)

            [pagina.ativar()
                for pagina in preenchidos if pagina.estaBloqueada()]
    else:
        heap = Heap()
        for pagina in preenchidos:
            if not pagina.estaVazia():
                heap.inserir(pagina.remover())

        while heap.heap:
            item = heap.remover()
            if not problema.paginas[item.indice].estaBloqueada():
                heap.inserir(problema.paginas[item.indice].remover())
            nova_sequencia.append(item)
            num_escritas += 1

        final.adicionar(nova_sequencia, final.indice)
    return num_escritas


def fim(problema):
    contagem = sum(1 for pagina in problema.paginas if not pagina.estaVazia(
    ) and pagina.obterContagemSequencias() == 1)
    return contagem == 1


def calcularAlpha(problema, registros_processados):
    return round(registros_processados / problema.numero_registros, 2)


def calcularBeta(problema, blocos, m):
    contagem_sequencias = sum(pagina.obterContagemSequencias()
                              for pagina in blocos)
    beta = (1 / (m * contagem_sequencias)) * problema.numero_registros
    return round(beta, 2)


def imprimir_resultados(problema, preenchidos, contador, m, verbose=True):
    beta = round(calcularBeta(
        problema, preenchidos, m), 2)

    if verbose:
        print(f"fase {contador} {beta}")
        for pagina in preenchidos:
            print(f"{pagina.indice + 1}: ", end="")
            pagina.imprimir()
            print()

# --------------------- Algoritmos ---------------------


def balanceadaMultiCaminhos(problema, m, r, k, verbose=True, salvar=False):
    contador = 0
    escritas = 0

    while not fim(problema):
        preenchidos = [
            pagina for pagina in problema.paginas if not pagina.estaVazia()]
        nao_preenchidos = [
            pagina for pagina in problema.paginas if pagina.estaVazia()]

        imprimir_resultados(
            problema, preenchidos, contador, m, verbose)

        while preenchidos and not preenchidos[0].estaVazia():
            for pagina in nao_preenchidos:
                if fim(problema) or preenchidos[0].estaVazia():
                    break
                escritas += intercalar(
                    problema, preenchidos, pagina)
                [pagina.ativar()
                    for pagina in preenchidos if pagina.estaBloqueada()]

        contador += 1

    preenchidos = [
        pagina for pagina in problema.paginas if not pagina.estaVazia()]
    imprimir_resultados(
        problema, preenchidos, contador, m, verbose)

    problema.paginaFinal = preenchidos
    problema.result_alpha = calcularAlpha(
        problema, escritas)

    if verbose:
        print(f"final {problema.result_alpha}")


def polifasica(problema, m, r, k, imprimir=True, salvar=False):
    contador = 0
    escritas = 0.0
    while not fim(problema):
        preenchidos = [
            pagina for pagina in problema.paginas if not pagina.estaVazia()]
        nao_preenchidos = [
            pagina for pagina in problema.paginas if pagina.estaVazia()]
        menor_pagina = min(
            preenchidos, key=lambda x: x.obterContagemSequencias())

        imprimir_resultados(
            problema, preenchidos, contador, m, imprimir)

        escritas += intercalar(
            problema, preenchidos, nao_preenchidos[0], menor_pagina=menor_pagina, polifasica=True)
        [pagina.ativar() for pagina in preenchidos if pagina.estaBloqueada()]

        contador += 1

    preenchidos = [
        pagina for pagina in problema.paginas if not pagina.estaVazia()]
    imprimir_resultados(
        problema, preenchidos, contador, m, imprimir)
    problema.paginaFinal = preenchidos
    problema.result_alpha = calcularAlpha(
        problema, escritas)
    if imprimir:
        print(f"final {problema.result_alpha}")
    if salvar:
        with open('./outputs/polifasica.txt', 'a') as file:
            file.write(f"{r}-{k}-{problema.result_alpha}\n")


def cascata(problema, m, r, k, imprimir=True, salvar=False):
    contador = 0
    escritas = 0.0

    while not fim(problema):
        preenchidos = [
            pagina for pagina in problema.paginas if not pagina.estaVazia()]
        nao_preenchidos = [
            pagina for pagina in problema.paginas if pagina.estaVazia()]
        final = nao_preenchidos[0]

        imprimir_resultados(
            problema, preenchidos, contador, m, imprimir)

        maior_pagina = max(problema.paginas, key=len)

        while not maior_pagina.estaVazia():
            escritas += intercalar(
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
    imprimir_resultados(
        problema, preenchidos, contador, m, imprimir)
    problema.result_alpha = calcularAlpha(
        problema, escritas)
    if imprimir:
        print(f"final {problema.result_alpha}")
