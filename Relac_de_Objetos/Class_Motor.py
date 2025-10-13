class Motor:
    def __init__(self, motorizacao, combustivel = 'flex'):
        # caso vc nao coloque algum valor em combustivel ele será automaticamente flex. Nao tem obrig de colocar!
        self._motorizacao = motorizacao # indicou para o programador nao chamar diretamente
        self._combustivel = combustivel

    @property
    def motorizacao(self):
        return self._motorizacao
    
    @motorizacao.setter
    def motorizacao(self, nova_motorizacao):
        self._motorizacao = nova_motorizacao
    
    # para evitar que imprima o endereço de memória
    def __str__(self):
        return f"Motor: {self._motorizacao}L, Combustível: {self._combustivel}"

if __name__ == "__main__":
    motor1 = Motor(2.0)
    print(motor1.motorizacao)
    print(motor1._combustivel) # nao vai funcionar pq nao foi defindo 
    print(motor1)
