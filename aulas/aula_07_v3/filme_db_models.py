from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class tb_filme_pais_origem(Base):
    __tablename__ = "filme_pais_origem"
    filme_id = Column(Integer, ForeignKey("filme.filme_id"), primary_key=True)
    pais_id = Column(Integer, ForeignKey("pais.pais_id"), primary_key=True)

class tb_pais(Base):
    __tablename__ = "pais"
    pais_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)

    filmes_origem = relationship("tb_filme", secondary="filme_pais_origem", back_populates="paises_origem")

class tb_diretor(Base):
    __tablename__ = "diretor"
    diretor_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    filmes = relationship("tb_filme", back_populates="diretor")

class tb_classificacao(Base):
    __tablename__ = "classificacao"
    classificacao_id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String, nullable=False)
    filmes = relationship("tb_filme", back_populates="classificacao")

class tb_genero(Base):
    __tablename__ = "genero"
    genero_id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String, nullable=False)

    filmes = relationship("tb_filme", secondary="filme_genero", back_populates="generos")

class tb_filme_genero(Base):
    __tablename__ = "filme_genero"
    filme_id = Column(Integer, ForeignKey("filme.filme_id"), primary_key=True)
    genero_id = Column(Integer, ForeignKey("genero.genero_id"), primary_key=True)

class tb_filme(Base):
    __tablename__ = "filme"
    filme_id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    ano_producao = Column(Integer)
    data_estreia = Column(Date)
    duracao = Column(Integer)
    sinopse = Column(String, nullable=False)
    is_active = Column(Boolean)

    diretor_id = Column(Integer, ForeignKey("diretor.diretor_id"))
    classificacao_id = Column(Integer, ForeignKey("classificacao.classificacao_id"))
    pais_estreia_id = Column(Integer, ForeignKey("pais.pais_id"))

    diretor = relationship("tb_diretor", back_populates="filmes")
    classificacao = relationship("tb_classificacao", back_populates="filmes")
    pais_estreia = relationship("tb_pais")
    generos = relationship("tb_genero", secondary="filme_genero", back_populates="filmes")
    paises_origem = relationship("tb_pais", secondary="filme_pais_origem", back_populates="filmes_origem")
