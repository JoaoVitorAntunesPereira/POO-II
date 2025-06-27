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

class Pais(Enum):
    BRASIL = "Brasil"
    EUA = "Estados Unidos"
    CANADA = "Canadá"
    FRANCA = "França"
    ALEMANHA = "Alemanha"
    REINO_UNIDO = "Reino Unido"
    JAPAO = "Japão"



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
                 genero: set[Genero] = None,
                 paises_origem: set[str] = None,
                 sinopse: str = None):

        self.titulo = titulo
        self.ano_producao = ano_producao
        self.diretor = diretor
        self.data_estreia = data_estreia
        self.pais_estreia = pais_estreia
        self.duracao = duracao
        self.classificacao = classificacao
        self.genero = genero if genero else set()
        self.paises_origem = paises_origem if paises_origem else set()
        self.sinopse = sinopse
        self.id = id = None
