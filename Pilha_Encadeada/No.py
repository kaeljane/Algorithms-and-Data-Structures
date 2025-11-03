class No:
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
