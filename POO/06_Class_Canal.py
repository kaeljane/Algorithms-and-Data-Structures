class Canal:
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos
        self.videos = []

    def inscrever(self, quantidade=1):
        self.inscritos += quantidade
    
    def postar(self, video):
        if video in self.videos:
            print("Esse video já foi postado!")
            return
        self.videos.append(video)

class CanalEmpresarial(Canal):
    def __init__(self, nome, descricao, inscritos):
        super().__init__(nome, descricao, inscritos)
        self._equipe = []

    @property
    def equipe(self):
        return self._equipe
    
    def adicionar_membro_equipe(self, membro):
        if membro not in self._equipe:
            self._equipe.append(membro)
        else:
            print(f"O membro {membro} já está na equipe")
    
    def remover_membro_equipe(self, membro):
        if membro in self._equipe:
            self._equipe.remove(membro)
        else:
            print(f"O membro {membro} não está na equipe")

class Video:
    def __init__(self, titulo, descricao):
        self._titulo = titulo
        self._descricao = descricao

        self._visualizacao = 0
        self._likes = 0
        self._deslikes = 0
        self._comentarios = []
        self._data_publicacão = None
    
    def __repr__(self): # para nao imprimir o endereço de memória
        return f"<{self._titulo}>" # para sinalizar que estamos imprimindo um objeto.

    @property
    def nome(self):
        return self._nome
    @property
    def descricao(self):
        return self._descricao
    @property
    def visualizacao(self):
        return self._visualizacao
    @property
    def deslikes(self):
        return self._deslikes
    @property
    def comentarios(self):
        return self._comentarios
    
    @property
    def data_publicacao(self):
        return self._data_publicacão

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @descricao.setter
    def descricao(self, nova_descricao):
        self._descricao = nova_descricao

    @visualizacao.setter
    def visualizacao(self, nova_visualizacao):
        if nova_visualizacao > 0:
            self._visualizacao = nova_visualizacao

    @deslikes.setter
    def deslikes(self, novo_deslike):
        if novo_deslike > 0:
            self._deslikes

    @comentarios.setter
    def comentarios(self, novo_comentario):
        self._comentarios = novo_comentario\

    @data_publicacao.setter
    def data_publicacao(self, data_publicacao):
        self._data_publicacão = data_publicacao

    def assistir(self):
        self._visualizacao += 1;
    
    def gostei(self):
        self._likes += 1

    def nao_gostei(self):
        self._deslikes += 1

    def comentar(self, comentario):
        self._comentarios.append(comentario)

    def data_publicacao(self, data_publicacao):
        self._data_publicacão = data_publicacao

    def info(self):
        print(f"""Título: {self._titulo}
Descrição: {self._descricao}
Data de Publicação: {self._data_publicacão}
{self._visualizacao} Visualizações
{self._likes} Likes {self._deslikes} Deslikes
{self._comentarios} \n""")


if __name__ == "__main__":
    Canal_Lancode = Canal('Lan Code', 'Códigos e gatos', 34000)
    Canal_Guanabara = Canal('Curso em Video', 'Paixão por ensinar', 250000)
    Canal_Duolingo = CanalEmpresarial("Duolingo", "Inglês", 500000)

    # print(f"Membros atuais: {Canal_Duolingo.equipe}")
    # Canal_Duolingo.adicionar_membro_equipe('Pedro')
    # print(f"Membros atuais: {Canal_Duolingo.equipe}")
    # Canal_Duolingo.adicionar_membro_equipe('André')
    # Canal_Duolingo.adicionar_membro_equipe('João')
    # Canal_Duolingo.remover_membro_equipe('Pedro')
    # print(f"Membros atuais: {Canal_Duolingo.equipe}")
    # Canal_Duolingo.remover_membro_equipe('Pedro')
    # 
    
    video_poo = Video('Python objetos', 'Aprenda agora')
    video_discordpy = Video('Aprenda_Discord.py', 'squarecloud')
    

    Canal_Lancode.postar(video_poo)
    Canal_Lancode.postar(video_discordpy)

    print(Canal_Lancode.videos)
    video_poo.data_publicacao("10/10/2025")
    video_discordpy.data_publicacao("11/10/2025")
    video_poo.info()
    video_discordpy.info()