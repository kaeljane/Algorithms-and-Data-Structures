class Pessoa:
    def __init__(self, n, i):
        self._nome = n                      # uma convenção!!
        self._idade = i
    
    @property
    def idade(self):
        return self._idade
    @property
    def nome(self):
        return self._nome
    @idade.setter                           # esse 'idade' é o nome da propriedade que foi definida acima
    def idade(self, nova_idade):
        if nova_idade > 0:
            self._idade = nova_idade 
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome


aluno = Pessoa('Carlos', 19)
print('Nome do Aluno: ', aluno.nome)       # se nao colocar o property e o setter vc so consegue imprimir se colocar aluno._nome
# aluno._idade = -3                        # so vai mudar se colocar aluno._idade = -3

aluno.idade = 10                           # valor so é alterado se for maior que 0.

print('Idade do Aluno: ', aluno.idade)
