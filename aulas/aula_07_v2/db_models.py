from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

""" 
Classe que representa a entidade Filme
"""

Base = declarative_base()


class tb_diretor(Base):
    __tablename__ = "diretor"
    diretor_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False) 
    
    filme = relationship("tb_filme", back_populates="diretor", uselist=False)

class tb_filme(Base):
    __tablename__ = "filme"
    filme_id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    ano_producao = Column(Integer, nullable=False)
    generos = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    
    diretor_id = Column(Integer, ForeignKey('diretor.diretor_id'), nullable=False, unique=True)
    diretor = relationship("tb_diretor", back_populates="filme", uselist=False)
