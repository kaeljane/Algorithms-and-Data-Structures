from No import No
from Exercicio_1_Lista_Encadeada import ListaEncadeada


lista = ListaEncadeada()
while(True):
    print(lista)
    print("Editor de Listas")
    print("-"*24)
    print("1 - Tamanho")
    print("2 - Inserir")
    print("3 - Remover")
    print("4 - Exibir Elemento")
    print("5 - Procurar valor")
    print("6 - Modificar")
    print("7 - Esvaziar")
    print("8 - Sair")
    a = int(input("Digite sua opção: "))
    
    # tamanho
    if a == 1:
        print(lista.tamanho)
    
    # inserir elemento
    elif a == 2:
        b = int(input("Número: "))
        ba = input("Onde você quer inserir?(inicio | indice | final)")
        if ba == "inicio":
            lista.add_inicio(b)
        elif ba == "indice":
            ind = int(input("Indice: "))
            lista.add_indice(ind, b)
        elif ba == "final":
            lista.add_final(b)

    # remover elemento
    elif a == 3:
        c = int(input("Posição: "))
        lista.remover(c)
    
    # Exibir elementos
    elif a == 4:
        d = int(input("Posição: "))
        print(lista.exibir(d)) #sacanagem alterar depois
    
    # Procurar valor
    elif a == 5:
        e = int(input("Valor: "))
        #imprimir o valor que está no índice
        print(lista.procurar(e))
    
    # Modificar
    elif a == 6:
        f = int(input("Indice a ser modificado: "))
        g = int(input("Valor a ser colocado: "))
        lista.modificar(f, g)
    
    elif a == 7:
        lista.esvaziar()
    # sair 
    elif a == 8:
        break