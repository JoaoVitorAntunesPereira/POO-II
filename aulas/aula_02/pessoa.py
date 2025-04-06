from rich import print

class Pessoa:
    def __init__(self, 
                nome: str, 
                email: str = None
                ):

        self.nome = nome
        self.email = email
        self.renda = 0
        pass

    def exibirDados(self):
        print(f"""Nome: {self.nome}\
              \nEmail: {self.email}\
              \nRenda: {self.renda}""")


class PessoaJuridica(Pessoa):
    pass

if __name__ == "__main__":
    p1 = Pessoa("Joao", "Joao@gmail.com")
    print(p1.nome)
    print(p1.email)
    p1.renda = 90_000
    print(f"Renda anual de {p1.nome}: R$ {p1.renda}")
    p2 = Pessoa("James")
    print(p2.nome)
    print(p2.email)
    
    pj = PessoaJuridica("Muffato")
    print(pj.nome)
    
    