class ArvoreBinaria:
    def __init__(self):
        self._root = None

    @property
    def root(self):
        return self._root
    
    @root.setter
    def root(self, novo_root):
        self._root = novo_root

    def vazia(self):
        return self._root is None
        
    def buscar(self, p, valor): # p é raiz
        if p is None:
            return None
        if p.dado == valor:
            return p
        no = self.buscar(p.esq, valor)
        if no is None:
            no = self.buscar(p.dir, valor)
        return no
        
    def pre_ordem(self, no):
        if no != None:
            print(no.dado)
            self.pre_ordem(no.esq)
            self.pre_ordem(no.dir)

    def em_ordem(self, no):
        if no != None:
            self.em_ordem(no.esq)
            print(no.dado)
            self.em_ordem(no.dir)

    def pos_ordem(self, no):
        if no != None:
            self.pos_ordem(no.esq)
            self.pos_ordem(no.dir)
            print(no.dado)

            
