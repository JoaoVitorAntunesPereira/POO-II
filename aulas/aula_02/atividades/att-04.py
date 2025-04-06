from abc import abstractmethod

class Roteador:
    
    def aceitar(self, dispositivo): 
        conexao = False
        
        if(issubclass(type(dispositivo), Dispositivo)):
            conexao = True
        return conexao
    
    
class Dispositivo:
    
    def __init__(self):
        pass
    
    @abstractmethod
    def conectar(self):
        pass
        
    
class Notebook(Dispositivo):
    
    def conectar(self):
        print("Conectando Notebook...")
        if(roteador.aceitar(self)):
            print("Conectado")
        else:
            print("Erro ao conectar")

class Smartphone(Dispositivo):
    def conectar(self):
        print("Conectando Smartphone...")
        if(roteador.aceitar(self)):
            print("Conectado")
        else:
            print("Erro ao conectar")
    
    
roteador = Roteador()
notebook = Notebook()
smartphone = Smartphone()

notebook.conectar()
smartphone.conectar()