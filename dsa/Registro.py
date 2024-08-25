class Registro:
    def __init__(self, valor):
        self.valor = valor
        self.flag = 0
        self.indice = None

    def definirFlag(self):
        self.flag = 1

    def removerFlag(self):
        self.flag = 0

    def definirIndice(self, indice):
        self.indice = indice

    def __lt__(self, outro):
        if self.flag != outro.flag:
            return self.flag < outro.flag
        return self.valor < outro.valor

    def __str__(self):
        return str(self.valor)

    def __repr__(self):
        return str(self.valor)
