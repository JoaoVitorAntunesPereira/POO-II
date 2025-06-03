from nicegui import ui, app
from filme_obj_models import Diretor, Estreia, Filme, Genero, Classificacao
from datetime import datetime
from dados import dados_filmes, diretor1, diretor2, diretor3, diretor4, diretor5

generos = [genero.value for genero in Genero]
classificacoes = []

filmes = list(dados_filmes)


def classificacao_to_text():
    for c in Classificacao:
        if c.value == 0:
            text = "Livre"
            classificacoes.append(text)
        else:
            text = "Proibido para menores de " + str(c.value)
            classificacoes.append(text)

def classificacao_map(classificacao: str):
    classificacao_mapa = {
        "Livre": Classificacao.LIVRE,
        "Proibido para menores de 10": Classificacao.IDADE_10,
        "Proibido para menores de 12": Classificacao.IDADE_12,
        "Proibido para menores de 14": Classificacao.IDADE_14,
        "Proibido para menores de 16": Classificacao.IDADE_16,
        "Proibido para menores de 18": Classificacao.IDADE_18
    }
    
    return classificacao_mapa.get(classificacao, None)




classificacao_to_text()

@ui.page("/cadastrar-filme")
def cadastrar_filme():

    estreias: list[Estreia] = []

    def data_lancamento_func():
        with ui.input('Date') as date:
            with ui.menu().props('no-parent-event') as menu:
                with ui.date().bind_value(date):
                    with ui.row().classes('justify-end'):
                        ui.button('Fechar', on_click=menu.close).props('flat')
            with date.add_slot('append'):
                ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')
        return date

    with ui.row():
        with ui.column():
            ui.label("Cadastrar Filme").classes(replace='text-lg')

            titulo = ui.input(label="Título")
            ano_producao = ui.number(label="Ano de produção", min=1900, max=datetime.now().year)
            diretor = ui.input(label="Diretor")
            duracao = ui.number(label="Duração (minutos)")
            sinopse = ui.textarea(label="Sinopse")
            ui.label("Países de Origem (separados por vírgula)")
            paises_origem = ui.input(label="Países de origem")

            # ESTREIAS
            ui.label("Adicionar Estreias").classes('text-base text-gray-700')
            estreia_pais = ui.input(label="País de estreia")
            estreia_data = data_lancamento_func()

            def adicionar_estreia():
                nova_estreia = Estreia(data=estreia_data.value, pais=estreia_pais.value)
                estreias.append(nova_estreia)
                ui.notify(f"Estreia adicionada: {nova_estreia.pais} - {nova_estreia.data}", type='positive')

            ui.button("Adicionar Estreia", on_click=adicionar_estreia).props('outline')

        with ui.column():
            ui.label("Classificação indicativa")
            classificacao_radio = ui.radio(classificacoes, value=classificacoes[0])

            ui.label("Gêneros")
            generos_select = ui.select(generos, multiple=True, value=generos[0], label='comma-separated').classes('w-64')

            def enviar_filme():
                titulo_value = titulo.value
                ano_producao_value = ano_producao.value
                diretor_value = diretor.value
                duracao_value = duracao.value
                sinopse_value = sinopse.value
                paises_origem_value = paises_origem.value.split(',') 
                classificacao_value = classificacao_radio.value

                diretor_obj = Diretor(nome=diretor_value)
                classificacao_obj = Classificacao(classificacao_map(classificacao_value))

                
                generos_valores = set(Genero(g) for g in generos_select.value)

                filme = Filme(
                    titulo=titulo_value,
                    ano_producao=ano_producao_value,
                    diretor=diretor_obj,
                    estreia=set(estreias),
                    duracao=duracao_value,
                    classificacao=classificacao_obj,
                    genero=generos_valores,
                    paises_origem=set(paises_origem_value),
                    sinopse=sinopse_value
                )

                filmes.append(filme)
                ui.notify(f'Filme "{filme.titulo}" cadastrado com sucesso!', type='positive')

            ui.button("Cadastrar Filme", on_click=enviar_filme)

@ui.page("/listar")
def listar():
    if filmes:
        dados_tabela = []

        for filme in filmes:
            generos_text = ', '.join(g.value for g in filme.genero)
            paises_origem_text = ', '.join(filme.paises_origem)
            classificacao_text = (
                "Livre" if filme.classificacao == Classificacao.LIVRE
                else f"Proibido para menores de {filme.classificacao.value}"
            )

            estreias_text = '\n'.join(
                f"{e.data.strftime('%d/%m/%Y')} ({e.pais})" if isinstance(e.data, datetime) else f"{e.data} ({e.pais})"
                for e in filme.estreia
            )


            dados_tabela.append({
                "Título": filme.titulo,
                "Ano": filme.ano_producao,
                "Diretor": filme.diretor.nome,
                "Classificação": classificacao_text,
                "Gêneros": generos_text,
                "Origem": paises_origem_text,
                "Estreias": estreias_text,
                "Duração (min)": filme.duracao,
                "Sinopse": filme.sinopse
            })

        colunas = [
            {'name': 'Título', 'label': 'Título', 'field': 'Título', 'align': 'left'},
            {'name': 'Ano', 'label': 'Ano', 'field': 'Ano', 'align': 'left'},
            {'name': 'Diretor', 'label': 'Diretor', 'field': 'Diretor', 'align': 'left'},
            {'name': 'Classificação', 'label': 'Classificação', 'field': 'Classificação', 'align': 'left'},
            {'name': 'Gêneros', 'label': 'Gêneros', 'field': 'Gêneros', 'align': 'left'},
            {'name': 'Origem', 'label': 'Países de Origem', 'field': 'Origem', 'align': 'left'},
            {'name': 'Estreias', 'label': 'Estreias', 'field': 'Estreias', 'align': 'left'},
            {'name': 'Duração (min)', 'label': 'Duração', 'field': 'Duração (min)', 'align': 'left'},
            {'name': 'Sinopse', 'label': 'Sinopse', 'field': 'Sinopse', 'align': 'left'},
        ]

        ui.table(columns=colunas, rows=dados_tabela, row_key='Título').classes('w-full')
    else:
        ui.label("A lista de filmes está vazia.")

#ui.run()




if __name__ == "__main__":
    from rich import print
    from filme_controller import FilmeController

    filme_controller = FilmeController()
    
    for filme in filme_controller.listar_filmes():
        print("Título: " + filme.titulo)
    
    
    # Initialize Database
    #test_create_movie() # teste de inserção de um filme
    #test_delete_movie(1)
    
    #db = SessionLocal() # db == database == banco de dados
    #filme = crud.get_filme(db, filme_id=2)
    #filme.titulo = "Avatar updated"
    #crud.update_filme(db, filme)

    #def test_add_filme():
    #    db = SessionLocal()
#
    #    for filme in filmes:
    #        add_filme(db, filme)
#
    #def test_list_filmes():
    #    db = SessionLocal()
    #    
    #    for filme in get_filmes(db):
    #        print("Titulo: " + filme.titulo)
#
    #def test_add_diretores():
    #    db = SessionLocal()
    #    add_diretor(db, diretor1)
    #    add_diretor(db, diretor2)
    #    add_diretor(db, diretor3)
    #    add_diretor(db, diretor4)
    #    add_diretor(db, diretor5)

    #test_add_diretores()


    #test_add_filme()

    ##test_list_filmes() # select all

    #print(results)
    
