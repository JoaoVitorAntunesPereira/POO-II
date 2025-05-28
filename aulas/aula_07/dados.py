from datetime import datetime
from models import Classificacao, Diretor, Estreia, Genero, Filme

# Criando diretores
diretor1 = Diretor("Christopher Nolan")
diretor2 = Diretor("Greta Gerwig")
diretor3 = Diretor("Jordan Peele")
diretor4 = Diretor("Hayao Miyazaki")
diretor5 = Diretor("James Cameron")

# Criando estreias
estreia1 = Estreia(datetime(2023, 7, 21), "Estados Unidos")
estreia2 = Estreia(datetime(2023, 7, 20), "Reino Unido")
estreia3 = Estreia(datetime(2019, 3, 22), "Estados Unidos")
estreia4 = Estreia(datetime(2001, 7, 20), "Japão")
estreia5 = Estreia(datetime(2009, 12, 18), "Estados Unidos")

# Criando filmes
filme1 = Filme(
    titulo="Oppenheimer",
    ano_producao=2023,
    diretor=diretor1,
    estreia=estreia1,
    duracao=180,
    classificacao=Classificacao.IDADE_14,
    genero={Genero.DRAMA, Genero.SUSPENSE},
    paises_origem={"Estados Unidos", "Reino Unido"},
    sinopse="A história do físico J. Robert Oppenheimer e sua contribuição para o desenvolvimento da bomba atômica."
)

filme2 = Filme(
    titulo="Barbie",
    ano_producao=2023,
    diretor=diretor2,
    estreia=estreia2,
    duracao=114,
    classificacao=Classificacao.IDADE_12,
    genero={Genero.COMEDIA, Genero.FANTASIA},
    paises_origem={"Estados Unidos"},
    sinopse="Barbie vive em Barbieland até ser expulsa por ser uma boneca de aparência imperfeita. Ela parte para o mundo real."
)

filme3 = Filme(
    titulo="Nós",
    ano_producao=2019,
    diretor=diretor3,
    estreia=estreia3,
    duracao=116,
    classificacao=Classificacao.IDADE_16,
    genero={Genero.TERROR, Genero.SUSPENSE},
    paises_origem={"Estados Unidos"},
    sinopse="Uma família enfrenta sua versão sombria em uma trama cheia de simbolismos e suspense psicológico."
)

filme4 = Filme(
    titulo="A Viagem de Chihiro",
    ano_producao=2001,
    diretor=diretor4,
    estreia=estreia4,
    duracao=125,
    classificacao=Classificacao.LIVRE,
    genero={Genero.FANTASIA, Genero.ANIMACAO},
    paises_origem={"Japão"},
    sinopse="Uma jovem garota se vê presa em um mundo mágico e precisa encontrar coragem para resgatar seus pais e voltar ao mundo real."
)

filme5 = Filme(
    titulo="Avatar",
    ano_producao=2009,
    diretor=diretor5,
    estreia=estreia5,
    duracao=162,
    classificacao=Classificacao.IDADE_12,
    genero={Genero.AVENTURA, Genero.FICCAO_CIENTIFICA},
    paises_origem={"Estados Unidos"},
    sinopse="Um ex-fuzileiro naval se envolve com os nativos de Pandora em uma luta pela sobrevivência e equilíbrio ambiental."
)


dados_filmes = {filme1, filme2, filme3, filme4, filme5}