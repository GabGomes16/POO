class Caneta:
    def __init__(self, m, c, t, p):
        self.__marca = m
        self.__cor = c
        self.__tampada = t
        self.__preco = p

    @property
    def marca(self):
        return self.__marca

    @property
    def cor(self):
        return self.__cor

    @property
    def tampada(self):
        tampado = self.__tampada
        if tampado is True:
            tampa = "Com tampa"
        else:
            tampa = "Sem tampa"
        return tampa

    @tampada.setter
    def tampada(self, tampa):
        self.__tampada = tampa

    @property
    def preco(self):
        preco_ = str(self.__preco)
        preco_.append(" R$")
        return preco_

    @preco.setter
    def preco(self, preco_):
        self.__preco = preco_

    def escrever(self, texto):
        print(texto, "(caneta ", self.__marca, " na cor ", self.__cor, ")")

class Papelaria:
    def __init__(self, n, c, e):
        self.__nome = n
        self.__CNPJ = c
        self.__endereco = e
        self.listaCanetas = []

    @property
    def nome(self):
        return __nome

    @property
    def cnpj(self):
        return __CNPJ

    @property
    def endereco(self):
        return __endereco

    def fazerPedido(self):
        return 0.0

    def addCaneta(self, caneta):
        self.listaCanetas +=[caneta]