import datetime

class DataAtual:
    
    def __init__(self):
        self.dateTime = datetime.datetime.now()
    
    def metodo1(self):
        return self.dateTime.strftime("%d/%m/%Y")
    
    def metodo2(self):  
        return self.dateTime.strftime("%Hh%Mm")
    
    def metodo3(self):
        return self.dateTime.strftime("%c")

data = DataAtual()
opt = 0


while(opt != 4):
    print("Informe o formato de data e hora que deseja visualizar:")
    print("1: dd/mm/YYYY")
    print("2: HH:MM")
    print("3: Formato local")
    print("4: sair")
    opt = int(input())
    
    if(opt == 1): print(data.metodo1())
    elif(opt == 2): print(data.metodo2())
    elif(opt == 3): print(data.metodo3())


