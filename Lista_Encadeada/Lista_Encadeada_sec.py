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
            return atual.valor
        
    def consultar_indice(self, indice):
        if indice < 0 or indice >= self._tamanho:
            return None
        else:
            atual = self._inicio
            for i in range (indice):
                atual = atual.prox
            return atual.valor
        
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
        
        atual = self._inicio # vai receber o primeiro valor da lista
        while(atual.prox is not None): 
            atual = atual.prox
        atual.prox = novo_no

    def adicionar_indice(self, indice, valor):
        if indice < 0 or indice > self._tamanho:
            return None
        self._tamanho += 1
        if indice == 0: #add no inicio
            self._adicionar_inicio(valor) #chamanado outra função para fazer o trabalho
            return
        
        if indice == self._tamanho:
            self._adicionar_final(valor) #nao adicione o No!!! na funcao ja cria o No
            return
        novo_no = No(valor)
        # caso realmente seja no meio
        atual = self._inicio # vai receber o primeiro valor da lista
        for i in range(indice - 1): # pegar o indíce anterior 
            atual = atual.prox # relação de ponteiros
        novo_no.prox = atual.prox #novo No aponta para o que o anterior apontava
        atual.prox = novo_no 

    def remover_inicio(self):
        if self._inicio is None:
            return None
        self._tamanho -= 1
        atual = self._inicio 
        self._inicio = atual.prox

    def remover_fim(self):
        # 1 Caso - Não existe items na lista
        if self._inicio is None:
            return None
        # 2 Caso - Só um item na lista
        if self._inicio.prox is None: # ou seja só tem um elemento na lista | irá remover o primeiro elemento
            self.remover_inicio()
            return
            # self._inicio = self._inicio.prox ou isso

        # 3 Caso - Varios items na lista
        self._tamanho -= 1
        atual = self._inicio
        while (atual.prox.prox is not None): # vai paarar exatamente no penultimo
            atual = atual.prox
        atual.prox = None

    def remover_indice(self, indice):
        # 3 casos possiveis...
        if indice < 0 or indice >= self._tamanho:  # prestar atenção nisso!!
            return None
        
        if indice == 0:
            self.remover_inicio()
            return
        
        if indice == self._tamanho - 1: # se esquecer disso ta lascada!!
            self.remover_fim()
            return
        
        atual = self._inicio
        for _ in range (indice - 1):
            atual = atual.prox
        # se eu fizer algo precipitado posso perder o restante da lista
        atual.prox = atual.prox.prox
        self._tamanho -= 1
    
    def __str__(self):
        atual = self._inicio
        resposta = "["
        
        while(atual is not None):
            resposta += str(atual.valor)
            atual = atual.prox
            if atual is not None:
                resposta += ", "
        resposta += "]"
        return resposta

# if __name__ == "__main__":
    # lista1 = ListaEncadeada()
    # lista1.adicionar_final("kay")
    # lista1.adicionar_final("kay")
    # lista1.adicionar_final("kay")
    # lista1.adicionar_inicio("Code")
    # lista1.adicionar_indice(2, "Forces")
    # lista1.remover_fim()
    # lista1.consultar_final()

    # print(lista1)