class Conta:

    def __init__(self, cliente, numero, saldo):
        self.cliente = cliente
        self.saldo = saldo
        self.numero = numero
        self.operacoes = []
        self.extrato = []
        self.limite = []

    def info(self):
        print('Cliente.: ' + self.cliente)
        print('Saldo...: ' + str(self.saldo))
        print('Numero..: ' + str(self.numero))
        #print('Extrato.: ' + str(self.extrato))
        print('******************************')

class Corrente(Conta):
    def __init__(self, cliente, numero, saldo):
        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo
        super().__init__(cliente, numero, saldo)
        #print('Conta')

class Poupanca(Conta):
    def __init__(self, cliente, numero, saldo):
        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo
        super().__init__(cliente, numero, saldo)
        #print('Conta')

class Investimento(Conta):
    def __init__(self, cliente, numero, saldo):
        self.cliente = cliente
        self.numero = numero
        self.saldo = saldo
        super().__init__(cliente, numero, saldo)
        #print('Conta')

print()

c1=Corrente('Carlos Silva', 123-4, 152)
c2=Poupanca('Natalia Borges', 321-4, 150)
c3=Investimento('Dian Carla', 351-4, 210)

c1.info()
c2.info()
c3.info()

if __name__ == '__main__':

    def deposito(self, valor):
        self.saldo += valor
        self.extrato.Conta('+ Deposito:' + str(valor))
        print(valor)

    def saque(self, valor=0):
        if valor <= self.limite + self.saldo:
            self.saldo -= valor
            self.operacoes.append(["Saque", valor])
        else:
            print('Saldo Insuficiente')

    def pode_sacar(self, valor):
        return self.saldo >= valor

    def extrato(self):
        print("numero: \n saldo:".format(self.numero, self.saldo))

class Cliente(Conta):
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco