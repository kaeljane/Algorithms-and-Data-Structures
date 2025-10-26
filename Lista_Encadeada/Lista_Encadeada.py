from No import No

class ListaEncadeada:
    def __init__(self):
        self._inicio = None
        self._tamanho = 0
    @property
    def inicio(self):
        return self._inicio
    
    @inicio.setter
    def inicio(self, valor):
        self._inicio = valor
    
    @property
    def tamanho(self):
        return self._tamanho
    
    @tamanho.setter
    def tamanho(self, tamanho):
        self._tamanho = tamanho
    
    # def consultar_inicio(self):
    #     if self._inicio is None:
    #         return None
    #     else:
    #         return self._inicio
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
            return atual.prox

    def consultar_final(self):
        if self._inicio is None:
            return None
        atual = self._inicio
        while (atual.prox is not None):
            atual = atual.prox
        return atual.prox # lembrar de sempre imprimir o valor que seria esse atual.prox
        
    def consultar_indice(self, posicao):
        if self._inicio is None:
            return None
        # para evitar erros
        if posicao < 1 or posicao > self._tamaho:
            return
        #atual andará na lista
        atual = self.inicio
        for _ in range(posicao - 2):
            atual = atual.prox
        return atual.prox

    def adicionar_inicio(self, valor):
        self._tamanho+=1
        if self._inicio is None:
            self._inicio = No(valor)
            return
        
        # caso já tenha algum elemento na lista
        novo_no = No(valor)
        novo_no.prox = self._inicio
        self._inicio = novo_no

    def adicionar_final(self, valor):
        self._tamanho+=1

        if self._inicio is None:
            self._inicio = No(valor)
            return
        
        # caso já tenha algum elemento na lista
        atual = self._inicio
        # vai fazer um loop até o final depois add no final o valor
        while (atual.prox is not None):
            atual = atual.prox
        atual.prox = No(valor)

    def adicionar_indice(self, posicao, valor):
        self._tamanho+=1
        # começa a contar do 1
        if self._inicio is None and posicao == 1:
            # add no inicio da lista
            self._inicio = No(valor)
            return
        # para evitar erros
        if posicao < 1 or posicao > self._tamanho:
            return
        
        atual = self._inicio
        # vai percorrer a listag
        for _ in range(posicao - 2):
            atual = atual.prox 
        novo_no = No(valor) #recebendo o no
        novo_no.prox = atual.prox  # agora o prox do novo No vai receber None
        atual.prox = novo_no # o None atual receberá o Valor no novo No, e depois dele terá um prox com valor None

    def __str__(self):
            p = self._inicio
            string = ""
            while(p != None):
                string += p.valor
                p = p.prox
            return string    
        
#-----------------------------
if __name__ == "__main__":
    lista = ListaEncadeada()
    lista.adicionar_final("A")
    lista.adicionar_final("B")
    lista.adicionar_final("B")
    lista.adicionar_final("B")
    lista.adicionar_final("B")
    

    print(lista)
        


        
    