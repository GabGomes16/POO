#AO IMPRIMIR A LISTA DE ARMAS DO PERSONAGEM, DEPOIS DE IMPRIMIR UM TERMOS DA LISTA ELE IMPRIME "NONE", NÃO CONSEGUIMOS VER O PQ. PEÇO QUE DESCONSIDERE
class Personagem:

    def __init__(self, r, c, n, i):
        self.raca = r
        self.classe = c
        self.nome = n
        self.idade = i
        self.armas = []
    
    def mostrarArma(self, arma):
        self.armas += [arma]
          
    def imprimiarmas(self):
        for i in range(len(self.armas)):
            print(self.armas[i].nomeArma())

    def mostrarPersonagem(self):
        print("RAÇA: {}\nCLASSE: {}\nNOME: {}\nIDADE: {}".format(self.raca, self.classe, self.nome, self.idade))
        self.imprimiarmas()
        print("-------------------")
        

class Arma:
    
    def __init__(self, _categoria, _nome, _magia):
        self.categoria = _categoria
        self.nomedarma = _nome
        self.magia = _magia
     
    def nomeArma(self):
        print(self.nomedarma)
    

persona1 = Personagem("Elfo", "Ranger", "Celebrindal", 125)
persona2 = Personagem("Anão", "Bardo", "Adrik", 60)
persona3 = Personagem("Humano", "Necromante", "Lich", 000)

espada = Arma("Físico", "Espada", False)
cajado = Arma("Mágico", "Cajado", True)
arco = Arma("Distância", "Arco e flechas", False)
faca = Arma("Físico", "Faca", False)
escudo = Arma("Físico", "Escudo", False)

persona1.mostrarArma(arco)
persona1.mostrarArma(faca)
persona1.mostrarPersonagem()

persona2.mostrarArma(espada)
persona2.mostrarArma(escudo)
persona2.mostrarPersonagem()

persona3.mostrarArma(cajado)
persona3.mostrarArma(faca)
persona3.mostrarPersonagem()