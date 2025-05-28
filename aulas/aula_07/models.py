from datetime import datetime
from enum import Enum

class Classificacao(Enum):
    LIVRE = 0
    IDADE_10 = 10
    IDADE_12 = 12
    IDADE_14 = 14
    IDADE_16 = 16
    IDADE_18 = 18


class Genero(Enum):
    ACAO = "Ação"
    AVENTURA = "Aventura"
    COMEDIA = "Comédia"
    DRAMA = "Drama"
    FANTASIA = "Fantasia"
    FICCAO_CIENTIFICA = "Ficção Científica"
    ROMANCE = "Romance"
    SUSPENSE = "Suspense"
    TERROR = "Terror"
    DOCUMENTARIO = "Documentário"
    ANIMACAO = "Animação"
    MUSICAL = "Musical"


class Estreia:

    def __init__(self, data: datetime = None, pais: str = None):
        self._data = data
        self._pais = pais
        self._id = id = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value: datetime):
        self._data = value

    @property
    def pais(self):
        return self._pais

    @pais.setter
    def pais(self, value: str):
        self._pais = value

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value: int):
        self._id = value


class Diretor:

    def __init__(self, nome: str = None):
        self._nome = nome
        self._id = id = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value: str):
        self._nome = value

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value


class Filme:
    def __init__(self, 
                 titulo: str = None, 
                 ano_producao: int = None, 
                 diretor: Diretor = None, 
                 estreia: Estreia = None, 
                 duracao: int = None, 
                 classificacao: Classificacao = None, 
                 genero: set[Genero] = None, 
                 paises_origem: set[str] = None, 
                 sinopse: str = None):
        
        self.titulo = titulo
        self.ano_producao = ano_producao
        self.diretor = diretor
        self.estreia = estreia
        self.duracao = duracao
        self.classificacao = classificacao
        self.genero = genero if genero else set() 
        self.paises_origem = paises_origem if paises_origem else set()
        self.sinopse = sinopse
        self.id = id = None
