
from conta_property_2 import Transacao, Conta
from nicegui import ui, app, observables
from datetime import datetime
from rich import print



contas: list[Conta] = []

c1 = Conta(10000, "joao@gmail.com", 5000, "JOao vitor")
c2 = Conta(510, "jose@gmail.com", 100, "sjose")
c3 = Conta(500, "vitor@gmail.com", 250, "vitor")
c4 = Conta(1110, "carlos@gmail.com", 500, "JOao Carlos vitor")

contas.append(c1)
contas.append(c2)
contas.append(c3)
contas.append(c4)


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
def index():
    
    
    def consulta_dados(conta):
        print(conta)
        dados_conta.set_text(f"R$ {conta[0]['saldo']}")
        if float(conta[0]['saldo']) < 0:
            dados_conta.classes(replace='text-negative')
        else:
            dados_conta.classes(replace='text-positive')
        
    
    ui.link('Página inicial', '/', new_tab=False)
    with ui.row():
        with ui.column():
            ui.label('Contas cadastradas')
            
            columns = [
                {'name': 'nome', 'label': 'Nome', 'field': 'nome', 'align': 'left'},
                {'name': 'pix', 'label': 'Chave pix', 'field': 'pix'}
            ]
            
            rows = []
            
            for conta in contas:
                rows.append({'nome': conta.nome, 'pix': conta.pix,'saldo':conta.saldo})
            
            ui.table(columns=columns, rows=rows, row_key='nome', on_select=lambda e: consulta_dados(e.selection), selection="single")
            
            with ui.row():
                ui.button('Cadastrar conta', on_click=lambda: ui.navigate.to('/cadastrar_conta'))
                ui.button('Realizar transferência', on_click=lambda: ui.navigate.to('/transferencia'))
        
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
    for conta in contas:
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