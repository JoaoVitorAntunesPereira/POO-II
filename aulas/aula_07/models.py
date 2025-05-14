from datetime import datetime
from enum import Enum

class Classificacao(Enum):
    LIVRE = "Livre para todas as idades"
    IDADE_10 = "Não recomendado para menores de 10 anos"
    IDADE_12 = "Não recomendado para menores de 12 anos"
    IDADE_14 = "Não recomendado para menores de 14 anos"
    IDADE_16 = "Não recomendado para menores de 16 anos"
    IDADE_18 = "Não recomendado para menores de 18 anos"


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

class Pais(Enum):
    MUNDIAL = "Mundial"
    BRASIL = "Brasil"
    CANADA = "Canadá"
    pass

class Estreia:

    def __init__(self,
                 data: datetime = None,
                 pais: Pais = None):

        self._data = data
        self._pais = pais

        pass

class Diretor:
    def __init__(self,
                 nome: str = None):
        
        self.nome = nome
        pass
    pass

class Filme:

    def __init__(self,
                 titulo: str = None,
                 ano_producao: int = None,
                 diretor: "Diretor" = None,
                 estreia: "Estreia" = None,
                 duracao: int = None,
                 classificacao: "Classificacao" = None,
                 genero: list[Genero] = None,
                 paises_origem: list[Pais] = None,
                 sinopse: str = None):
        
        self._titulo = titulo
        self._ano_producao = ano_producao
        self._diretor = diretor
        self._estreia = estreia 
        self._duracao = duracao
        self._classificacao = classificacao
        self._genero = genero if genero else []
        self._paises_origem = paises_origem if paises_origem else []
        self._sinopse = sinopse
        pass
    pass