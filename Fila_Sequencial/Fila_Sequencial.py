class FilaException:
    def __init__(self, mensagem):
        super.__init__(mensagem)

class FilaSequencial:
    def __init__(self):
        self._dados = []

    def vazio(self):
        return len(self._dados) == 0
    
    def tamanho(self):
        return len(self._dados)
    
    #seria o topo da pilha
    def inicio(self):
        if self.vazio():
            raise FilaException('A fila está vazia')
        return self._dados[0]
    
    def inserir(self, dado):
        self._dados.append(dado)
    
    def remover(self):
        if self.vazio():
            raise FilaException('A fila está vazia')
        return self._dados.pop(0) # retornar???

    def __str__(self):
        return self._dados.__str__()
    
    def imprimir(self): # chama o proprio metodo str da classe
        print(self.__str__()) 

if __name__ == '__main__':
    f = FilaSequencial()
    # for i in range (1, 6):
    #     f.inserir(i*10)

    # print(f)
    try:
        f.remover()
    except FilaException as fe: #tem algum erro aqui
        print(fe)
    # f.remover()
    # print(f)
    print(f)