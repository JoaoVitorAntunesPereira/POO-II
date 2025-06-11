from filme_repository import FilmeRepository
from filme_obj_models import Filme


class FilmeController:
    def __init__(self):
        self.filme_repository = FilmeRepository()
        
    def listar_filmes(self):
        return self.filme_repository.get_all_filmes()
    
    def buscar_filme_por_id(self, id: int):
        return self.filme_repository.get_filme_by_id(id)
    
    def listar_diretores(self):
        return self.filme_repository.get_all_diretor()
    
    def buscar_diretor_por_id(self, id: int):
        return self.filme_repository.get_diretor_by_id(id)
    
    def listar_classificacoes(self):
        return self.filme_repository.get_all_classificacao()
    
    def buscar_classificacao_por_id(self, id: int):
        return self.filme_repository.get_classificacao_by_id(id)
    
    def listar_paises(self):
        return self.filme_repository.get_all_pais()
    
    def buscar_pais_por_id(self, id: int):
        return self.filme_repository.get_pais_by_id(id)
    
    def listar_generos(self):
        return self.filme_repository.get_all_genero()
    
    def buscar_genero_por_id(self, id: int):
        return self.filme_repository.get_genero_by_id(id)
    
    
    def adicionar_filme(self, filme: Filme):
        self.filme_repository.add_filme(filme)
    
    def editar_filme(self, filme: Filme):
        self.filme_repository.edit_filme(filme)
        
    def excluir_filme(self, filme: Filme):
        self.filme_repository.delete_filme(filme)
