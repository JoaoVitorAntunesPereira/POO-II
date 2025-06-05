from datetime import datetime
from filme_obj_models import Classificacao, Diretor, Genero, Filme, Pais
from filme_controller import FilmeController
from filme_repository import FilmeRepository

filme_repository = FilmeRepository()

# Lista de países para dropdown, etc
paises = [p.value for p in Pais]

# Criando diretores
diretor1 = Diretor(filme_repository.get_diretor_by_id(1))
diretor2 = Diretor(filme_repository.get_diretor_by_id(2))
diretor3 = Diretor(filme_repository.get_diretor_by_id(3))
diretor4 = Diretor(filme_repository.get_diretor_by_id(4))
diretor5 = Diretor(filme_repository.get_diretor_by_id(5))

# Criando filmes
filme1 = Filme(
    titulo="Oppenheimer",
    ano_producao=2023,
    diretor=diretor1,
    data_estreia=datetime(2023, 7, 21),
    pais_estreia=Pais.EUA.value,
    duracao=180,
    classificacao=Classificacao.IDADE_14,
    genero={Genero.DRAMA, Genero.SUSPENSE},
    paises_origem={Pais.EUA.value, Pais.REINO_UNIDO.value},
    sinopse="A história do físico J. Robert Oppenheimer e sua contribuição para o desenvolvimento da bomba atômica."
)

filme2 = Filme(
    titulo="Barbie",
    ano_producao=2023,
    diretor=diretor2,
    data_estreia=datetime(2023, 7, 20),
    pais_estreia=Pais.REINO_UNIDO.value,
    duracao=114,
    classificacao=Classificacao.IDADE_12,
    genero={Genero.COMEDIA, Genero.FANTASIA},
    paises_origem={Pais.EUA.value},
    sinopse="Barbie vive em Barbieland até ser expulsa por ser uma boneca de aparência imperfeita. Ela parte para o mundo real."
)

filme3 = Filme(
    titulo="Nós",
    ano_producao=2019,
    diretor=diretor3,
    data_estreia=datetime(2019, 3, 22),
    pais_estreia=Pais.EUA.value,
    duracao=116,
    classificacao=Classificacao.IDADE_16,
    genero={Genero.TERROR, Genero.SUSPENSE},
    paises_origem={Pais.EUA.value},
    sinopse="Uma família enfrenta sua versão sombria em uma trama cheia de simbolismos e suspense psicológico."
)

filme4 = Filme(
    titulo="A Viagem de Chihiro",
    ano_producao=2001,
    diretor=diretor4,
    data_estreia=datetime(2001, 7, 20),
    pais_estreia=Pais.JAPAO.value,
    duracao=125,
    classificacao=Classificacao.LIVRE,
    genero={Genero.FANTASIA, Genero.ANIMACAO},
    paises_origem={Pais.JAPAO.value},
    sinopse="Uma jovem garota se vê presa em um mundo mágico e precisa encontrar coragem para resgatar seus pais e voltar ao mundo real."
)

filme5 = Filme(
    titulo="Avatar",
    ano_producao=2009,
    diretor=diretor5,
    data_estreia=datetime(2009, 12, 18),
    pais_estreia=Pais.EUA.value,
    duracao=162,
    classificacao=Classificacao.IDADE_12,
    genero={Genero.AVENTURA, Genero.FICCAO_CIENTIFICA},
    paises_origem={Pais.EUA.value},
    sinopse="Um ex-fuzileiro naval se envolve com os nativos de Pandora em uma luta pela sobrevivência e equilíbrio ambiental."
)

# Atribuindo IDs manualmente
filme1.id = 1
filme2.id = 2
filme3.id = 3
filme4.id = 4
filme5.id = 5

# Lista de filmes
dados_filmes = [filme1, filme2, filme3, filme4, filme5]
