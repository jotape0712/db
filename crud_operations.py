from database import obter_sessao, Cliente, Produto

# Função para criar um novo usuário
def criar_usuario(usuario, senha, tipo='usuario'):
    sessao = obter_sessao()
    novo_cliente = Cliente(usuario=usuario, senha=senha, tipo=tipo)
    try:
        sessao.add(novo_cliente)
        sessao.commit()
        print(f"Usuário {usuario} cadastrado com sucesso!")
    except Exception as e:
        sessao.rollback()
        print(f"Erro ao cadastrar usuário: {e}")
    finally:
        sessao.close()

# Função para autenticar o usuário
def autenticar_usuario(usuario, senha):
    sessao = obter_sessao()
    cliente = sessao.query(Cliente).filter_by(usuario=usuario, senha=senha).first()
    sessao.close()
    if cliente:
        return cliente
    else:
        return None

# Função para adicionar um produto
def adicionar_produto(nome, preco):
    sessao = obter_sessao()
    novo_produto = Produto(nome=nome, preco=preco)
    try:
        sessao.add(novo_produto)
        sessao.commit()
        print(f"Produto {nome} adicionado com sucesso!")
    except Exception as e:
        sessao.rollback()
        print(f"Erro ao adicionar produto: {e}")
    finally:
        sessao.close()

# Função para listar os produtos
def listar_produtos():
    sessao = obter_sessao()
    produtos = sessao.query(Produto).all()
    sessao.close()
    return produtos
