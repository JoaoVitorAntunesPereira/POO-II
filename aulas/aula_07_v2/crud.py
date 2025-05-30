from db_models import Base, tb_diretor, tb_filme
from models import Diretor, Filme, Genero
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

# ============================================
# Configuração do sqlite
# ============================================

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///filmes.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)



def get_filmes(db: Session):
    return db.query(tb_filme).filter().all()

def get_diretor_by_id(db: Session, id: int):
    return db.query(tb_diretor).filter(tb_diretor.diretor_id == id).first()

def get_diretor_by_name(db: Session, nome: str):
    return db.query(tb_diretor).filter(tb_diretor.nome == nome).one()

def add_diretor(db: Session, diretor_obj: Diretor):
    diretor = tb_diretor(
        nome = diretor_obj.nome
    )
    
    db.add(diretor)
    db.commit()


def map_diretor(diretor: tb_diretor):
    diretor_obj = Diretor(diretor.nome)
    diretor_obj.id = diretor.diretor_id
    
    return diretor_obj

def add_filme(db: Session, filme_obj: Filme):
    # INSERT INTO filmes ...
    print("ID do diretor recebido:", filme_obj.diretor.id)
    generos_str = ', '.join(g.value for g in filme_obj.genero)
    
    diretor = get_diretor_by_id(db, filme_obj.diretor.id)
    
    filme = tb_filme(
        titulo = filme_obj.titulo,
        ano_producao = filme_obj.ano_producao,
        generos = generos_str,
        diretor = diretor
    )
    db.add(filme)  # insere na tabela
    db.commit()    # confirma a transação 
    
