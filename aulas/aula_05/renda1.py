from nicegui import ui



with ui.column():
    i = ui.input(label='Renda anual')
    imposto = ui.label('Valor a pagar:')

def calculo():
    ui.notify(f"Calculando...{i.value}")
    ir = float(i.value) * 0.10
    imposto.set_text(f"Valor a pagar: R${ir}")
    
ui.button("Calcular", on_click=calculo)








ui.run()