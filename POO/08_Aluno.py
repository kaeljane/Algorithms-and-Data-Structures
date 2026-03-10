class Aluno:
    def __init__(self, matricula, nome, notas):
        self._matricula = str(matricula)
        self._nome = nome
        self._notas = notas
    
    @property
    def nome(self):
        return self._nome 
    
    @property
    def matricula(self):
        if (len(self._matricula) == 7):
            return f"{self._matricula[0:4] }.{self._matricula[4]}.{self._matricula[5:7]}"
        else: 
            return False
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    def media(self):
        soma = 0
        for i in self._notas:
            soma += i
        media = soma/len(self._notas)
        return media
    
    def adicionarNota(self, nota):
        self._notas.append(nota)
    
               

lista = [10, 10, 10]
aluno1 = Aluno(2025145, "kaeljane", lista)

print(aluno1.matricula)
print(aluno1.media())

aluno1.adicionarNota(5)
print(aluno1.media())