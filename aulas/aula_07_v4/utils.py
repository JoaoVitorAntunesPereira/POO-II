from filme_db_models import Base
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ============================================
# Configuração do sqlite
# ============================================

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///filmes.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
    
init_db()


    
