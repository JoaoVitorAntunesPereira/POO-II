import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conta_property_2 import Transacao, Conta
from nicegui import ui, app, observables
from datetime import datetime
from rich import print



contas: list[Conta] = []





@ui.page('/cadastrar_conta')
def criar_conta():
    
    def criar_conta_func():
        ui.navigate.to('/')
        conta = Conta(saldo=float(saldo.value), pix=pix.value, limite=float(limite.value), nome=nome.value)
        ui.notify(conta.saldo)
        contas.append(conta)
        app.storage.general(contas)
        
    
    with ui.column():
        ui.label("Criar conta")
        saldo = ui.input(label='Saldo da conta')
        nome = ui.input(label='Nome')
        pix = ui.input(label='Chave pix')
        limite = ui.input(label='Limite')
        ui.button('Criar', on_click=criar_conta_func)


@ui.page('/')
def contas_cadastradas():
    ui.link('Página inicial', '/', new_tab=False)
    ui.label('Contas cadastradas')
    
    
    columns = [
        {'name': 'nome', 'label': 'Nome', 'field': 'nome', 'align': 'left'},
        {'name': 'pix', 'label': 'Chave pix', 'field': 'pix'}
    ]
    
    rows = []
    
    for conta in contas:
        rows.append({'nome': conta.nome, 'pix': conta.pix})
        
    ui.table(columns=columns, rows=rows, row_key='name')
    
    ui.button('Cadastrar conta', on_click=lambda: ui.navigate.to('/cadastrar_conta'))

ui.run()