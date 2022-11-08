import abc
import math

class Figura(abc.ABC):
    def __init__(self, cor):
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @abc.abstractmethod
    def calcularArea(self):
        pass

    @abc.abstractmethod
    def retornaDados(self):
        pass

class Circulo(Figura):
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.__raio = raio

    @property
    def raio(self):
        return self.__raio

    @raio.setter
    def raio(self, raio):
        self.__raio = raio

    def calcularArea(self):
        return math.pi * (self.__raio ** 2)
    
    def retornaDados(self):
        return "Círculo " + self.cor + " com raio " + str(self.__raio)

class Quadrado(Figura):
    def __init__(self, cor, lado):
        super().__init__(cor)
        self.__lado = lado

    @property
    def lado(self):
        return self.__lado

    @lado.setter
    def lado(self, lado):
        self.__lado = lado

    def calcularArea(self):
        return self.__lado ** 2

    def retornaDados(self):
        return "Quadrado " + self.cor + " com lado " + str(self.__lado)

figuras = {}
numFigura = 1
print("CADAASTRO DE FIGURAS\n")
resposta = input("Deseja cadastrar uma figura? (s/n) ")
while resposta in ["s", "S"]:
    tipoFigura = int(input("Qual figura? (1 para Círculo 2 para Quadrado) "))
    corFigura = input("Informe a cor da figura: ")
    if tipoFigura == 1:
        while True:
            try:
                medida = float(input("Qual o valor do raio? "))
                figuras['c' + str(numFigura)] = Circulo(corFigura, medida)
                numFigura += 1
                break
            except ValueError:
                print("Valor inválido! Digite um número real!")
    elif tipoFigura == 2:
        while True:
            try:
                medida = float(input("Qual o valor do lado? "))
                figuras['c' + str(numFigura)] = Quadrado(corFigura, medida)
                numFigura += 1
                break
            except ValueError:
                print("Valor inválido! Digite um número real!")
    else:
        print("Figura inválida! =/")
    resposta = input("Deseja cadastrar uma figura? (s/n) \n\n")

for chave in figuras:
    print(figuras[chave].retornaDados())
    print(f"Área{figuras[chave].calcularArea()} m²", end="\n\n")