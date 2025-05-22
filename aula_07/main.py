from nicegui import ui, app
from models import Diretor, Estreia, Filme, Genero, Classificacao
from datetime import datetime
from dados import dados_filmes

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

    def data_lancamento_func():
        with ui.input('Date') as date:
            with ui.menu().props('no-parent-event') as menu:
                with ui.date().bind_value(date):
                    with ui.row().classes('justify-end'):
                        ui.button('Close', on_click=menu.close).props('flat')
            with date.add_slot('append'):
                ui.icon('edit_calendar').on('click', menu.open).classes('cursor-pointer')
        return date

    with ui.row():
        with ui.column():
            ui.label("Cadastrar Filme").classes(replace='text-lg')

            titulo = ui.input(label="Título")
            ano_producao = ui.number(label="Ano de produção", min=1900, max=datetime.now().year)
            diretor = ui.input(label="Diretor")
            pais_estreia = ui.input(label="País de estreia")
            ui.label("Data de estreia").classes(replace='text-gray-500 text-base')
            data_lancamento = data_lancamento_func()
            duracao = ui.number(label="Duração (minutos)")
            sinopse = ui.textarea(label="Sinopse")

            ui.label("Países de Origem (separados por vírgula)")
            paises_origem = ui.input(label="Países de origem")

        with ui.column():
            ui.label("Classificação indicativa")
            classificacao_radio = ui.radio(classificacoes, value=classificacoes[0])

            ui.label("Gêneros")
            generos_select = ui.select(generos, multiple=True, value=generos[0], label='comma-separated').classes('w-64')
            

            def enviar_filme():
                titulo_value = titulo.value
                ano_producao_value = ano_producao.value
                diretor_value = diretor.value
                pais_estreia_value = pais_estreia.value
                data_lancamento_value = data_lancamento.value
                duracao_value = duracao.value
                sinopse_value = sinopse.value
                paises_origem_value = paises_origem.value.split(',') 
                classificacao_value = classificacao_radio.value

                diretor_obj = Diretor(nome=diretor_value)
                estreia_obj = Estreia(data=data_lancamento_value, pais=pais_estreia_value)
                classificacao_obj = Classificacao(classificacao_map(classificacao_value))
                filme = Filme(
                    titulo=titulo_value,
                    ano_producao=ano_producao_value,
                    diretor=diretor_obj,
                    estreia=estreia_obj,
                    duracao=duracao_value,
                    classificacao=classificacao_obj,
                    genero=set(generos_select),
                    paises_origem=set(paises_origem_value),
                    sinopse=sinopse_value
                )
                filmes.append(filme)
                ui.label(f'Filme "{filme.titulo}" cadastrado com sucesso!').classes('text-green-500')

            ui.button("Cadastrar Filme", on_click=enviar_filme)


@ui.page("/listar")
def listar():
    if filmes:
        for filme in filmes:
            if len(filme.genero) != 0:
                ui.label("tem generos")
            ui.label(f"Título: {filme.titulo}")
            ui.label(f"Ano de Produção: {filme.ano_producao}")
            ui.label(f"Diretor: {filme.diretor.nome}")
            ui.label(f"Classificação: {str(filme.classificacao.name.replace('_', ' ').capitalize())}")
            generos_list = filme.genero
            generos_text = "Gêneros: "
            for genero in generos_list:
                generos_text += f"{genero.value}, "
            ui.label(f"Países de Origem: {', '.join(filme.paises_origem)}")
            ui.label(generos_text)
            data_estreia = filme.estreia.data 
            pais_estreia = filme.estreia.pais
            ui.label(f"Estreia: {data_estreia} - País: {pais_estreia}")
            
            ui.label(f"Sinopse: {filme.sinopse}")
            ui.label("-"*300)
    else:
        ui.label("A lista de filmes está vazia.")

ui.run()
