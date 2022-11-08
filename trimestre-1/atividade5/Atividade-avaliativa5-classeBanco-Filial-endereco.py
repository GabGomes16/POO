class Banco:

    def __init__(self,_nome, _codigo):
        self.nome = _nome
        self.codigo = _codigo
        self.filiais = []
    
    def addFilial(self, _agencia, Logradouro, Log_Nome, Numero, Bairro, Cep):
        self.filiais += [Filial(_agencia, Logradouro, Log_Nome, Numero, Bairro, Cep)]

    def ver_filiais(self):
        for i in range(len(self.filiais)):
            print("Banco: "+ self.nome + " - Agencia: " + self.filiais[i].agencia + "\nEndereço: ", end="")
            self.filiais[i].endereco.imprimiEndereco()
            print("---------------")


class Filial:

    def __init__(self, _agencia, Logradouro, Log_Nome, Numero, Bairro, Cep):
        self.endereco = Endereco(Logradouro, Log_Nome, Numero, Bairro, Cep)
        self.agencia = _agencia


class Endereco:

    def __init__(self, Logradouro, Log_Nome, Numero, Bairro, Cep):
        self.logradouro = Logradouro
        self.nome = Log_Nome
        self.numero = Numero
        self.bairro = Bairro
        self.cep = Cep
    
    def imprimiEndereco(self):
        print(self.logradouro + " "+ self.nome + ", " + self.numero + ", " + self.bairro + "." + self.cep + ".")

Banco_do_Brasil = Banco("Banco do Brasil", "0001")
Bradesco = Banco("Bradesco", "0111")

Banco_do_Brasil.addFilial("2022","Rua", "Padre Pedro Pinto", "1010", "Venda Nova","31550-000")
Banco_do_Brasil.addFilial("1011", "Rua", "Nova Esperança", "12", "São João Batista","31660-000")

Bradesco.addFilial("555","Rua", "Jovino Rodrigues Pedo", "140", "Mantiqueira","31550-000")
Bradesco.addFilial("6666","Rua", "Taiobeiras", "169", "Sevilha","33858-480")

Banco_do_Brasil.ver_filiais()
Bradesco.ver_filiais()