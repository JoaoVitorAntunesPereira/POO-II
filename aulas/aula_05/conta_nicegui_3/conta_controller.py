import csv
from conta import *
from uuid import uuid4

class ContaController:
    
    def conta_to_array(conta: Conta):
        array = []
        array.append(conta.uuid)
        array.append(conta.nome)
        array.append(conta.pix)
        array.append(conta.saldo)
        array.append(conta.limite)
            
        return array
            
    
    def criar_arquivo():
        cabecalho = [
                    ['uuid','nome','pix','saldo','limite']
                    ]
        
        with open('arquivos/contas.csv', mode='w', newline='', encoding='utf-8') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(cabecalho)
            
        pass
    
    def adicionar_conta_arquivo(self, conta: Conta):
        conta_array = []
        conta_array.append(ContaController.conta_to_array(conta))
        
        with open('arquivos/contas.csv', mode='a', newline='', encoding='utf8') as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerows(conta_array)
        
        pass
    
    
    
    pass