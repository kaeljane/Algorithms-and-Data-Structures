from No import No

class ListaEncadeada:
    def __init__(self):
        self._inicio = None
        self._tamanho = 0

    def consultar_inicio(self):
        if self._inicio is None:
            return None
        else:
            return self._inicio
    
    def consultar_final(self):
        if self._inicio is None:
            return None
        else:
            atual = self._inicio
            while (atual.prox is not None):
                atual = atual.prox
            return atual
        
    def consultar_indice(self, indice):
        if indice < 0 or indice >= self._tamanho:
            return None
        else:
            atual = self._inicio
            for i in range (indice):
                atual = atual.prox
            return atual
        
    def adicionar_inicio(self, valor):
        self._tamanho +=1
        novo_no = No(valor)
        novo_no.prox = self._inicio
        self._inicio = novo_no
        
    def adicionar_final(self, valor):
        self._tamanho += 1
        novo_no = No(valor)
        if self._inicio is None:
             self._inicio = novo_no
             return
        
        atual = self._inicio
        while(atual.prox is not None): 
            atual = atual.prox
        atual.prox = novo_no

    def adicionar_indice(self, valor):
        ...

