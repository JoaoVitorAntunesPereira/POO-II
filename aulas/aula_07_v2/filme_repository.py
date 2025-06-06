from utils import SessionLocal, init_db
from filme_db_models import tb_filme, tb_diretor, tb_classificacao, tb_filme_genero, tb_filme_pais_origem, tb_genero, tb_pais
from filme_obj_models import Filme, Diretor, Classificacao, Genero, Pais

class FilmeRepository:
    def __init__(self):
        init_db()
        self.db = SessionLocal()


#---Filmes---
    def get_all_filmes(self):
        filme_list = []
        query = self.db.query(tb_filme).all()
        for filme in query:
            filme_list.append(self.map_filme_to_obj(filme))
        return filme_list
    
    def map_filme_to_obj(self, filme: tb_filme):
        diretor_obj = self.get_diretor_by_id(filme.diretor_id)
        classificacao_obj = self.get_classificacao_by_id(filme.classificacao_id)
        generos_obj_list = []
        
        for g in filme.generos:
            genero_obj = Genero(g.descricao)
            genero_obj.id = g.genero_id
            generos_obj_list.append(genero_obj)        
        
        paises_origem_list = []
        for p in filme.paises_origem:
            pais_obj = Pais(p.nome)
            pais_obj.id = p.pais_id
            paises_origem_list.append(pais_obj)
        
        filme_obj = Filme(
            titulo=filme.titulo,
            ano_producao=filme.ano_producao,
            diretor=diretor_obj,
            data_estreia=filme.data_estreia,
            pais_estreia=filme.pais_estreia,
            duracao=filme.duracao,
            classificacao=classificacao_obj,
            generos=generos_obj_list,
            paises_origem=paises_origem_list,
            sinopse=filme.sinopse
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
        return self.map_diretor_to_obj(self.db.query(tb_diretor).filter(tb_diretor.diretor_id == id).first())

    def get_diretor_by_name(self, nome: str):
        return self.db.query(tb_diretor).filter(tb_diretor.nome == nome).one()
    
    def get_all_diretor(self):
        diretores = self.db.query(tb_diretor).all()
        return [self.map_diretor_to_obj(d) for d in diretores]


    def add_diretor(self, diretor_obj: Diretor):
        diretor = self.map_diretor_to_obj(diretor_obj)
        self.db.add(diretor)
        self.db.commit()

    def map_diretor_to_obj(self, diretor: tb_diretor):
        diretor_obj = Diretor(diretor.nome)
        diretor_obj.id = diretor.diretor_id
        return diretor_obj
    
#---Classificação
    def get_classificacao_by_id(self, id: int):
        return self.map_classificacao_to_obj(self.db.query(tb_classificacao).filter(tb_classificacao.classificacao_id == id).first())
    
    def get_all_classificacao(self):
        classificacoes = self.db.query(tb_classificacao).all()
        return [self.map_classificacao_to_obj(c) for c in classificacoes]
    
    def map_classificacao_to_obj(self, classificacao: tb_classificacao):
        classificacao_obj = Classificacao(classificacao.descricao)
        classificacao_obj.id = classificacao.classificacao_id
        return classificacao_obj
    
    def add_class(self, classi: tb_classificacao):
        self.db.add(classi)
        self.db.commit()
    
   
#---Pais
    def get_pais_by_id(self, id: int):
        return self.map_pais_to_obj(self.db.query(tb_pais).filter(tb_pais.pais_id == id).first())
    
    def get_all_pais(self):
        paises = self.db.query(tb_pais).all()
        return [self.map_pais_to_obj(p) for p in paises]
    
    def map_pais_to_obj(self, pais: tb_pais):
        pais_obj = Pais(pais.nome)
        pais_obj.id = pais.pais_id
        return pais_obj


#---Genero
    def get_genero_by_id(self, id: int):
        return self.map_genero_to_obj(self.db.query(tb_genero).filter(tb_genero.genero_id == id).first())

    def get_all_genero(self):
        generos = self.db.query(tb_genero).all()
        return [self.map_genero_to_obj(g) for g in generos]
    
    def map_genero_to_obj(self, genero: tb_genero):
        genero_obj = Genero(genero.descricao)
        genero_obj.id = genero.genero_id
        return genero_obj
    

#---Filme_Genero
    def get_filme_genero_by_filme_id(self, id: int):
        return self.db.query(tb_filme_genero).filter(tb_filme_genero.filme_id == id).all()
    
    

#---Filme_Pais_Origem
    def get_filme_pais_origem_by_filme_id(self, id: int):
        return self.db.query(tb_filme_pais_origem).filter(tb_filme_pais_origem.filme_id == id).all()
    
    
    
    
            



