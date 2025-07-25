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
    
    def get_filme_by_id(self, id: int):
        try:
            filme = self.map_filme_to_obj(self.db.query(tb_filme).filter(tb_filme.filme_id == id).first())
            return filme
        except ValueError:
            return 0
    
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
        
        pais_estreia_obj = self.map_pais_to_obj(filme.pais_estreia)
        
        filme_obj = Filme(
            titulo=filme.titulo,
            ano_producao=filme.ano_producao,
            diretor=diretor_obj,
            data_estreia=filme.data_estreia,
            pais_estreia=pais_estreia_obj,
            duracao=filme.duracao,
            classificacao=classificacao_obj,
            generos=generos_obj_list,
            paises_origem=paises_origem_list,
            sinopse=filme.sinopse
        )
        
        filme_obj.id = filme.filme_id
        
        return filme_obj

    def add_filme(self, filme_obj):
        diretor_db = self.db.query(tb_diretor).get(filme_obj.diretor.id)
        classificacao_db = self.db.query(tb_classificacao).get(filme_obj.classificacao.id)
        pais_estreia_db = self.db.query(tb_pais).get(filme_obj.pais_estreia.id)

        generos_db = [self.db.query(tb_genero).get(g.id) for g in filme_obj.generos]
        paises_origem_db = [self.db.query(tb_pais).get(p.id) for p in filme_obj.paises_origem]

        filme_db = tb_filme(
            titulo=filme_obj.titulo,
            ano_producao=filme_obj.ano_producao,
            data_estreia=filme_obj.data_estreia,
            duracao=filme_obj.duracao,
            sinopse=filme_obj.sinopse,
            is_active=True,
            diretor=diretor_db,
            classificacao=classificacao_db,
            pais_estreia=pais_estreia_db
        )

        filme_db.generos.extend(generos_db)
        filme_db.paises_origem.extend(paises_origem_db)

        self.db.add(filme_db)
        self.db.commit()
            
    def edit_filme(self, filme_obj):
        filme_db = self.db.query(tb_filme).get(filme_obj.id)
        if not filme_db:
            return 0

        filme_db.titulo = filme_obj.titulo
        filme_db.ano_producao = filme_obj.ano_producao
        filme_db.data_estreia = filme_obj.data_estreia
        filme_db.duracao = filme_obj.duracao
        filme_db.sinopse = filme_obj.sinopse
        filme_db.diretor = self.db.query(tb_diretor).get(filme_obj.diretor.id)
        filme_db.classificacao = self.db.query(tb_classificacao).get(filme_obj.classificacao.id)
        filme_db.pais_estreia = self.db.query(tb_pais).get(filme_obj.pais_estreia.id)

        filme_db.generos.clear()
        generos_db = [self.db.query(tb_genero).get(g.id) for g in filme_obj.generos]
        filme_db.generos.extend(generos_db)

        filme_db.paises_origem.clear()
        paises_db = [self.db.query(tb_pais).get(p.id) for p in filme_obj.paises_origem]
        filme_db.paises_origem.extend(paises_db)

        self.db.commit()

    def delete_filme(self, filme_obj: Filme):
        filme_db = self.db.query(tb_filme).get(filme_obj.id)
        if not filme_db:
            raise ValueError("Filme não encontrado.")
        
        try:
            self.db.delete(filme_db)
            self.db.commit()
        except ValueError:
            print("Erro ao excluir filme")

    def get_filme_by_title(self, titulo):
        filme_list = []
        query = self.db.query(tb_filme).filter(tb_filme.titulo.like(f'%{titulo}%'))
        for filme in query:
            filme_list.append(self.map_filme_to_obj(filme))
        return filme_list
        


#---Diretor
    def get_diretor_by_id(self, id: int):
        return self.map_diretor_to_obj(self.db.query(tb_diretor).filter(tb_diretor.diretor_id == id).first())

    def get_diretor_by_name(self, nome: str):
        return self.db.query(tb_diretor).filter(tb_diretor.nome == nome).one()
    
    def get_all_diretor(self):
        diretores = self.db.query(tb_diretor).all()
        return [self.map_diretor_to_obj(d) for d in diretores]


    def add_diretor(self, diretor_obj: Diretor):
        diretor = self.map_diretor_to_tb_model(diretor_obj)
        self.db.add(diretor)
        self.db.commit()

    def map_diretor_to_obj(self, diretor: tb_diretor):
        diretor_obj = Diretor(diretor.nome)
        diretor_obj.id = diretor.diretor_id
        return diretor_obj
    
    def map_diretor_to_tb_model(self, diretor: Diretor):
        diretor_tb_model = tb_diretor(nome=diretor.nome)
        diretor_tb_model.diretor_id = diretor.id
        return diretor_tb_model
    
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
    
    def map_classificacao_to_tb_model(self, classificacao: Classificacao):
        classificacao_tb_model = tb_classificacao(descricao=classificacao.descricao)
        classificacao_tb_model.classificacao_id = classificacao.id
        return classificacao_tb_model
    
    def add_classificacao(self, classi: tb_classificacao):
        self.db.add(classi)
        self.db.commit()
    
   
#---Pais
    def get_pais_by_id(self, id: int):
        return self.map_pais_to_obj(self.db.query(tb_pais).filter(tb_pais.pais_id == id).first())
    
    def get_pais_by_name(self, name: str):
        return self.db.query(tb_pais).filter(tb_pais.nome == name).first()
    
    def get_all_pais(self):
        paises = self.db.query(tb_pais).all()
        return [self.map_pais_to_obj(p) for p in paises]
    
    def map_pais_to_obj(self, pais: tb_pais):
        pais_obj = Pais(pais.nome)
        pais_obj.id = pais.pais_id
        return pais_obj
    
    def map_pais_to_tb_model(self, pais: Pais):
        pais_tb_model = tb_pais(nome=pais.descricao)
        pais_tb_model.pais_id = pais.id
        return pais_tb_model


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
    
    def map_genero_to_tb_model(self, genero: Genero):
        genero_tb_model = tb_genero(descricao=genero.descricao)
        genero_tb_model.genero_id = genero.id
        return genero_tb_model
    

#---Filme_Genero
    def get_filme_genero_by_filme_id(self, id: int):
        return self.db.query(tb_filme_genero).filter(tb_filme_genero.filme_id == id).all()
    
    

#---Filme_Pais_Origem
    def get_filme_pais_origem_by_filme_id(self, id: int):
        return self.db.query(tb_filme_pais_origem).filter(tb_filme_pais_origem.filme_id == id).all()
