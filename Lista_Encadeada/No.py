class No:
    def __init__(self, valor):
        self._valor = valor
        self._prox = None

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


class No_teste:
    def __init__(self, dado):
        self._dado = dado
        self._prox = None
    
    @property
    def dado(self):
        return self._dado
    
    @dado.setter
    def dado(self, dado):
        self._dado = dado
    
    @property
    def prox(self):
        return self._prox

    @prox.setter
    def prox(self, prox):
        self._prox = prox