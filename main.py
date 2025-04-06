from aulas.aula_02.pessoa import Pessoa
from aulas.aula_02.pessoa_abs import PessoaJuridica
from aulas.aula_01.pessoa import Pessoa as P1



p = Pessoa("Maria")
print(p.nome)

pj = PessoaJuridica("Italo", "it@gov.br", "0000")
print(pj.nome)

p1 = P1("Jose")
p1.exibe_dados()