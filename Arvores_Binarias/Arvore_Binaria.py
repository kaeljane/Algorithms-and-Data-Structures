class ArvoreBinaria:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root
    
    @root.setter
    def root(self, novo_root):
        self._root = novo_root
    
    def em_ordem(self, no):
        if no != None:
            self.em_ordem(no.esq)
            print(no.dado)
            self.em_ordem(no.dir)

    def pre_ordem(self, no):
        if no != None:
            print(no.dado)
            self.pre_ordem(no.esq)
            self.pre_ordem(no.dir)

    def pos_ordem(self, no):
        if no != None:
            self.pos_ordem(no.esq)
            self.pos_ordem(no.dir)
            print(no.dado)

            