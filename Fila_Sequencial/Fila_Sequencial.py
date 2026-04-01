class FilaSequencial:
    def __init__(self):
        self._fila = []

    def push(self, dado):
        self._fila.append(dado)

    def pop(self):
        return self._fila.pop(0) # remove do início 
    
    def front(self):
        return self._fila[0]
    
    def imprimir(self):
        return self._fila
    
    def size(self):
        return len(self._fila)

    def esvaziar(self):
        self._fila = []
    
fila = FilaSequencial()

fila.push(1)
fila.push(2)
fila.push(3)
fila.push(4)

print(fila.imprimir())
fila.pop()
print(fila.imprimir())
print(fila.front())
print(fila.size())
print(fila.imprimir())
fila.esvaziar()
print(fila.imprimir())
