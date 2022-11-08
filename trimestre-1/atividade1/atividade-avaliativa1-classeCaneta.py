class Caneta:

    def __init__(self, m, c, t):
        self.marca = m
        self.cor = c
        self.tampada = t

    def escrever(self, texto):
        print(texto, "(caneta ", self.marca, " na cor ", self.cor, ")")

exemplo1 = Caneta("Bic", "Vermelha", True)
exemplo2 = Caneta("Faber castell", "Azul", False)

exemplo2.escrever("É um dia feliz! Apareceu a vacina! =)")
exemplo2.escrever("Vora passsear! Chega de confinamento! =)")
exemplo1.escrever("Mas esse dia ainda não é hoje... =(")