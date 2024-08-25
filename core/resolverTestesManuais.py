def resolver_testes_manuais():
    algoritmo = input("Algoritmo (B, P ou C): ")
    m, k, r, n = map(int, input("m, k, r e n: ").strip().split())
    registros = list(map(int, input("Registros: ").strip().split()))

    return algoritmo, m, k, r, n, registros
