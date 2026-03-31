def hash_code(matricula, tamanhoTabela):

    # pega os dois últimos digitos da matricula
    dezena = int(matricula[6:8])
    
    # Pega o último digito da matricula
    unidade  = int(matricula[7:8])

    numero = dezena + unidade 

    if tamanhoTabela > 0:
        return (numero %  tamanhoTabela)
    else:
        return -1
