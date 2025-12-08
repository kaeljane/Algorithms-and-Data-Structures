class Dado:
    def __init__(self):
        self._chave = None
        self._indice = None

        # Informações do Registro
        # getters e setters...

class No:
    def __init__(self, dado):
        self._dado = dado
        self._esquerda = None
        self._direita = None

        # getters e setters...

def criar_arvore_de_busca(chaves):
    arvore = None
    p = None
    q = None
    item = Dado()

    item.set_chave(chaves[0]) # recebe a primeira chave do vetor
    item.set_indice(0)
    arvore = No(item)

    for i in range(1, len(chaves)): # executa o for a partir do indice 1
        p = q = arvore

        while (chaves[i] != p.get_dado().get_cahve() and q != None):
            p = q
            if (chaves[i] < p.get_dado().get_chave()):
                q = p.get_esquerda()
            else:
                q = p.get_direita()

        item = Dado()
        item.set_chave(chaves[i])
        item.set_indice(i)

        q = No(item)
        if (chaves[i] < p.get_dado().get_chave()):
            p.set_esquerda(q)
        else:
            p.set_direita(q)

    return arvore

def encontrar_indiceA(chave, arvore):
    p = arvore
    while(p != None and chave != p.get_dado().get_chave()):
        if (chave < p.get_dado().get_chave()):
            p = p.get_esquerda()
        else:
            p = p.get_direita()
    
    return p.get_dado().get_indice() if (p != None) else -1

