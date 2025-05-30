from datetime import datetime
from models import Classificacao, Diretor, Estreia, Genero, Filme
from crud import get_diretor_by_name, SessionLocal, map_diretor

# Criando diretores
#diretor1 = Diretor("Christopher Nolan")
#diretor2 = Diretor("Greta Gerwig")
#diretor3 = Diretor("Jordan Peele")
#diretor4 = Diretor("Hayao Miyazaki")
#diretor5 = Diretor("James Cameron")

db = SessionLocal()

diretor1 = map_diretor(get_diretor_by_name(db,"Christopher Nolan"))
diretor2 = map_diretor(get_diretor_by_name(db,"Greta Gerwig"))
diretor3 = map_diretor(get_diretor_by_name(db,"Jordan Peele"))
diretor4 = map_diretor(get_diretor_by_name(db,"Hayao Miyazaki"))
diretor5 = map_diretor(get_diretor_by_name(db,"James Cameron"))

# Criando estreias
estreias_oppenheimer = {
    Estreia(datetime(2023, 7, 21), "Estados Unidos"),
    Estreia(datetime(2023, 7, 22), "Canadá"),
    Estreia(datetime(2023, 7, 20), "Reino Unido")
}

estreias_barbie = {
    Estreia(datetime(2023, 7, 20), "Reino Unido"),
    Estreia(datetime(2023, 7, 21), "Estados Unidos")
}

estreias_nos = {
    Estreia(datetime(2019, 3, 22), "Estados Unidos"),
    Estreia(datetime(2019, 3, 28), "Brasil")
}

estreias_chihiro = {
    Estreia(datetime(2001, 7, 20), "Japão")
}

estreias_avatar = {
    Estreia(datetime(2009, 12, 10), "Reino Unido"),
    Estreia(datetime(2009, 12, 18), "Estados Unidos"),
    Estreia(datetime(2009, 12, 25), "Brasil")
}

# Criando filmes
filme1 = Filme(
    titulo="Oppenheimer",
    ano_producao=2023,
    diretor=diretor1,
    estreia=estreias_oppenheimer,
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
    estreia=estreias_barbie,
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
    estreia=estreias_nos,
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
    estreia=estreias_chihiro,
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
    estreia=estreias_avatar,
    duracao=162,
    classificacao=Classificacao.IDADE_12,
    genero={Genero.AVENTURA, Genero.FICCAO_CIENTIFICA},
    paises_origem={"Estados Unidos"},
    sinopse="Um ex-fuzileiro naval se envolve com os nativos de Pandora em uma luta pela sobrevivência e equilíbrio ambiental."
)

# Conjunto com todos os filmes
dados_filmes = {filme1, filme2, filme3, filme4, filme5}
