class Carro:
    def __init__(self, cor, placa, pecas=[]):
        self._cor = cor
        self._placa = placa
        self._pecas = pecas

    def get_pecas(self):
        return self._pecas
    def set_pecas(self, novas_pecas):
        self._pecas = novas_pecas
    
    def add_peca(self, nova_peca):
        self._pecas.append(nova_peca)

    def __str__(self):
        for i in range(len(self._pecas)):
            saida = saida + f'{self._pecas[i]}' + ' '

        return f"Cor: {self._cor}, Placa: {self._placa}, Peças => {saida}"
