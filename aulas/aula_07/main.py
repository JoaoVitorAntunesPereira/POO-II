from nicegui import ui
from models import Diretor, Filme, Genero, Classificacao, Pais
from datetime import datetime, date
from dados import dados_filmes, paises

generos = [genero.value for genero in Genero]
classificacoes = []
filmes = list(dados_filmes)


def classificacao_to_text():
    for c in Classificacao:
        if c.value == 0:
            text = "Livre"
        else:
            text = f"Proibido para menores de {c.value}"
        classificacoes.append(text)


def classificacao_map(classificacao: str):
    mapa = {
        "Livre": Classificacao.LIVRE,
        "Proibido para menores de 10": Classificacao.IDADE_10,
        "Proibido para menores de 12": Classificacao.IDADE_12,
        "Proibido para menores de 14": Classificacao.IDADE_14,
        "Proibido para menores de 16": Classificacao.IDADE_16,
        "Proibido para menores de 18": Classificacao.IDADE_18
    }
    return mapa.get(classificacao)


def get_filme_by_id(filme_id: int):
    for filme in filmes:
        if filme.id == filme_id:
            return filme


classificacao_to_text()


@ui.page("/cadastrar-filme")
def cadastrar_filme():
    def data_lancamento_func():
        with ui.input('Data de Estreia') as date_input:
            with ui.menu().props('no-parent-event') as menu:
                with ui.date().bind_value(date_input):
                    with ui.row().classes('justify-end'):
                        ui.button('Fechar', on_click=menu.close).props('flat')
            with date_input.add_slot('append'):
                ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')
        return date_input

    ui.label("Cadastro de Filme").classes('text-2xl font-bold mb-4')

    with ui.card().classes('w-full max-w-2xl mx-auto p-10 shadow-lg'):
        with ui.grid(columns=2).classes('gap-4'):
            titulo = ui.input(label="Título")
            ano_producao = ui.number(label="Ano de produção", min=1900, max=datetime.now().year)
            diretor = ui.input(label="Diretor")
            duracao = ui.number(label="Duração (minutos)")
            pais_estreia = ui.select(paises, multiple=False, label="País de estreia").classes("w-64")
            data_lancamento = data_lancamento_func()

            with ui.column():
                ui.label("Classificação indicativa").classes('text-base font-medium')
                classificacao_radio = ui.radio(classificacoes, value=classificacoes[0])

            with ui.column():
                generos_select = ui.select(generos, multiple=True, value=generos[0], label="Gêneros").classes('w-full')
                paises_origem = ui.select(paises, multiple=True, label="Países de origem").classes("w-64")
                sinopse = ui.textarea(label="Sinopse")

        def enviar_filme():
            novo_id = max([f.id for f in filmes]) + 1 if filmes else 1

            data_estreia = data_lancamento.value
            # Conversão para datetime caso seja string ou date
            if isinstance(data_estreia, str):
                try:
                    data_estreia = datetime.strptime(data_estreia, "%Y-%m-%d")
                except ValueError:
                    data_estreia = None  # Caso não consiga converter, seta None
            elif isinstance(data_estreia, date) and not isinstance(data_estreia, datetime):
                data_estreia = datetime.combine(data_estreia, datetime.min.time())

            filme = Filme(
                titulo=titulo.value,
                ano_producao=ano_producao.value,
                diretor=Diretor(nome=diretor.value),
                data_estreia=data_estreia,
                pais_estreia=pais_estreia.value,
                duracao=duracao.value,
                classificacao=classificacao_map(classificacao_radio.value),
                genero={Genero(g) for g in generos_select.value},
                paises_origem=paises_origem.value,
                sinopse=sinopse.value
            )
            filme.id = novo_id
            filmes.append(filme)
            ui.notify(f'Filme "{filme.titulo}" cadastrado com sucesso!', type='positive')

        ui.button("Cadastrar Filme", on_click=enviar_filme).classes('mt-4 bg-blue-500 text-white')


@ui.page("/listar")
def listar():
    ui.label("Lista de Filmes").classes('text-2xl font-bold mb-4')

    if filmes:
        for filme in filmes:
            with ui.card().classes('mb-4 shadow-md max-w-3xl'):
                ui.link(f"{filme.titulo}", f"/exibir_filme/{filme.id}").classes('text-xl text-blue-600')
                ui.label(f"Ano de Produção: {filme.ano_producao}")
                ui.label(f"Diretor: {filme.diretor.nome}")
                ui.label(f"Classificação: {filme.classificacao.name.replace('_', ' ').capitalize()}")
                generos_text = ", ".join([g.value for g in filme.genero])
                ui.label(f"Gêneros: {generos_text}")
                ui.label(f"Países de Origem: {', '.join(filme.paises_origem)}")
                if filme.data_estreia:
                    ui.label(f"Estreia: {filme.data_estreia.strftime('%d/%m/%Y')} - País: {filme.pais_estreia}")
                else:
                    ui.label(f"Estreia: Desconhecida - País: {filme.pais_estreia}")
                ui.label(f"Sinopse: {filme.sinopse}")
    else:
        ui.label("A lista de filmes está vazia.").classes('text-red-500')


@ui.page("/exibir_filme/{filme_id}")
def exibir_filme(filme_id: int):
    filme = get_filme_by_id(filme_id)
    if not filme:
        ui.label("Filme não encontrado.").classes("text-red-500")
        return

    with ui.card().classes('w-full max-w-2xl mx-auto mt-8 p-6 shadow-lg rounded-lg bg-white'):
        with ui.row():
            ui.label("Título").classes("text-gray-600 text-sm mt-1")
            ui.label(filme.titulo).classes("text-lg font-semibold mb-4")

        with ui.row():
            ui.label("Ano produção").classes("text-gray-600 text-sm mt-1")
            ui.label(str(filme.ano_producao)).classes("text-base mb-4")

        with ui.row():
            ui.label("Dirigido por").classes("text-gray-600 text-sm")
            ui.label(filme.diretor.nome).classes("text-base bg-gray-200 rounded px-2 py-1 w-fit mb-4")

        with ui.row():
            ui.label("Estreia").classes("text-gray-600 text-sm")
            if filme.data_estreia:
                estreia_text = f"{filme.data_estreia.strftime('%d/%m/%Y')} - {filme.pais_estreia}"
            else:
                estreia_text = "Desconhecida"
            ui.label(estreia_text).classes("text-base mb-4")

        with ui.row():
            ui.label("Duração").classes("text-gray-600 text-sm")
            ui.label(f"{filme.duracao} min").classes("text-base mb-4")

        with ui.row():
            ui.label("Classificação").classes("text-gray-600 text-sm")
            classificacao_text = filme.classificacao.name.replace("_", " ").capitalize()
            ui.label(classificacao_text).classes("text-white bg-black px-2 py-1 rounded w-fit mb-4")

        with ui.row():
            ui.label("Gênero").classes("text-gray-600 text-sm")
            with ui.row().classes("mb-4"):
                for genero in filme.genero:
                    ui.label(genero.value).classes("bg-gray-300 rounded px-2 py-1 text-sm")

        with ui.row():
            ui.label("Países de Origem").classes("text-gray-600 text-sm")
            with ui.row().classes("mb-4"):
                for pais in filme.paises_origem:
                    ui.label(pais).classes("bg-gray-200 rounded px-2 py-1 text-sm")

        ui.label("Sinopse").classes("text-gray-600 text-base font-semibold mt-4")
        ui.label(filme.sinopse).classes("text-base text-justify mt-2")


ui.run()
