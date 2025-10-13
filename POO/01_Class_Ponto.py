class Ponto:
    def __init__(self, x, y):    #construtor
        self.x = x               # atributos do objeto Ponto
        self.y = y

    def quadrante(self):
        if (self.x > 0 and self.y > 0):
            return "1 quadrante"
        elif (self.x < 0 and self.y > 0):
            return "2 quadrante"
        elif (self.x < 0 and self.y < 0):
            return "3 quadrante"
        elif (self.x > 0 and self.y < 0):
            return "4 quadrante"

ponto1 = Ponto(1, 2)
ponto2 = Ponto(5, 5)
ponto3 = Ponto(5, -3)

print(f'Coordenadas do Ponto 1 ({ponto1.x} {ponto1.y})')
print(f'Coordenadas do Ponto 2 ({ponto2.x} {ponto2.y})')

print(ponto1, ponto2)

print(ponto1.quadrante())
print(ponto2.quadrante())
print(ponto3.quadrante())