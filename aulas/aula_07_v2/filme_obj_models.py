from datetime import datetime
from typing import Optional, Set

class EntidadeSimples:
    def __init__(self, descricao: str):
        self.descricao = descricao
        self.id = None

class Genero(EntidadeSimples):
    pass

class Classificacao(EntidadeSimples):
    pass

class Pais(EntidadeSimples):
    pass


class Diretor:
    def __init__(self, nome: str = None):
        self.nome = nome
        self.id = None

class Filme:
    def __init__(self, 
                 titulo: str = None, 
                 ano_producao: int = None, 
                 diretor: Diretor = None, 
                 data_estreia: datetime = None,
                 pais_estreia: Pais = None, 
                 duracao: int = None, 
                 classificacao: Classificacao = None, 
                 generos: Optional[Set[Genero]] = None, 
                 paises_origem: Optional[Set[Pais]] = None, 
                 sinopse: str = None):
        
        self.titulo = titulo
        self.ano_producao = ano_producao
        self.diretor = diretor
        self.data_estreia = data_estreia
        self.pais_estreia = pais_estreia
        self.duracao = duracao
        self.classificacao = classificacao
        self.generos = set(generos) if generos else set()
        self.paises_origem = set(paises_origem) if paises_origem else set()
        self.sinopse = sinopse
        self.id = None
