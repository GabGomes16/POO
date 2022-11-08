class Caneta:

    def __init__(self, m, c, t, p):
        self.marca = m
        self.cor = c
        self.tampada = t
        self.preco = p

    def escrever(self, texto):
        print(texto, "(caneta ", self.marca, " na cor ", self.cor, ")")

class Papelaria:
    def __init__(self, n, c, e):
        self.nome = n
        self.CNPJ = c
        self.endereco = e
        self.listaCanetas = []

    def fazerPedido(self):
        return 0.0

    def addCaneta(self, caneta):
        self.listaCanetas +=[caneta]    

exemplo1 = Caneta("Bic", "Vermelha", True, "5.0")
exemplo2 = Caneta("Faber castell", "Azul", False, "2.0")

exemplo2.escrever("É um dia feliz! Apareceu a vacina! =)")
exemplo2.escrever("Vora passsear! Chega de confinamento! =)")
exemplo1.escrever("Mas esse dia ainda não é hoje... =(")

objetoPapelaria = Papelaria("Calunga", "333.444.555/0001-04", "Rua Teste, 6")
objetoPapelaria.addCaneta(exemplo2)
print(objetoPapelaria.listaCanetas[0].cor)
objetoPapelaria.addCaneta(exemplo1)
print(objetoPapelaria.listaCanetas[0].cor)
print(objetoPapelaria.listaCanetas[1].marca)   