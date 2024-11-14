from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///banco.db"

Base = declarative_base()

# Modelo de Cliente (usuário)
class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)
    tipo = Column(String, nullable=False)  # 'admin' ou 'usuario'

# Modelo de Produto
class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)

# Função para criar as tabelas
def criar_tabelas():
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)

# Função para obter a sessão do banco
def obter_sessao():
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    Session = sessionmaker(bind=engine)
    return Session()

# Criar tabelas
criar_tabelas()
