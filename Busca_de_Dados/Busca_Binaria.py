def encontrar_indice_binaria(chave, chaves):
    limiteInf = 0
    limiteSup = len(chaves) - 1
    metade = 0

    while (limiteInf <= limiteSup):
        metade = (limiteInf + limiteSup)//2
        if (chaves[metade] == chave):
            return metade
        if (chave < chaves[metade]):
            limiteSup = metade - 1
        else:
            limiteInf = metade + 1
    
    return - 1