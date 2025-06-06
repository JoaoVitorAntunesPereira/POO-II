from filme_repository import FilmeRepository
from filme_db_models import tb_classificacao

fr =FilmeRepository()

paises = fr.get_all_pais()
generos = fr.get_all_genero()
classificacoes = fr.get_all_classificacao()
diretores = fr.get_all_diretor()
filmes = fr.get_all_filmes()

for p in paises:
    print(p.descricao)

print("-------------------------")
for g in generos:
    print(g.descricao)

print("-------------------------")
for c in classificacoes:
    print(c.descricao)

print("-------------------------")
for d in diretores:
    print(d.nome)

print("-------------------------")

for f in filmes:
    print("="*40)
    print(f"Título: {f.titulo}")
    print(f"Ano de Produção: {f.ano_producao}")
    print(f"Duração: {f.duracao} minutos")
    
    if f.data_estreia:
        print(f"Data de Estreia: {f.data_estreia.strftime('%d/%m/%Y')}")
    
    if f.diretor:
        print(f"Diretor: {f.diretor.nome}")
    
    if f.classificacao:
        print(f"Classificação: {f.classificacao.descricao}")
    
    if f.pais_estreia:
        print(f"País de Estreia: {f.pais_estreia.nome}")
    
    if f.generos:
        print("Gêneros:")
        for g in f.generos:
            print(f" - {g.descricao}")
    
    if f.paises_origem:
        print("Países de Origem:")
        for p in f.paises_origem:
            print(f" - {p.descricao}")
    
    if f.sinopse:
        print("Sinopse:")
        print(f.sinopse)

    print("="*40)
    print()

    



    
    