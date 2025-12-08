def busca_e_insere(chave, chaves, registros):
    for i in range(len(chaves)):
        if (chaves[i] == chave):
            return i;

    chaves.append(chave)
    recebe_registros(registros) # nao entendi essa linha

    return len(chaves)
