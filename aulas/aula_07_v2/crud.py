from db_models import Base, db_filme
from models import Filme, Genero
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
    return db.query(filme).filter().all()


def add_filme(db: Session, filme_obj: Filme):
    # INSERT INTO filmes ...
    filme = Filme(
        titulo = filme_obj.titulo,
        ano = filme_obj.ano,
        #genero = filme_obj.genero
    )
    db.add(filme)  # insere na tabela
    db.commit()    # confirma a transação 