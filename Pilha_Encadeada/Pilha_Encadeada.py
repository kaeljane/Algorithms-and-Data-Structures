from No import No

class PilhaEncadeada:
    def __init__(self):
        self._topo = None
        self._tamanho = 0
    
    @property
    def topo(self):
        # verificar se estar vazia OK
        if self.vazia():
            print("A pilha está vazia!!")
        else:
            return self._topo.dado
    
    def vazia(self):
        return self._tamanho == 0
    
    def tamanho(self):
        return self._tamanho
    
    def inserir(self, novoDado):
        # não tem erro
        no = No(novoDado)
        no.prox = self._topo
        self._topo = no
        self._tamanho += 1

    def remover(self):
        # verificar se a lista está vazia
        if self.vazia():
            print("A pilha está vazia!!")
        else:
            self._topo  = self._topo.prox

    def __str__(self):
        resposta = "["
        atual = self._topo
        while (atual != None):
            resposta += str(atual.dado)
            atual = atual.prox
            if atual != None:
                resposta += ", "
        resposta += "]"
        return resposta
    
    def imprimir(self):
        print(self.__str__())

    def modificar(self, dado):
        if self.vazia():
            print("A pilha está vazia!!")
        else:
            self._topo.dado = dado

if __name__ == "__main__":
    p = PilhaEncadeada()
    p.inserir(10) # 4
    p.inserir(20) # 3
    p.inserir(30) # 2
    p.inserir(40) # 1

    p.imprimir()    # [40, 30, 20, 10] -> ind [3, 2, 1, 0]
    print(p)        #  t   
                    #  t.prox 
                    #  t.prox.prox 
                    #  t.prox.prox.prox
    p.remover()
    print(p)        #  [30, 20, 10]
    p.remover()
    print(p)        #  [20, 10]