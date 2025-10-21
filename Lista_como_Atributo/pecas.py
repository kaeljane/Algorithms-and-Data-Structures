class Peca:
    def __init__(self, id, nome):
        self._id = id
        self._nome = nome

    @property
    def id(self):
        return self._id
    id.setter
    def id(self, nova_id):
        self._id = nova_id

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    def __str__(self):
        return f"Identificação: {self._id}, Nome: {self._nome}"
    
    