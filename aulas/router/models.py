from abc import ABC

class Roteador:
    
    def __init__(self):
        self.ip = "192.168.1."
        self.contador = 1
        self.dispositivos_conectados = []
        self.senha = None
        pass

    def aceitar(self, dispositivo: "Dispositivo", senha: str):
        if senha == self.senha:
            print(f"Conexão aceita com {dispositivo.nome}")
            dispositivo.ip = self.ip + str(self.contador) 
            self.contador += 1
            self.dispositivos_conectados.append(dispositivo)
        else:
            print("Senha incorreta")
            print("Conexão recusada")
        pass

    def listar_dispositivos(self):
        print("Dispositivos conectados")
        for dispositivo in self.dispositivos_conectados:
            print(f"{dispositivo.nome} - {dispositivo.ip}")
        pass


class Dispositivo(ABC):

    def __init__(self, nome: str):
        self.nome = nome 
        self.ip = None


    def conectar(self, roteador: "Roteador", senha: str):
        print("Conectando com roteador")
        roteador.aceitar(self, senha)
        pass


class Notebook(Dispositivo):
    pass


class Smartphone(Dispositivo): 
    pass