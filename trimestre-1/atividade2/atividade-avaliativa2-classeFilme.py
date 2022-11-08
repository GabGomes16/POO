class Filme:

    def __init__(self, t, d, f):
        self.titulo = t
        self.diretor = d
        self.faixa = f
    
    def escreve(self, filmin):
        print("{}{}!\nDirigido por: {}\nE sua classificação é indicada para maiores de: {} anos.\nFaça um bom proveito filme! =]".format(filmin, self.titulo, self.diretor, self.faixa))

movie1 = Filme("Vingadores: Ultimato", "Joe Russo, Anthony Russo", 13)

movie1.escreve("O filme apresentafo será: ")