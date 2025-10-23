import No

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
    
    def consultar_inicio(self):
        if self._inicio is None:
            return None
        else:
            return self._inicio

    def consultar_final():
        pass
    def consultar_indice():
        pass
    def adicionar_inicio(self, valor):
        self._tamanho+=1
        if self._inicio is None:
            self._inicio = No(valor)
            return
        
        novo_no = No(valor)
        novo_no.proximo = self._inicio
        self._inicio = novo_no

    def adicionar_final(self):
        self._tamanho+=1
        pass
    def adicionar_indice(self):
        self._tamanho+=1
        pass

    