def busca_com_transposicao(chave, tabela):
    p = tabela
    q = None
    r = None

    while (p != None and not chave == p.get_registro().get_chave()):
        r = q
        q = p
        p = p.get_proximo()

    if (p == None):
        return None # registro nao encontrado

        # Neste ponto, q aponta para o antecessor imediato
        # de p e r aponta para o antecessor imediato de q

    if (q == None): # registro já é o primeiro da lista
        return p.get_registro() # nao é necessaria a transposicao
    
    q.set_proximo(p.get_proximo())
    p.set_proximo(q)

    if (r == None): # registro encontrado passa a ser o primeiro
        tabela = p
    else:
        r.set_proximo(p)

    return p.get_registro()

        
