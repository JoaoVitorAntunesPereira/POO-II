from datetime import datetime
from enum import Enum

class Classificacao():
    def __init__(self,
                 id: int = None,
                 descricao: str = None):

        self._id = id
        self._descricao = descricao
        
        pass
    pass

class Genero(Enum):
    def __init__(self,
                 id: int = None,
                 nome: str = None):

        self._id = id
        self._nome = nome
        
        pass
    pass

class PaisOrigem:
    pass

class Estreia:

    def __init__(self,
                 data: datetime = None,
                 pais: str = None):

        self._data = data
        self._pais = pais

        pass



class Filme:

    def __init__(self,
                 titulo: str = None,
                 ano_producao: int = None,
                 diretor:str = None,
                 estreia: "Estreia" = None,
                 duracao: int = None,
                 classificacao: "Classificacao" = None,
                 genero: list[Genero] = None,
                 paises_origem: list[PaisOrigem] = None,
                 sinopse: str = None):
        
        self._titulo = titulo
        self._ano_producao = ano_producao
        self._diretor = diretor
        self._estreia = estreia 
        self._duracao = duracao
        self._classificacao = classificacao
        self._genero = genero
        self._paises_origem = paises_origem
        self._sinopse = sinopse
        pass
    pass