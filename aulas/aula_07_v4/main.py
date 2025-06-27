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

@ui.page("/editar/{filme_id}")
def editar(filme_id: str):
    ui.timer(0.1, lambda: ui.navigate.to(f"/formulario/{filme_id}"), once=True)

@ui.page("/cadastrar-filme")
def cadastrar_filme():
    ui.timer(0.1, lambda: ui.navigate.to(f"/formulario/{0}"), once=True)

@ui.page("/formulario/{filme_id}")
def formulario(filme_id: int):
    
    filme_edit = None
    
    if filme_id != 0:
        filme_edit = filme_controller.buscar_filme_por_id(filme_id)
        if not filme_edit:
            ui.timer(0.1, lambda: ui.navigate.to(f"/listar"), once=True)
    
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
            titulo.set_value(filme_edit.titulo if filme_edit else "")
            
            ano_producao = ui.number(label="Ano de produção", min=1900, max=datetime.now().year)
            ano_producao.set_value(filme_edit.ano_producao if filme_edit else None)
            
            diretores = filme_controller.listar_diretores()
            mapa_diretores = {d.nome: d for d in diretores}
            nomes_diretores = list(mapa_diretores.keys())
            diretor = ui.select(nomes_diretores, multiple=False, label="Diretor").classes("w-64")
            diretor.set_value(filme_edit.diretor.nome if filme_edit else None)
            
            duracao = ui.number(label="Duração (minutos)")
            duracao.set_value(filme_edit.duracao if filme_edit else None)
            
            paises = filme_controller.listar_paises()
            mapa_paises = {p.descricao: p for p in paises}
            nomes_paises = list(mapa_paises.keys())      
            pais_estreia = ui.select(nomes_paises, multiple=False, label="País de estreia").classes("w-64")
            pais_estreia.set_value(filme_edit.pais_estreia.descricao if filme_edit else None)
            
            data_lancamento = data_lancamento_func()
            data_lancamento.set_value(filme_edit.data_estreia if filme_edit else None)

            with ui.column():
                ui.label("Classificação indicativa").classes('text-base font-medium')
                mapa_classificacoes = classificacao_map()
                opcoes_classificacao = list(mapa_classificacoes.keys())

                chave_classificacao = None
                if filme_edit:
                    for k, v in mapa_classificacoes.items():
                        if v.id == filme_edit.classificacao.id:
                            chave_classificacao = k
                            break
                
                classificacao_radio = ui.radio(opcoes_classificacao, value='Livre')
                classificacao_radio.set_value(chave_classificacao)

            with ui.column():
                generos = filme_controller.listar_generos()
                mapa_generos = {g.descricao: g for g in generos}
                nomes_generos = list(mapa_generos.keys())
                
                chave_generos = None
                if filme_edit:
                   chave_generos = [k for k, v in mapa_generos.items() if v.id in {g.id for g in filme_edit.generos}]
                        
                generos_select = ui.select(nomes_generos, multiple=True, value=[nomes_generos[0]], label="Gêneros").classes('w-full')
                generos_select.set_value(chave_generos)

                chave_paises = None
                if filme_edit:
                   chave_paises = [k for k, v in mapa_paises.items() if v.id in {p.id for p in filme_edit.paises_origem}]

                paises_origem = ui.select(nomes_paises, multiple=True, label="Países de origem").classes("w-64")
                paises_origem.set_value(chave_paises)
                
                sinopse = ui.textarea(label="Sinopse")
                sinopse.set_value(filme_edit.sinopse if filme_edit else None)

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
            
            
            if filme_edit:
                filme.id = filme_edit.id
                filme_controller.editar_filme(filme)
            else:
                filme_controller.adicionar_filme(filme)
            ui.notify(f'Filme "{filme.titulo}" cadastrado com sucesso!', type='positive')
            ui.timer(0.1, lambda: ui.navigate.to("/listar"), once=True)

        botao_texto = "Editar Filme" if filme_id != 0 else "Cadastrar Filme"
        ui.button(botao_texto, on_click=enviar_filme).classes('mt-4 bg-blue-500 text-white')


def abrir_link_cadastrar():
    ui.timer(0.1, lambda: ui.navigate.to("/cadastrar-filme"), once=True)

@ui.page("/listar")
def listar():
    ui.label("Lista de Filmes").classes('text-2xl font-bold mb-4')
        
    with ui.row():
        filme_busca = ui.input(label='Buscar filme', on_change=lambda: tabela.refresh())
    
    @ui.refreshable
    def tabela():
        
        if filme_busca.value == "":
            filmes_list = filme_controller.listar_filmes()
        else:
            filmes_list = filme_controller.buscar_filme_por_titulo(filme_busca.value)
        
        with ui.column():
            if filmes_list:
                columns = [
                    {'name': 'titulo', 'label': 'Título', 'field': 'titulo', 'align': 'left'},
                    {'name': 'estreia', 'label': 'Data de Lançamento', 'field': 'estreia', 'align': 'left'},
                    {'name': 'diretor', 'label': 'Diretor', 'field': 'diretor', 'align': 'left'},
                    {'name': 'ver_mais', 'label': 'Detalhes', 'field': 'ver_mais', 'align': 'left'},
                    {'name': 'editar', 'label': 'Editar', 'field': 'editar', 'align': 'left'},
                    {'name': 'excluir', 'label': 'Excluir', 'field': 'excluir', 'align': 'left'}
                ]

                rows = []
                for filme in filmes_list:
                    rows.append({
                        'titulo': filme.titulo,
                        'estreia': filme.data_estreia.strftime('%d/%m/%Y') if filme.data_estreia else 'Desconhecida',
                        'diretor': filme.diretor.nome,
                        'ver_mais': '/exibir_filme/'+str(filme.id),
                        'editar': '/editar/'+str(filme.id),
                        'excluir': '/excluir/'+str(filme.id)
                    })

                table = ui.table(columns=columns, rows=rows, row_key='titulo')

                table.add_slot('body-cell-ver_mais', '''
                    <q-td :props="props">
                        <a :href="props.value">
                            <q-icon name="search" size="md" class="cursor-pointer" />
                        </a>
                    </q-td>
                ''')
                table.add_slot('body-cell-editar', '''
                    <q-td :props="props">
                        <a :href="props.value">
                            <q-icon name="edit" size="md" class="cursor-pointer" />
                        </a>
                    </q-td>
                ''')
                table.add_slot('body-cell-excluir', '''
                    <q-td :props="props">
                        <a :href="props.value">
                            <q-icon name="delete" size="md" class="cursor-pointer" />
                        </a>
                    </q-td>
                ''')

            else:
                ui.label("A lista de filmes está vazia.").classes('text-red-500')
    tabela()
    
    ui.button("Cadastrar novo filme", on_click=abrir_link_cadastrar).classes('mt-4 bg-blue-500 text-white')

@ui.page("/excluir/{filme_id}")
def excluir(filme_id: int):
    filme_delete = filme_controller.buscar_filme_por_id(filme_id)
    
    filme_controller.excluir_filme(filme_delete)
    ui.timer(0.1, lambda: ui.navigate.to("/listar"), once=True)


@ui.page("/exibir_filme/{filme_id}")
def exibir_filme(filme_id: int):
    filme = filme_controller.buscar_filme_por_id(filme_id)
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
