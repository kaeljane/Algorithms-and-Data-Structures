from Pilha_Sequencial import PilhaSequencial

nome = input("Digite o nome: ")

pilha = PilhaSequencial()
pilhaAux = PilhaSequencial()

for i in nome:
    pilha.empilhar(i)

for i in range(len(nome) - 1, len(nome) // 2 - 1, -1):
    if (len(nome) % 2 != 0 and i == len(nome) // 2):
        pilha.desempilhar()
    else:
        pilhaAux.empilhar(pilha.desempilhar())
        
print(pilha.imprimir())
print(pilhaAux.imprimir())

if (pilha.imprimir() == pilhaAux.imprimir()):
    print("É palindromo")
else: 
    print("Não é palindromo")
