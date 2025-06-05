
from filme_repository import FilmeRepository


class FilmeController:
    def __init__(self):
        self.filme_repository = FilmeRepository()
        
    def listar_filmes(self):
        return self.filme_repository.get_filmes()
    
    def listar_diretores(self):
        return self.filme_repository.get_all_diretor()
    
    def listar_classificacoes(self):
        return self.filme_repository.get_all_classificacao()
    
    