
import uuid
from conta_property_2 import Transacao, Conta
from nicegui import ui, app, observables
from datetime import datetime
from rich import print



contas = {}

def adicionarConta(obj):
    id_unico = str(uuid.uuid4())
    contas[id_unico] = obj
    return id_unico


c1 = Conta(10000, "joao@gmail.com", 5000, "JOao vitor")
c2 = Conta(510, "jose@gmail.com", 100, "sjose")
c3 = Conta(500, "vitor@gmail.com", 250, "vitor")
c4 = Conta(-200, "carlos@gmail.com", 500, "JOao Carlos vitor")

adicionarConta(c1)
adicionarConta(c2)
adicionarConta(c3)
adicionarConta(c4)


@ui.page('/cadastrar_conta')
def criar_conta():
    
    def criar_conta_func():
        ui.navigate.to('/')
        conta = Conta(saldo=float(saldo.value), pix=pix.value, limite=float(limite.value), nome=nome.value)
        ui.notify(conta.saldo)
        adicionarConta(conta)
        app.storage.general(contas)
        
    
    with ui.column():
        ui.label("Criar conta")
        saldo = ui.input(label='Saldo da conta')
        nome = ui.input(label='Nome')
        pix = ui.input(label='Chave pix')
        limite = ui.input(label='Limite')
        ui.button('Criar', on_click=criar_conta_func)


@ui.page('/')
def index():
    
    def consulta_dados(conta_obj):
        
        if not conta_obj:
            dados_conta.set_text('')
            return Conta(0,'')
        for id, conta in contas.items():
            if id == conta_obj[0]['uuid']:
                print(conta)
                dados_conta.set_text(conta.saldo)
                if conta.saldo < 0:
                    dados_conta.classes(replace='text-negative')
                else:
                    dados_conta.classes(replace='text-positive')
                return conta
        
    
    ui.link('Página inicial', '/', new_tab=False)
    with ui.row():
        with ui.column():
            ui.label('Contas cadastradas')
            
            columns = [
                {'name': 'nome', 'label': 'Nome', 'field': 'nome', 'align': 'left'},
                {'name': 'pix', 'label': 'Chave pix', 'field': 'pix'}
            ]
            
            rows = []
            
            for id, conta in contas.items():
                rows.append({'uuid': id,'nome': conta.nome, 'pix': conta.pix})
            
            ui.table(columns=columns, rows=rows, row_key='nome', on_select=lambda e: consulta_dados(e.selection), selection="single")
            
            with ui.row():
                ui.button('Cadastrar conta', on_click=lambda: ui.navigate.to('/cadastrar_conta'))
                ui.button('Transferir', on_click=lambda: ui.navigate.to('/transferencia'))
        
        with ui.column():
            pass
        
        with ui.column():
            ui.label('Consulta saldo')
            dados_conta = ui.label('')
    

@ui.page('/transferencia')
def transferencia():
    ui.link('Página inicial', '/', new_tab=False)
    ui.label("TRanferencias")
    
    with ui.row():
        
        with ui.column():
            ui.label('Informe a chave pix')
            origem = ui.input(label='De')
            destino = ui.input(label='Para')
            valor = ui.input(label='Valor')
            ui.button("Transferir", on_click=lambda: transferencia_func(origem.value, destino.value, valor.value))
            pass
        
        with ui.column():
            pass


def buscar_conta(pix: str) -> Conta:
    for id, conta in contas.items():
        if conta.pix == pix:
            return conta
        
    return None

def transferencia_func(origem, destino, valor):
    conta_origem = buscar_conta(origem)
    conta_destino = buscar_conta(destino)
    valor_transferencia = float(valor)
    
    conta_origem.transferir(conta_destino=conta_destino, valor=valor_transferencia)

    ui.notify("Transferência realizada!")
    ui.navigate.to("/")

ui.run()