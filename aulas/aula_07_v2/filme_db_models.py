from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# --- Tabela País ---
class tb_pais(Base):
    __tablename__ = "pais"
    pais_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)

    estreias = relationship("tb_estreia", back_populates="pais")


# --- Tabela Associativa filme_estreia (chaves compostas) ---
class tb_filme_estreia(Base):
    __tablename__ = "filme_estreia"
    filme_id = Column(Integer, ForeignKey('filme.filme_id'), primary_key=True)
    estreia_id = Column(Integer, ForeignKey('estreia.estreia_id'), primary_key=True)


# --- Estreia com atributos extras (data e país) ---
class tb_estreia(Base):
    __tablename__ = "estreia"
    estreia_id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date, nullable=False)
    
    pais_id = Column(Integer, ForeignKey('pais.pais_id'), nullable=False)
    pais = relationship("tb_pais", back_populates="estreias")

    filmes = relationship("tb_filme", secondary="filme_estreia", back_populates="estreias")


# --- Filme ---
class tb_filme(Base):
    __tablename__ = "filme"
    filme_id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    ano_producao = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)

    diretor_id = Column(Integer, ForeignKey('diretor.diretor_id'), nullable=False)
    diretor = relationship("tb_diretor", back_populates="filmes")

    classificacao_id = Column(Integer, ForeignKey('classificacao.classificacao_id'), nullable=False)
    classificacao = relationship("tb_classificacao", back_populates="filmes")

    generos = relationship("tb_genero", secondary="filme_genero", back_populates="filmes")

    estreias = relationship("tb_estreia", secondary="filme_estreia", back_populates="filmes")


# --- Classificação ---
class tb_classificacao(Base):
    __tablename__ = "classificacao"
    classificacao_id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String, nullable=False)

    filmes = relationship("tb_filme", back_populates="classificacao")


# --- Diretor ---
class tb_diretor(Base):
    __tablename__ = "diretor"
    diretor_id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)

    filmes = relationship("tb_filme", back_populates="diretor")


# --- Gênero ---
class tb_genero(Base):
    __tablename__ = "genero"
    genero_id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String, nullable=False)

    filmes = relationship("tb_filme", secondary="filme_genero", back_populates="generos")


# --- Filme_Genero ---
class tb_filme_genero(Base):
    __tablename__ = "filme_genero"
    filme_id = Column(Integer, ForeignKey('filme.filme_id'), primary_key=True)
    genero_id = Column(Integer, ForeignKey('genero.genero_id'), primary_key=True)
