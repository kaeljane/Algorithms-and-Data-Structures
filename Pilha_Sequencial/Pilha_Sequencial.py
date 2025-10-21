class PilhaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class PilhaSequencial:
    def __init__(self):
        self._dados = []

    def vazio(self):
        return len(self._dados) == 0 # retorna True or False
    
    def tamanho(self):
        return len(self._dados)
    
    def topo(self):
        if self.vazio():
            raise PilhaException("A pilha está vazia")
        return self._dados[0]
    
    def inserir(self, dado):
        self._dados.insert(0, dado)
    
    def remover(self):
        if self.vazio():
            raise PilhaException("A pilha está vazia")
        return self._dados.pop(0)
    
    def __str__(self):
        return self._dados.__str__()
    
    def imprimir(self):
        print(self.__str__())

if __name__ == '__main__':
    p = PilhaSequencial()

    # for i in range(1, 6):
    #     p.inserir(i*10)

    # print(p)
    # print(p.imprimir())

    # p.remover()
    # print(p)

    try:
        p.remover()
    except PilhaException as pe: # pe seria um nome qualquer, apenas uma variavel.
        print(pe)
    
    print(p)