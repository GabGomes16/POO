class Carteira:
    def __init__(self, investimento):
        self.__investimento = investimento
        self.__listaContas = []

    @property
    def investimento(self):
        return self.__investimento

    @investimento.setter
    def investimento(self, investimento):
        self.__investimento = investimento

    @property
    def listaContas(self):
        return self.__listaContas

    def addConta(self, objetoConta):
        if len(self.__listaContas) == 3:
            print("Não é possivel ter mais de 3 contas!")
        else:
            self.__listaContas.append(objetoConta)
        '''
        recebe o parâmetro 'objetoConta' e o adiciona à lista de contas desde que não haja mais de 3 item na lista
        '''

    def retornaConta(self):
        for continha in self.__listaContas:
            if continha != None:
                if continha == []:
                    return f"Essa carteira {self.__investimento} não possui contas cadastradas!\n"
                else:
                    return f"A carteira {self.__investimento} possui as contas:\n{continha.retornaDados()}"
        '''
        retorna em forma de texto as contas existentes na '__listaContas' na posição continha desde que essa conta não tenha o valor 'None'. 
        Caso não haja contas na lista é exibido uma mensagem
        '''

    def contasNegativas():
        listaNegativas = []
        for continha in self.__listaContas:
            if continha.saldo < 0:
                listaNegativas += [continha]
        if len(listaNegativas) == 0:
            print("Nenhuma conta está negativa nessa carteira!")
        return listaNegativas
        '''
        caso uma conta na '__listaContas' esteja com o saldo negativo, esta conta é adicionada à lista.
        caso não haja contas negativas é exibido uma mensagem
        '''

class Conta:
    def __init__(self, numero, nome, valor):
        self.__numero = numero
        self.__titular = nome
        self.__saldo = valor
    
    def conta(self):
        pass

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

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Não foi possivel alterar o saldo!")
        else:
            self.__saldo = saldo

    def sacar (self, valor):
        if valor > self.__saldo:
            print("Não foi possível sacar esse valor!")
        else:
            self.__saldo -= valor
        '''
        recebe como parametro o valor do saque e caso este seja maior do que o saldo, é mostrado uma mensagem mostrando a impossibilidade do saque
        caso contrário, é retornado a subtração do saldo pelo valor do saque
        '''

    def depositar(self, valor):
        if valor < 0:
            print("Não foi possível realizar o depósito!")
        else:
            self.__saldo += valor
        '''
        recebe como parametro o valor do depósito e caso este seja menor do que 0, é mostrado uma mensagem mostrando a impossibilidade do depósito
        caso contrário, é retornado a soma do saldo pelo valor do depósito
        '''    

    def retornaDados(self):
        return f"Número: {self.__numero}\nNome do Titular: {self.__titular}\nSaldo da conta: {str(self.__saldo)}\n\n"
        '''
        retorna os dados: numero da conta, titular, e saldo em forma de texto
        '''

class ContaCorrente(Conta):

    contador = 0

    def __init__(self, numero, nome, valor):
        super().__init__(numero, nome, valor)
        self.__limite = 2000
        ContaCorrente.contador += 1

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        if limite < 0:
            print("Não foi possivel alterar o limite!")
        else:
            self.__limite = limite

    def saldoTotal(self):
        return self.saldo + self.__limite
        '''
        retorna o saldo total sendo esse a soma do saldo atual com o limite 
        '''

    def sacar(self, valor):
        if valor > self.saldoTotal():
            print("Não foi possível sacar esse valor!")
        else:
            if valor <= self.saldo:
                self.saldo -= valor
            else:
                self.limite = valor - self.saldo
        '''
        recebe como parametro o valor do saque e caso este seja maior do que o saldo total, é mostrado uma mensagem mostrando a impossibilidade do saque
        caso contrário, se o valor do saque for maior que o saldo o saldo recebe a diferença do saldo pelo valor do saque
        senão o limite recebe a diferença entre o valor e o saldo
        '''
    
    def retornaDados(self):
        return f"Número: {self.numero}\nNome do Titular: {self.titular}\nSaldo da conta: {str(self.saldo)}\n\n"
        '''
        retorna os dados: numero da conta, titular, e saldo em forma de texto
        '''

class ContaPoupanca (Conta):
    def __init__(self, numero , nome, valor, rendimento):
        super().__init__(numero, nome, valor)
        self.__rendimento = rendimento

    @property
    def rendimento(self):
        return self.__rendimento

    @rendimento.setter
    def rendimento(self, rendimento):
        if rendimento < 0:
            print("Não foi possivel alterar a taxa de rendimento!")
        else:
            self.__rendimento = rendimento

    def acaoRendimento(self):
        self.saldo *= self.__rendimento
        '''
        retorna o rendimento sendo esse, o produto do saldo com o valor do rendimento
        '''
    
    def retornaDados(self):
        return f"Número: {self.numero}\nNome do Titular: {self.titular}\nSaldo da conta: {str(self.saldo)}\nRendimento: {str(self.__rendimento)}\n\n"
        '''
        retorna os dados: numero da conta, titular, saldo, e rendimento em forma de texto
        '''