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

c1 = Circulo('Vermelho', 5)
q1 = Quadrado('Verde', 10)
c2 = Circulo('Azul', 7)
f1 = Figura('Azul')
print(q1.cor)
print(f"{q1.calcularArea()} m²")

print(f"{c1.calcularArea():.1f} m²")
print(f"{c2.calcularArea():.1f} m²")