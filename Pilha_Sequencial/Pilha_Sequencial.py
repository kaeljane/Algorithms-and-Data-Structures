class PilhaSequencial:
    def __init__(self):
        self._pilha = []

    def vazio(self):
        return len(self._pilha) == 0 
    
    def tamanho(self):
        return len(self._pilha)
    
    def topo(self):
        return self._pilha[len(self._pilha) - 1]
    
    # nunca dar erro
    def empilhar(self, dado):
        self._pilha.append(dado)
    
    def desempilhar(self):
        if len(self._pilha) > 0:
            return self._pilha.pop()
    
    def __str__(self):
        return self._pilha.__str__()
    
    def imprimir(self):
        return self._pilha

teste = PilhaSequencial()

teste.empilhar(1)
teste.empilhar(2)
teste.empilhar(3)
print(teste.imprimir())
teste.desempilhar()
print(teste.imprimir())
print(teste.topo())