def encontrar_indice(chave, chaves):
    for i in range(len(chaves)):
        if (chaves[i] == chave):
            return i
    return -1
