from core.experimentos import gerar_experimentos
import math


def resolver_experimentos(ferramenta_ordenacao):
    algoritmo = input("Algoritmo (B, P ou C): ")
    k_lista, m_lista, r_lista = gerar_experimentos()

    for r in r_lista:
        for k in k_lista:
            for m in m_lista:
                n = math.ceil(r/k)
                ferramenta_ordenacao.ordenar(
                    algoritmo, m, k, r, n, verbose=True)
