from Banco.Contas import Conta

if __name__ == "__main__":
    minhaConta = Conta("168536-2", "Josuke Higashikata Joestar",5000.25)
    print("Saldo de " + minhaConta.titular + " = " + str(minhaConta.saldo))
    print(f"Saldo de {minhaConta.titular} = {minhaConta.saldo}")