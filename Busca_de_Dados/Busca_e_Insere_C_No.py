def busca_e_insere2(chave, chaves, tabela):
    p = tabela
    q = None
    r = None

    i = 0
    while (p != None):
        q = p
        if (chaves[i] == chave):
            return p.get_registro() # analisar isso ...
        i += 1
        p = p.get_proximo()

    # Insere o novo registro caso nao tenha encontrado

    r = No()
    recebe_registro(r)
    r.set_proximo(None)

    if (tabela == None):
        tabela = r
    else:
        q.set_proximo(r)
    
    return r.get_registro()

