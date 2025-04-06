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

print(data.metodo1())
print(data.metodo2())
print(data.metodo3())