class Conta:
    def __init__ (self, numero, nome, valor):
        self.__numero = numero 
        self.__titular = nome
        self.__saldo = valor

    @property
    def numero(self):
        return self.__numero    

    @property
    def titular(self):
        partesNomes = self.__titular.split(" ")       
        tamanho = len(partesNomes)
        return partesNomes[0] + " " + partesNomes[tamanho-1]

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def saldo(self):
        return self.__saldo 

    def sacar(self, valor):
        if (valor < self.saldo):
            print("Não foi possível sacar esse valor!")
        else:
            self.__saldo -= valor

    def depositar(self, valor):
        if (valor < 0):
            print("Não foi possível realizar o depósito!")
        else:
            self.__saldo += valor                    