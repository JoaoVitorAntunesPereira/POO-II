from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class tb_filme_genero(Base):
    __tablename__ = "filme_genero"
    filme_id = Column(Integer, ForeignKey('filme.filme_id'), primary_key=True)
    genero_id = Column(Integer, ForeignKey('genero.genero_id'), primary_key=True)


class tb_diretor(Base):
    __tablename__ = "diretor"
    diretor_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False) 
    
    filmes = relationship("tb_filme", back_populates="diretor")


class tb_genero(Base):
    __tablename__ = "genero"
    genero_id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String, nullable=False)

    filmes = relationship("tb_filme", secondary="filme_genero", back_populates="generos")


class tb_filme(Base):
    __tablename__ = "filme"
    filme_id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    ano_producao = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

    diretor_id = Column(Integer, ForeignKey('diretor.diretor_id'), nullable=False)
    diretor = relationship("tb_diretor", back_populates="filmes")

    generos = relationship("tb_genero", secondary="filme_genero", back_populates="filmes")
