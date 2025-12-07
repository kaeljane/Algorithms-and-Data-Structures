class No:
    def __init__(self, dado):
        self._dado = dado
        self._dir = None
        self._esq = None
    # dado ---------------
    @property
    def dado(self):
        return self._dado
    
    @dado.setter
    def dado(self, novo):
        self._dado = novo
    
    # esquerda ---------------
    @property
    def esq(self):
        return self._esq
    
    @esq.setter
    def esq(self, novo):
        self._esq = novo

    # direita ---------------    
    @property
    def dir(self):
        return self._dir
    
    @dir.setter
    def dir(self, novo):
        self._dir = novo
    
    
