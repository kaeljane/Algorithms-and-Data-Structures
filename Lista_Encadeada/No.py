class No:
    def __init__(self, valor):
        self._valor = valor
        self.prox = None
    
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor (self, valor):
        self._valor = valor

    @property
    def prox(self):
        return self._prox
    
    @prox.setter
    def prox(self, prox):
        self._prox = prox