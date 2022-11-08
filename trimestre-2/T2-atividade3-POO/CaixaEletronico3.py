from Contas2 import *
from clientes import *
import os

def MensagemInicial():
    print ("\033[1;33;40mBem-vindo ao  Bank POOdle – Fazendo cachorrada com sua grana\nPois você investe com classe, mas é tratado como objeto!\n\033[1;37;40m")
    opcao = int(input("(1) Cadastrar uma novo cliente\n(2) Pesquisar por um cliente existente\n(3) Sair\n\n> "))
    return opcao

def cadastrarcliente():
    pessoa = int(input("(1) Pessoa Física\n(2) Pessoa Jurídica\n(3) Voltar\n\n> "))
    cliente = None
    if pessoa == 1:
        nome = input("Digite seu nome: ")
        data = input("Digite sua data de nascimento: ")
        ende = input("Digite seu endereço: ")
        cpf = input("Digite seu CPF: ")
        cliente = PesssoaFisica(nome, data, ende, cpf)
        listaClientes.append(cliente)
        print("Cadastrado!")
        return pessoa
    elif pessoa == 2:
        nome = input("Digite seu nome: ")
        data = input("Digite sua data de nascimento: ")
        ende = input("Digite seu endereço: ")
        cnpj = input("Digite seu CNPJ: ")
        cliente = PessoaJuridica(nome, data, ende, cnpj)
        listaClientes.append(cliente)
        print("Cadastrado!")
        return pessoa
    elif pessoa == 3:
        return pessoa
    else:
        print("Opção inválida!")
        return pessoa
    
def pesquisarCliente():
    achou = False
    documento = input("Digite o número do seu documento:\n> ")
    for listinha in listaClientes:
        if listinha.documento == documento:
            print("\n",listinha.retornaCliente(documento),"\n")
            achou = True
            return listinha
    if not achou:
        print("Esse cliente não existe!\n")

def cadastrarCarteira(objCliente, opcao):
    if opcao == 1:
        inv = input("Qual o tipo de invertimento?\n> ")
        car = Carteira(inv)
        objCliente.addCarteira(car)
        return car

def cadastrarConta(objCarteira, objCliente, opcao):
    cont = opcao
    if cont == 1:
        num = input("Informe o numero da conta: ")
        tit = str(objCliente.nome)
        sal = float(input("Qual o valor do saldo inicial?\n> "))
        tip = int(input("(1) Conta Comum\n(2) Conta Corrente\n(3) Conta Poupança\n> "))
        if tip == 1:
            conta = Conta(num, tit, sal)
        elif tip == 2:
            conta = ContaCorrente(num, tit, sal)
        elif tip == 3:
            ren = float(input("Qual o rendimeto mensal?\n> "))
            conta = ContaPoupanca(num, tit, sal, ren)
        else:
            print("Opção inválida!!")
            return
            
        objCliente.addCarteira(objCarteira.addConta(conta))
        print(f"Cadastro na carteira {objCarteira.investimento} realizado com sucesso!\n")

listaClientes = []

if __name__ == "__main__":
    sair = False
    while not sair:
        os.system("cls" if os.name == "nt" else "clear")
        opcao = MensagemInicial()
        if opcao == 3:
            os.system("cls" if os.name == "nt" else "clear")
            break
        while opcao != 3:
            if opcao == 1:
                os.system("cls" if os.name == "nt" else "clear")
                op = cadastrarcliente()
                input()
                if op == 3:
                    pass
                break
                os.system("cls" if os.name == "nt" else "clear")
            elif opcao == 2:
                os.system("cls" if os.name == "nt" else "clear")
                cli = pesquisarCliente()
                if cli != None:
                    while True:
                        x = int(input("(1) Criar uma nova carteira\n(2) Voltar\n> "))
                        if x == 1:
                            cart = cadastrarCarteira(cli,1)
                            cadastrarConta(cart, cli, 1)
                            break
                        elif x == 2:
                            break
                        else:
                            print("Opção inválida!!")
                        break
                break
            elif opcao == 3:
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print("Opção inválida!!\n")
    print("Volte sempre ao Bank POOdle!")