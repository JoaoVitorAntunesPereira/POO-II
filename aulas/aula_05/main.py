import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aula_04.conta_property import Transacao, Conta
from nicegui import ui
from datetime import datetime
from rich import print



contas: list[Conta] = []


def criar_conta():
    conta = Conta(saldo=float(saldo.value), pix=pix.value, limite=float(limite.value))
    contas.append(conta)



with ui.column():
    ui.label("Criar conta")
    saldo = ui.input(label='Saldo da conta')
    nome = ui.input(label='Nome')
    pix = ui.input(label='Chave pix')
    limite = ui.input(label='Limite')
    ui.button('Criar', on_click=criar_conta)

with ui.column():
    for conta in contas:
        ui.label(f"{conta.nome}")





ui.run()