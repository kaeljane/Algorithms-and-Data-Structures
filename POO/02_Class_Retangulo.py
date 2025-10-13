class Retangulo:
    def __init__(self, b, a):
        self.b = b
        self.a = a
    
    def calculo(self):
        return self.b * self.a
    
# main
retangulo1 = Retangulo(10,10)
print(retangulo1.calculo())
print(retangulo1.a)
print(retangulo1.b) 