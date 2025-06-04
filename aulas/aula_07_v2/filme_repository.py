from utils import SessionLocal, init_db
from filme_db_models import tb_filme, tb_diretor, tb_classificacao, tb_genero
from filme_obj_models import Filme, Diretor

class FilmeRepository:
    def __init__(self):
        init_db()
        self.db = SessionLocal()


#---Filmes---
    def get_filmes(self):
        filme_list = []
        query = self.db.query(tb_filme).all()
        for filme in query:
            filme_list.append(self.map_filme(filme))
        return filme_list
    
    def map_filme(self, filme: tb_filme):
        diretor_obj = self.map_diretor(filme.diretor)
        filme_obj = Filme(
            titulo=filme.titulo,
            ano_producao=filme.ano_producao,
            genero=filme.generos, 
            diretor=diretor_obj
        )
        return filme_obj

    def add_filme(self, filme_obj: Filme):
        print("ID do diretor recebido:", filme_obj.diretor.id)
        generos_str = ', '.join(g.value for g in filme_obj.genero)
        diretor = self.get_diretor_by_id(filme_obj.diretor.id)
        filme = tb_filme(
            titulo=filme_obj.titulo,
            ano_producao=filme_obj.ano_producao,
            generos=generos_str,
            diretor=diretor
        )
        self.db.add(filme)
        self.db.commit()


#---Diretor
    def get_diretor_by_id(self, id: int):
        return self.db.query(tb_diretor).filter(tb_diretor.diretor_id == id).first()

    def get_diretor_by_name(self, nome: str):
        return self.db.query(tb_diretor).filter(tb_diretor.nome == nome).one()

    def add_diretor(self, diretor_obj: Diretor):
        diretor = self.map_diretor(diretor_obj)
        self.db.add(diretor)
        self.db.commit()

    def map_diretor(self, diretor: tb_diretor):
        diretor_obj = Diretor(diretor.nome)
        diretor_obj.id = diretor.diretor_id
        return diretor_obj
    
#---Classificação
    def get_classificacao_by_id(self, id: int):
        return self.db.query(tb_cl)


