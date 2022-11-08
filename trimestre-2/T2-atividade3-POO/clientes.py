class Cliente:
    def __init__(self, nome, dataNascimento, endereco):
        self.__nome = nome
        self.__dataN = dataNascimento
        self.__endereco = endereco   

    @property
    def nome(self):
        return self.__nome
    
    @property
    def dataN(self):
        return self.__dataN
    
    @property
    def endereco(self):
        return self.__endereco

class PesssoaFisica(Cliente):
    def __init__(self, nome, dataNascimento, endereco, CPF):
        super().__init__(nome, dataNascimento, endereco)
        self.__documento = CPF
        self.__listaCarteiras = []
    
    @property
    def documento(self):
        return self.__documento

    @property
    def listaCarteiras(self):
        return self.__listaCarteiras

    def addCarteira(self, objCarteira):
        self.__listaCarteiras.append(objCarteira)
        '''
        recebe o parâmetro 'objCarteira' e o adiciona à lista de carteiras
        '''

    def retornaCliente(self, CPF):
        if CPF == self.__documento:
            if len(self.__listaCarteiras) == 0:
                return f"Cliente {self.nome} não possui carteiras!"
            else:
                return f"Cliente {self.nome} tem as carteiras:\n{self.imprimeListaCarteira()}"
        '''
        recebe o parâmetro 'CPF', verifica se o cpf recebido equivale ao CPF do cliente e, caso a resposta for sim,
        é retornado os dados da carteira do cliente a partir da função "imprimeListaCarteiras()", caso não haja é mostrado uma mensagem avisando
        '''

    def imprimeListaCarteira(self):
        '''
        retorna os dados da lista na posição 'carteirinha' desde que o valor dela não seja "None"
        '''
        for carteirinha in self.__listaCarteiras:
            if carteirinha != None:
                yield f"{carteirinha.retornaConta()}"

    def maiorLegal():
        pass
                
class PessoaJuridica(Cliente):
    def __init__(self, nome, dataNascimento, endereco, CNPJ):
        super().__init__(nome, dataNascimento, endereco)
        self.__documento = CNPJ
        self.__listaCarteiras = []
    
    @property
    def documento(self):
        return self.__documento

    @property 
    def listaCarteiras(self):
        return self.__listaCarteiras

    def addCarteira(self, objCarteira):
        self.__listaCarteiras.append(objCarteira)
        '''
        recebe o parâmetro 'objCarteira' e o adiciona à lista de carteiras
        '''

    def retornaCliente(self, CNPJ):
        if CNPJ == self.__documento:
            if len(self.__listaCarteiras) == 0:
                return f"Cliente {self.nome} não possui carteiras!"
            else:
                return f"Cliente {self.nome} tem as carteiras:\n{self.imprimeListaCarteira()}"
        '''
        recebe o parâmetro 'CNPJ', verifica se o cnpj recebido equivale ao CNPJ do cliente e, caso a resposta for sim,
        é retornado em forma de texto os dados da carteira do cliente a partir da função "imprimeListaCarteiras()".
        Caso não haja carteiras na lista, é exibido uma mensagem
        '''
    
    def imprimeListaCarteira(self):
        '''
        retorna os dados da lista na posição 'carteirinha' desde que o valor dela não seja "None"
        '''
        for carteirinha in self.__listaCarteiras:
            if carteirinha != None:
                return carteirinha.retornaConta() 

    def tipoSociedade():
        pass