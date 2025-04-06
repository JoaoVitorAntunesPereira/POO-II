from rich import print

class Transacao:
    """ Atributos: op, tipo, data, valor, origem, destino, status """
    pass

class Conta: 
    """ Atributos: saldo, limite, pix, nome, transacoes """

    def __init__(self, 
                 saldo: float, 
                 pix: str, 
                 limite: float = None,
                 nome: str = None
                ):
        
        self.nome = nome
        self.saldo = saldo
        self.pix = pix
        self.limite = limite
        self.transacoes: list[Transacao] = [] # 1 Conta possui N transações(1-N)

    def transferir(self, conta_destino: "Conta", valor: float):
        """ realiza transferência pix """
        print(f"Transferindo R${float(valor)} de {self.pix} para {conta_destino.pix}")

        if (self.saldo - valor) < (0 - self.limite): 
            print("Transferência recusada! Excede o limite.")
        else: 
            self.saldo -= valor
            conta_destino.saldo += valor
            print("Transferência concluida")
        pass

    def consulta(self):
        """ consulta saldo da conta """
        cl = "red" if self.saldo < 0 else "green"
        print(f"Saldo atual:  R$[{cl}]{self.saldo}[/] ({self.pix})")
        pass

# Testar:

if __name__ == "__main__":

    maria = Conta(saldo=20_000, pix="maria@pessoa.br", limite=2000)
    jose = Conta(saldo=-6000, pix="jose@pessoa.br")

    maria.transferir(jose, 8_000)

    maria.consulta()
    jose.consulta()
