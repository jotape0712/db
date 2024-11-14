from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Tabela Categoria
class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    produtos = relationship("Produto", back_populates="categoria")

# Tabela Produto
class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    fabricante = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    categoria = relationship("Categoria", back_populates="produtos")

# Tabela Cliente (Usuario)
class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    usuario = Column(String(50), unique=True, nullable=False)
    senha = Column(String(50), nullable=False)
    tipo = Column(String(10), nullable=False)  # Pode ser 'admin' ou 'usuario'

# Tabela Venda
class Venda(Base):
    __tablename__ = 'vendas'
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))
    produto_id = Column(Integer, ForeignKey('produtos.id'))
    quantidade = Column(Integer, nullable=False)
    total = Column(Float, nullable=False)
