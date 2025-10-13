from Class_Motor import Motor 

class Carro:
    def __init__(self, cor, placa, motor):
        self._cor = cor
        self._placa = placa
        self._motor = motor

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, nova_cor):
        self._cor = nova_cor

    def __str__(self):
        return f"Cor: {self._cor}, Placa: {self._placa}, Motor: {self._motor}"
    
if __name__ == "__main__":
    motor = Motor(1.8, 'gasolina')
    carro = Carro('preto', 'ABC-1234', motor)

    print(carro)