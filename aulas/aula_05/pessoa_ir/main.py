from pessoa_abs import PessoaFisica, PessoaJuridica, TipoPessoa
from nicegui import ui



pf = PessoaFisica("joao", "joao@gmail.com", "11723323985")
pj = PessoaJuridica("joao", "joao@gmail.com", "11723323985")

with ui.column():
    renda = ui.input(label='Renda anual')
    imposto = ui.label('Valor a pagar:')

with ui.row():
    tipo_pessoa = ui.radio(['Pessoa Física', 'Pessoa Jurídica'], value='Pessoa Física').props('inline')



def calculo():
    if tipo_pessoa.value == TipoPessoa.FISICA.value:
        pf.renda = float(renda.value)  
        ui.notify(f"Calculando...{pf.renda}")
        ir = pf.calcular_ir()
        imposto.set_text(f"Valor a pagar: R${ir}")
    else:    
        pj.renda = float(renda.value)
        ui.notify(f"Calculando...{pj.renda}")
        ir = pj.calcular_ir()
        imposto.set_text(f"Valor a pagar: R${ir}")


ui.button("Calcular", on_click=calculo)








ui.run()
