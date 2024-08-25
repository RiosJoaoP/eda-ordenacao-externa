import sys
from core.experimentos import gerar_experimentos
from dsa.TestesManuais import TestesManuais
from dsa.Experimentos import Experimentos
from core.resolverTestesManuais import resolver_testes_manuais

''''
    Note:

    Main.py
    Main file to run the project
    Usage:
        python3 Main.py [file]
    Example:
        python3 Main.py examples/hard_example

    to Output the results to a file, use the following command:
        python3 Main.py examples/hard_example > output.txt

'''

if __name__ == "__main__":
    # experimentos = gerar_experimentos()

    tipo_teste = input("Testes Manuais(M) ou Experimentais(E)? ")

    if tipo_teste.lower() == "m":
        ferramenta_ordenacao = TestesManuais()
        algoritmo, m, k, r, n, registros = resolver_testes_manuais()
        ferramenta_ordenacao.ordenar(
            algoritmo, m, k, r, n, registros, verbose=True)
    else:
        ferramenta_ordenacao = Experimentos()

    # tipo_teste = "m"

    # if tipo_teste.lower() == "m":
    #     ferramenta_ordenacao = TestesManuais()
    #     algoritmo, m, k, r, n, registros = "B", 3, 4, 3, 17, [
    #         7, 1, 5, 6, 3, 8, 2, 10, 4, 9, 1, 3, 7, 4, 1, 2, 3]
    #     ferramenta_ordenacao.ordenar(
    #         algoritmo, m, k, r, n, registros, verbose=True)
    # else:
    #     ferramenta_ordenacao = Experimentos()
