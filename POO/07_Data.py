class Data:
    def __init__(self, dia, mes, ano):
        self._dia = dia
        self._mes = mes
        self._ano = ano
    
    @property
    def dia(self):
        return self._dia
    
    @property
    def mes(self):
        return self._mes
    
    @property
    def ano(self):
        return self._ano
    
    @dia.setter
    def dia(self, dia):
        self._dia = dia
    
    @mes.setter
    def mes(self, mes):
        self._mes = mes
    
    @ano.setter
    def ano(self, ano):
        self._ano = ano

    def __str__(self):
        return f"{self._dia}/{self._mes}/{self._ano}"
    

data1 = Data(17, 11, 2004)

print(data1)