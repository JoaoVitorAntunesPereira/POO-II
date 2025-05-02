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
    
    ui.link('Página inicial', '/', new_tab=False)
    with ui.row():
        with ui.column():
            ui.label('Contas cadastradas')
            
            columns = [
                {'name': 'nome', 'label': 'Nome', 'field': 'nome', 'align': 'left'},
                {'name': 'pix', 'label': 'Chave pix', 'field': 'pix', 'align': 'left'},
                {'name': 'link', 'label': 'Consultar dados', 'field': 'link', 'align': 'left'}
            ]
            
            rows = []
            
            for id, conta in contas.items():
                rows.append({'uuid': id,'nome': conta.nome, 'pix': conta.pix, 'link': '/consulta/'+id})
            
            table = ui.table(columns=columns, rows=rows, row_key='nome')
            table.add_slot('body-cell-link', '''
                            <q-td :props="props">
                                <a :href="props.value"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" style="fill: rgba(0, 0, 0, 1);transform: ;msFilter:;"><path d="M10 18a7.952 7.952 0 0 0 4.897-1.688l4.396 4.396 1.414-1.414-4.396-4.396A7.952 7.952 0 0 0 18 10c0-4.411-3.589-8-8-8s-8 3.589-8 8 3.589 8 8 8zm0-14c3.309 0 6 2.691 6 6s-2.691 6-6 6-6-2.691-6-6 2.691-6 6-6z"></path><path d="M11.412 8.586c.379.38.588.882.588 1.414h2a3.977 3.977 0 0 0-1.174-2.828c-1.514-1.512-4.139-1.512-5.652 0l1.412 1.416c.76-.758 2.07-.756 2.826-.002z"></path></svg></a>
                            </q-td>
                        ''')

            
            with ui.row():
                ui.button('Cadastrar conta', on_click=lambda: ui.navigate.to('/cadastrar_conta'))
                ui.button('Transferir', on_click=lambda: ui.navigate.to('/transferencia'))
        
    

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


def buscar_conta_pix(pix: str) -> Conta:
    for id, conta in contas.items():
        if conta.pix == pix:
            return conta
        
    return None

def transferencia_func(origem, destino, valor):
    conta_origem = buscar_conta_pix(origem)
    conta_destino = buscar_conta_pix(destino)
    valor_transferencia = float(valor)
    
    conta_origem.transferir(conta_destino=conta_destino, valor=valor_transferencia)

    ui.notify("Transferência realizada!")
    ui.navigate.to("/")


def buscar_conta_uuid(uuid: str) -> Conta:
    for id, conta in contas.items():
        if id == uuid:
            return conta
        
    return None


def replace_text_color(label: ui.label, value: float):
    if value < 0:
        label.classes(replace='text-red-600 textt-lg')
    else:
        label.classes(replace='text-green-600 text-lg')

@ui.page('/consulta/{id}')
def consulta_dados(id: str):
    conta = buscar_conta_uuid(id)
    
    with ui.column():
        with ui.row():
            ui.label("Nome: ").classes(replace='font-bold text-lg')
            ui.label(conta.nome).classes(replace='text-lg text-blue-600')
        
        with ui.row():
            ui.label("Chave pix: ").classes(replace='font-bold text-lg')
            ui.label(conta.pix).classes(replace='text-lg text-blue-600')
            
        with ui.row():
            ui.label("Saldo: ").classes(replace='font-bold text-lg')
            saldo_dado = ui.label(conta.saldo)
            replace_text_color(saldo_dado, conta.saldo)
        
        with ui.row():
            ui.label("Limite: ").classes(replace='font-bold text-lg')
            limite_dado = ui.label(conta.limite)
            replace_text_color(limite_dado, conta.limite)
    pass


ui.run()