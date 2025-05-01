from enum import Enum

class DDD(Enum):
    PARANA = 45
    SC = 49

class TipoPessoa(Enum):
    FISICA = "Pessoa Fisica"
    JURIDICA = "Pessoa Jurídica"

opcao = "Pessoa Fisica"

if opcao == TipoPessoa.FISICA.value:
    print("ir PF")
elif opcao == TipoPessoa.JURIDICA.value:
    print("ir PJ")

print(type(DDD.PARANA))