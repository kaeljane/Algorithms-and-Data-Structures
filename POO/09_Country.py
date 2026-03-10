class Country:
    def __init__(self, nome, capital, dimensao):
        self._nome = nome
        self._capital = capital
        self._dimensao = dimensao
        self._vizinhos = []
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def capital(self):
        return self._capital
    
    @property
    def dimensao(self):
        return self._dimensao
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @capital.setter
    def capital(self, capital):
        self._capital = capital
    
    @dimensao.setter
    def dimensao(self, dimensao):
        self._dimensao = dimensao
        
    def adicionarVizinho(self, vizinho):
        self._vizinhos.append(vizinho)
        
    def imprimirVizinhos(self):
        print(self._vizinhos)
    
    def __str__(self):
        return f"{self._nome} {self._capital} {self._dimensao}km²" 
    
    
pais1 = Country("aleatorio", "al", 100)

pais1.adicionarVizinho("al2")
pais1.adicionarVizinho("al3")
pais1.adicionarVizinho("al4")
pais1.adicionarVizinho("al5")
pais1.adicionarVizinho("al6")

pais1.imprimirVizinhos()
print(pais1)

