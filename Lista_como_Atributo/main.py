from novo_carro import Carro
from pecas import Peca

if __name__ == "__main__":
    pecas = []
    p1 = Peca('1', 'chassi')
    p2 = Peca('2', 'volante')
    p3 = Peca('3', 'dicos de freio')

    pecas.append(p1)
    pecas.append(p2)
    pecas.append(p3)

    carro = Carro('verde', 'ABC-1234', pecas)

    print(carro) # possui 3 objetos
    carro.add_peca(Peca('4', 'filtro de ar'))
    # print(carro.get_pecas()[3]) # possui 4 objetos
    print(carro)