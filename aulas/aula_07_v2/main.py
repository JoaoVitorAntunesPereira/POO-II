from nicegui import ui
from filme_obj_models import Diretor, Filme, Genero, Classificacao, Pais
from filme_controller import FilmeController
from datetime import datetime, date

filme_controller = FilmeController()

filmes = filme_controller.listar_filmes()

def classificacao_map():
    classificacoes = filme_controller.listar_classificacoes()
    mapa = {
        "Livre": classificacoes[0],
        "Proibido para menores de 10 anos": classificacoes[5],
        "Proibido para menores de 12 anos": classificacoes[1],
        "Proibido para menores de 14 anos": classificacoes[2],
        "Proibido para menores de 16 anos": classificacoes[3],
        "Proibido para menores de 18 anos": classificacoes[4]
    }
    return mapa

classificacoes = filme_controller.listar_classificacoes()
generos = filme_controller.listar_generos()

def get_filme_by_id(filme_id: int):
    for filme in filmes:
        if filme.id == filme_id:
            return filme


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
            
            diretores = filme_controller.listar_diretores()
            mapa_diretores = {d.nome: d for d in diretores}
            nomes_diretores = list(mapa_diretores.keys())
            diretor = ui.select(nomes_diretores, multiple=False, label="Diretor").classes("w-64")
            
            duracao = ui.number(label="Duração (minutos)")
            
            paises = filme_controller.listar_paises()
            mapa_paises = {p.descricao: p for p in paises}
            nomes_paises = list(mapa_paises.keys())      
            pais_estreia = ui.select(nomes_paises, multiple=False, label="País de estreia").classes("w-64")
            
            data_lancamento = data_lancamento_func()

            with ui.column():
                ui.label("Classificação indicativa").classes('text-base font-medium')
                mapa_classificacoes = classificacao_map()
                opcoes_classificacao = list(mapa_classificacoes.keys())
                classificacao_radio = ui.radio(opcoes_classificacao, value='Livre')

            with ui.column():
                generos = filme_controller.listar_generos()
                mapa_generos = {g.descricao: g for g in generos}
                nomes_generos = list(mapa_generos.keys())
                generos_select = ui.select(nomes_generos, multiple=True, value=[nomes_generos[0]], label="Gêneros").classes('w-full')

                paises_origem = ui.select(nomes_paises, multiple=True, label="Países de origem").classes("w-64")
                sinopse = ui.textarea(label="Sinopse")

        def enviar_filme():

            data_estreia = data_lancamento.value
            
            if isinstance(data_estreia, str):
                try:
                    data_estreia = datetime.strptime(data_estreia, "%Y-%m-%d")
                except ValueError:
                    data_estreia = None  
            elif isinstance(data_estreia, date) and not isinstance(data_estreia, datetime):
                data_estreia = datetime.combine(data_estreia, datetime.min.time())

            filme = Filme(
                titulo=titulo.value,
                ano_producao=ano_producao.value,
                diretor=mapa_diretores[diretor.value],
                data_estreia=data_estreia,
                pais_estreia=mapa_paises[pais_estreia.value],
                duracao=duracao.value,
                classificacao=mapa_classificacoes[classificacao_radio.value],
                generos={mapa_generos[g] for g in generos_select.value},
                paises_origem={mapa_paises[p] for p in paises_origem.value},
                sinopse=sinopse.value
            )
            print("==== DADOS DO FILME ====")
            print(f"Título: {filme.titulo}")
            print(f"Ano de Produção: {filme.ano_producao}")
            print(f"Diretor: {filme.diretor.nome} (ID: {filme.diretor.id})")
            print(f"Data de Estreia: {filme.data_estreia}")
            print(f"País de Estreia: {filme.pais_estreia.descricao} (ID: {filme.pais_estreia.id})")
            print(f"Duração: {filme.duracao} minutos")
            print(f"Classificação: {filme.classificacao.descricao} (ID: {filme.classificacao.id})")
            print("Gêneros:")
            for genero in filme.generos:
                print(f" - {genero.descricao} (ID: {genero.id})")
            print("Países de Origem:")
            for pais in filme.paises_origem:
                print(f" - {pais.descricao} (ID: {pais.id})")
            print(f"Sinopse: {filme.sinopse}")
            print("========================")
            filme_controller.adicionar_filme((filme))
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
                ui.label(f"Classificação: {filme.classificacao.descricao.capitalize()}")
                generos_text = ", ".join([g.descricao for g in filme.generos])
                ui.label(f"Gêneros: {generos_text}")
                ui.label(f"Países de Origem: {', '.join(p.descricao for p in filme.paises_origem)}")
                if filme.data_estreia:
                    ui.label(f"Estreia: {filme.data_estreia.strftime('%d/%m/%Y')} - País: {filme.pais_estreia.descricao}")
                else:
                    ui.label(f"Estreia: Desconhecida - País: {filme.pais_estreia.descricao}")
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
                estreia_text = f"{filme.data_estreia.strftime('%d/%m/%Y')} - {filme.pais_estreia.descricao}"
            else:
                estreia_text = "Desconhecida"
            ui.label(estreia_text).classes("text-base mb-4")

        with ui.row():
            ui.label("Duração").classes("text-gray-600 text-sm")
            ui.label(f"{filme.duracao} min").classes("text-base mb-4")

        with ui.row():
            ui.label("Classificação").classes("text-gray-600 text-sm")
            classificacao_text = filme.classificacao.descricao.capitalize()
            ui.label(classificacao_text).classes("text-white bg-black px-2 py-1 rounded w-fit mb-4")

        with ui.row():
            ui.label("Gênero").classes("text-gray-600 text-sm")
            with ui.row().classes("mb-4"):
                for genero in filme.generos:
                    ui.label(genero.descricao).classes("bg-gray-300 rounded px-2 py-1 text-sm")

        with ui.row():
            ui.label("Países de Origem").classes("text-gray-600 text-sm")
            with ui.row().classes("mb-4"):
                for pais in filme.paises_origem:
                    ui.label(pais.descricao).classes("bg-gray-200 rounded px-2 py-1 text-sm")

        ui.label("Sinopse").classes("text-gray-600 text-base font-semibold mt-4")
        ui.label(filme.sinopse).classes("text-base text-justify mt-2")


ui.run()
