from No import No

class ListaEncadeada:
    def __init__(self):
        self._inicio = None
        self._tamanho = 0
    
    @property
    def tamanho(self):
        return self._tamanho
    @tamanho.setter
    def tamanho(self, novo_t):
        self._tamanho = novo_t
    # --------------------------------

    def add_inicio(self, valor):
        self._tamanho += 1
        novo_no = No(valor)
        if self._inicio is None:
            self._inicio = novo_no
            return
        
        novo_no.prox = self._inicio
        self._inicio = novo_no

    def add_final(self, valor):
        self._tamanho += 1
        novo_no = No(valor)
        if self._inicio is None:
            self._inicio = novo_no
            return
        
        atual = self._inicio
        while(atual.prox is not None):
            atual = atual.prox
        atual.prox = novo_no
    
    def add_indice(self, ind, valor):
        if ind < 0 or ind > self._tamanho:
            return None
        if ind == 0:
            self.add_inicio(valor)
            return
        if ind == self._tamanho:
            self.add_final(valor)
            return
        atual = self._inicio
        novo_no = No(valor)
        for _ in range (ind - 1):
            atual = atual.prox
        novo_no.prox = atual.prox
        atual.prox = novo_no
        self._tamanho += 1
    # --------------------------------

    def remover(self, ind):
        if ind < 0 or ind >= self._tamanho:
            return None
        self._tamanho -= 1
        if ind == 0:
            self._inicio  = self._inicio.prox
            return
        
        atual = self._inicio
        #vai parar no numero anterior no que queremos
        for _ in range (ind - 1):
            atual = atual.prox
        atual.prox = atual.prox.prox
        
    # --------------------------------
    def exibir(self, ind):
        if ind < 0 or ind >= self._tamanho:
            return None
        if ind == 0:
            return self._inicio.valor
        
        atual = self._inicio
        for _ in range(ind):
            atual = atual.prox
        return atual.valor
    # --------------------------------
    def procurar(self, valor):
        pos = 0
        if self._inicio is None:
            return None
        atual = self._inicio
        while (atual is not None):
            if atual.valor == valor:
                return pos
            atual = atual.prox
            pos += 1
    # --------------------------------
    def modificar(self, ind, valor):
        if self._inicio is None:
            return None
        if ind < 0 or ind >= self._tamanho:
            return None
        if ind == 0:
            self._inicio.valor = valor
            return
    
        # novo_no = No(valor)
        atual = self._inicio
        for _ in range (ind):
            atual = atual.prox
        atual.valor = valor
        # ESSES CODIGOS DE BAIXO SAO CONSIDERADOS UMA MÁ PRÁTICA
        # novo_no.prox = atual.prox.prox
        # atual.prox = novo_no
    # --------------------------------
    def esvaziar(self):
        self._inicio = None
        self._tamanho = 0

    # --------------------------------
    def removeInicio(self):
        if self._inicio is None:
            return "Lista vazia!!"
        self._inicio = self._inicio.prox
        self._tamanho -= 1
    # --------------------------------
    def removeFinal(self):
        if self._inicio is None:
            return "Lista vazia!!"
        if self._tamanho == 1:
            self.esvaziar()
            return
        atual = self._inicio 
        while(atual.prox.prox is not None):
            atual = atual.prox
        atual.prox = None
        self._tamanho -= 1
        # tomar cuidado com as condicoes sempre!!

    # --------------------------------
    def removeOcorrencias(self, valor):
        if self._inicio is None:
            return "Lista vaziaa!!"
        
        atual = self._inicio
        
        while (atual.valor == valor):
            self.removeInicio()
        
        if self._inicio is None:
            return "Lista vaziaa!!"
        
        while(atual.prox is not None ):
            if atual.prox.valor == valor:
                atual.prox = atual.prox.prox
                self._tamanho -= 1
            else:
                atual = atual.prox

        
    # --------------------------------
    def __str__(self):
        r = "["
        atual = self._inicio
        while(atual is not None):
            r += str(atual.valor)
            atual = atual.prox
            if atual is not None:
                r += ", "
        r += "]"
        return r
    