from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from filme_db_models import (
    Base,
    tb_pais,
    tb_diretor,
    tb_classificacao,
    tb_genero,
    tb_filme,
    tb_filme_genero,
    tb_filme_pais_origem
)


# Criação do banco de dados em memória ou em arquivo
engine = create_engine("sqlite:///filmes.db")  # Altere para PostgreSQL/MySQL se quiser
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# 1. Inserir Países
paises = {
    "EUA": tb_pais(nome="EUA"),
    "REINO_UNIDO": tb_pais(nome="Reino Unido"),
    "JAPAO": tb_pais(nome="Japão"),
}
#session.add_all(paises.values())

# 2. Inserir Diretores
diretores = {
    1: tb_diretor(nome="Christopher Nolan"),
    2: tb_diretor(nome="Greta Gerwig"),
    3: tb_diretor(nome="Jordan Peele"),
    4: tb_diretor(nome="Hayao Miyazaki"),
    5: tb_diretor(nome="James Cameron"),
}
#session.add_all(diretores.values())

# 3. Inserir Classificações
classificacoes = {
    "LIVRE": tb_classificacao(descricao="Livre"),
    "IDADE_12": tb_classificacao(descricao="12 anos"),
    "IDADE_14": tb_classificacao(descricao="14 anos"),
    "IDADE_16": tb_classificacao(descricao="16 anos"),
    "IDADE_18": tb_classificacao(descricao="18 anos"),
}
#session.add_all(classificacoes.values())

# 4. Inserir Gêneros
generos = {
    "DRAMA": tb_genero(descricao="Drama"),
    "SUSPENSE": tb_genero(descricao="Suspense"),
    "COMEDIA": tb_genero(descricao="Comédia"),
    "FANTASIA": tb_genero(descricao="Fantasia"),
    "TERROR": tb_genero(descricao="Terror"),
    "ANIMACAO": tb_genero(descricao="Animação"),
    "AVENTURA": tb_genero(descricao="Aventura"),
    "FICCAO_CIENTIFICA": tb_genero(descricao="Ficção Científica"),
}
#session.add_all(generos.values())
#session.commit()

# Helper para buscar objetos
def get_pais(nome): return next(p for p in paises.values() if p.nome == nome)
def get_genero(desc): return next(g for g in generos.values() if g.descricao == desc)
def get_classificacao(desc): return next(c for c in classificacoes.values() if c.descricao == desc)

# 5. Inserir Filmes
filmes = [
    tb_filme(
        titulo="Oppenheimer",
        ano_producao=2023,
        data_estreia=datetime(2023, 7, 21),
        duracao=180,
        is_active=True,
        diretor=diretores[1],
        classificacao=get_classificacao("14 anos"),
        pais_estreia=get_pais("EUA"),
        generos=[get_genero("Drama"), get_genero("Suspense")],
        sinopse="A história de J. Robert Oppenheimer, o físico teórico que liderou o Projeto Manhattan e desenvolveu a primeira bomba atômica durante a Segunda Guerra Mundial."
    ),
    tb_filme(
        titulo="Barbie",
        ano_producao=2023,
        data_estreia=datetime(2023, 7, 20),
        duracao=114,
        is_active=True,
        diretor=diretores[2],
        classificacao=get_classificacao("12 anos"),
        pais_estreia=get_pais("Reino Unido"),
        generos=[get_genero("Comédia"), get_genero("Fantasia")],
        sinopse="Em Barbieland, tudo é perfeito — até que Barbie começa a questionar sua existência e parte para o mundo real em uma jornada de autoconhecimento e empoderamento."
    ),
    tb_filme(
        titulo="Nós",
        ano_producao=2019,
        data_estreia=datetime(2019, 3, 22),
        duracao=116,
        is_active=True,
        diretor=diretores[3],
        classificacao=get_classificacao("16 anos"),
        pais_estreia=get_pais("EUA"),
        generos=[get_genero("Terror"), get_genero("Suspense")],
        sinopse="Uma família é aterrorizada por seus duplos durante uma viagem de férias, revelando um mistério perturbador sobre identidade e sociedade."
    ),
    tb_filme(
        titulo="A Viagem de Chihiro",
        ano_producao=2001,
        data_estreia=datetime(2001, 7, 20),
        duracao=125,
        is_active=True,
        diretor=diretores[4],
        classificacao=get_classificacao("Livre"),
        pais_estreia=get_pais("Japão"),
        generos=[get_genero("Fantasia"), get_genero("Animação")],
        sinopse="Chihiro, uma garota de 10 anos, entra em um mundo mágico governado por espíritos, onde precisa resgatar seus pais e encontrar coragem para crescer."
    ),
    tb_filme(
        titulo="Avatar",
        ano_producao=2009,
        data_estreia=datetime(2009, 12, 18),
        duracao=162,
        is_active=True,
        diretor=diretores[5],
        classificacao=get_classificacao("12 anos"),
        pais_estreia=get_pais("EUA"),
        generos=[get_genero("Aventura"), get_genero("Ficção Científica")],
        sinopse="Em Pandora, um ex-fuzileiro se infiltra entre os Na'vi através de um avatar e se vê dividido entre sua missão e a defesa de um novo mundo."
    )
]


session.add_all(filmes)
session.commit()

# 6. Inserir Países de origem (relacionamento N:N)
filmes_paises_origem = {
    "Oppenheimer": ["EUA", "Reino Unido"],
    "Barbie": ["EUA"],
    "Nós": ["EUA"],
    "A Viagem de Chihiro": ["Japão"],
    "Avatar": ["EUA"]
}

for filme in filmes:
    for nome_pais in filmes_paises_origem[filme.titulo]:
        session.add(tb_filme_pais_origem(filme_id=filme.filme_id, pais_id=get_pais(nome_pais).pais_id))

session.commit()
session.close()
