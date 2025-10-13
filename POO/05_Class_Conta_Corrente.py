class Conta_Corrente:
    def __init__(self, n, s):
        self._nome = n
        self._saldo = s
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def saldo(self):
        return self._saldo
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @saldo.setter
    def saldo(self, novo_saldo):
        self._saldo = novo_saldo

    def deposito(self, deposito): 
        self._saldo += deposito

    def retirada(self, retirada):
        if (self._saldo - retirada >= 0):
            self._saldo -= retirada

if __name__ == "__main__":
    #main
    conta1 = Conta_Corrente("Kaeljane Ferreira", 1000)

    print(conta1) # endereço de memória 
    print(conta1.nome) # nome do dono da conta
    print(conta1.saldo) # saldo da conta
    conta1.deposito(10) # saldo -> 1010
    print(conta1.saldo) # saldo da conta
    conta1.retirada(100) # saldo -> 910
    print(conta1.saldo) # saldo da conta

