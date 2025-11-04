from No import No
from Arvore_Binaria import ArvoreBinaria

if __name__ == "__main__":
    arvore = ArvoreBinaria()
    
    arvore.root = No("A")
    arvore.root.esq = No("B")
    arvore.root.dir = No("C")

    p = arvore.root.esq
    q = arvore.root.dir

    p.esq = No("D")
    p.dir = No("E")

    q.esq = No("F")
    q.dir = No("G")

    arvore.em_ordem(arvore.root)