from datetime import datetime
from rich import print

class Transacao:
    def __init__(self):
        """ Atributos: op, tipo, data, valor, origem, destino, status """
        self.operacao: str = None
        self.data: datetime = None
        self.valor: float = None
        self.origem: Conta = None
        self.destino: Conta = None
        self.status: bool = False
        pass

    def credito(valor: float, origem: "Conta", destino: "Conta") -> "Transacao":
        #cria uma transação de crédito
        t = Transacao()
        t.operacao = "C"
        t.data = datetime.now()
        t.valor = valor
        t.origem = origem
        t.destino = destino
        return t
    pass

    def debito(valor: float, origem: "Conta", destino: "Conta") -> "Transacao":
        #cria uma transação de crédito
        t = Transacao()
        t.operacao = "D"
        t.data = datetime.now()
        t.valor = valor
        t.origem = origem
        t.destino = destino
        return t
    pass

class Conta: 
    """ Atributos: saldo, limite, pix, nome, transacoes """

    def __init__(self, 
                 saldo: float, 
                 pix: str, 
                 limite: float = None,
                 nome: str = None
                ):


        self._saldo = saldo # _ para tornar a variável protegida
        self.nome = nome
        self._pix = pix
        self._limite = limite
        self.transacoes: list[Transacao] = [] # 1 Conta possui N transações(1-N)

    @property
    def saldo(self) -> float: #getter
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float):
        self._saldo = valor

    @property
    def limite(self) -> float:
        return self._limite

    @limite.setter
    def limite(self, valor: float):
        self._limite = valor

    @property
    def pix(self) -> str:
        return self._pix

    @pix.setter
    def pix(self, valor: str):
        if not isinstance(valor, str):
            raise TypeError("Deve ser uma string")
        if len(valor) < 4:
            raise ValueError("Mínimo de 4 caracteres")
        self._pix = valor

    @property
    def saldo_limite(self) -> float:
        return self._saldo + self._limite


    def transferir(self, conta_destino: "Conta", valor: float):
        """ realiza transferência pix """

        t_credito = Transacao.credito(valor, origem=self, destino=conta_destino)
        t_debito = Transacao.debito(valor, origem=self, destino=conta_destino)

        if self != conta_destino:
            print(f"Transferindo R${float(valor)} de {self.pix} para {conta_destino.pix}")

            if valor > self.saldo_limite: 
                print("Transferência recusada! Excede o limite.")
            elif valor <= 0:
                print("Valor negativo ou igual a zero informado!")
            else: 
                self.saldo -= valor
                conta_destino.saldo += valor
                print("Transferência concluida")
                t_credito.status = True
                t_debito.status = True
        else:
            print("Transação não autorizada! Pix para sí próprio.")
        pass

        conta_destino.transacoes.append(t_credito)
        self.transacoes.append(t_debito)


    def consulta(self):
        """ consulta saldo da conta """
        cl = "red" if self.saldo < 0 else "green"
        print(f"Saldo atual:  R$[{cl}]{self.saldo}[/] ({self.pix})")
        pass

    def extrato(self):
        print(f"[yellow]Transações: {self.pix} [\]")
        for t in self.transacoes:
            print("="*30)
            cor = "red" if t.operacao == "D" else "green"

            if t.operacao == "D":
                operacao = "Débito"
                cor_operacao = "red"
            else:
                operacao = "Crédito"
                cor_operacao = "green"

            if t.status == False:
                status = "Recusada"
                cor_status = "red"
            else:
                status = "Aprovada"
                cor_status = "green"

            print(f"Operação: [{cor_operacao}]{operacao}[/]\n" +
                  f"Data: {t.data}\n" +
                  f"Valor: [{cor_operacao}]{t.valor}[/]\n" +
                  f"Origem: {t.origem.pix}\n" +
                  f"Destino: {t.destino.pix}\n" +
                  f"Status: [{cor_status}]{status}[/]")



        self.operacao: str = None
        self.data: datetime = None
        self.valor: float = None
        self.origem: Conta = None
        self.destino: Conta = None
        self.status: bool = False

# Testar:

if __name__ == "__main__":

    maria = Conta(saldo=20_000, pix="maria@pessoa.br", limite=2000)
    jose = Conta(saldo=-6000, pix="jose@pessoa.br")

    maria.transferir(jose, 23_000)
    maria.transferir(jose, 21_000)




    maria.extrato()
    jose.extrato()

    maria.consulta()
    jose.consulta()