from dsa.TestesManuais import TestesManuais
from dsa.Experimentos import Experimentos
from core.resolverTestesManuais import resolver_testes_manuais
from core.resolverExperimentos import resolver_experimentos

if __name__ == "__main__":

    tipo_teste = input("Testes Manuais(M) ou Experimentais(E)? ")

    if tipo_teste.lower() == "m":
        ferramenta_ordenacao = TestesManuais()
        algoritmo, m, k, r, n, registros = resolver_testes_manuais()
        ferramenta_ordenacao.ordenar(
            algoritmo, m, k, r, n, registros, verbose=True)
    else:
        ferramenta_ordenacao = Experimentos()
        resolver_experimentos(ferramenta_ordenacao)
