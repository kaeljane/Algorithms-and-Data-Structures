class Aluno:
    def __init__(self, nome, matricula, idade):
        self.n = nome
        self.m = matricula
        self.i = idade
    
# main

# criando o objeto aluno
kaeljane = Aluno("Kaeljane Ferreira da Silva", 202514320008, 20)

print(kaeljane.n)
print(kaeljane.m)
print(kaeljane.i)