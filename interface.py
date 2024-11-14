import tkinter as tk
from tkinter import messagebox
from crud_operations import criar_usuario, autenticar_usuario, adicionar_produto, listar_produtos

# Função para criar a interface de login
def criar_interface_login():
    def login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        cliente = autenticar_usuario(usuario, senha)
        
        if cliente:
            messagebox.showinfo("Login", f"Bem-vindo, {usuario}!")
            if cliente.tipo == 'admin':
                criar_interface_admin()
            else:
                criar_interface_usuario()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    janela_login = tk.Tk()
    janela_login.title("Login")

    tk.Label(janela_login, text="Usuário:").pack()
    entry_usuario = tk.Entry(janela_login)
    entry_usuario.pack()

    tk.Label(janela_login, text="Senha:").pack()
    entry_senha = tk.Entry(janela_login, show="*")
    entry_senha.pack()

    tk.Button(janela_login, text="Entrar", command=login).pack()

    tk.Button(janela_login, text="Cadastrar novo usuário", command=criar_interface_cadastro).pack()

    janela_login.mainloop()

# Função para criar a interface de cadastro de cliente
def criar_interface_cadastro():
    def cadastrar():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        tipo = entry_tipo.get()  # Pode ser 'admin' ou 'usuario'

        if usuario and senha:
            criar_usuario(usuario, senha, tipo)
            messagebox.showinfo("Cadastro", f"Usuário {usuario} cadastrado com sucesso!")
            janela_cadastro.destroy()
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    janela_cadastro = tk.Tk()
    janela_cadastro.title("Cadastro de Usuário")

    tk.Label(janela_cadastro, text="Usuário:").pack()
    entry_usuario = tk.Entry(janela_cadastro)
    entry_usuario.pack()

    tk.Label(janela_cadastro, text="Senha:").pack()
    entry_senha = tk.Entry(janela_cadastro, show="*")
    entry_senha.pack()

    tk.Label(janela_cadastro, text="Tipo (admin/usuario):").pack()
    entry_tipo = tk.Entry(janela_cadastro)
    entry_tipo.pack()

    tk.Button(janela_cadastro, text="Cadastrar", command=cadastrar).pack()

    janela_cadastro.mainloop()

# Função para criar a interface do Admin
def criar_interface_admin():
    def adicionar_produto_interface():
        def adicionar():
            nome = entry_nome.get()
            preco = entry_preco.get()

            if nome and preco:
                adicionar_produto(nome, float(preco))
                messagebox.showinfo("Produto", f"Produto {nome} adicionado com sucesso!")
            else:
                messagebox.showerror("Erro", "Preencha todos os campos!")

        janela_admin = tk.Tk()
        janela_admin.title("Adicionar Produto")

        tk.Label(janela_admin, text="Nome do Produto:").pack()
        entry_nome = tk.Entry(janela_admin)
        entry_nome.pack()

        tk.Label(janela_admin, text="Preço do Produto:").pack()
        entry_preco = tk.Entry(janela_admin)
        entry_preco.pack()

        tk.Button(janela_admin, text="Adicionar Produto", command=adicionar).pack()

        janela_admin.mainloop()

    janela_admin = tk.Tk()
    janela_admin.title("Interface do Admin")

    tk.Label(janela_admin, text="Bem-vindo, Admin!").pack()

    tk.Button(janela_admin, text="Adicionar Produto", command=adicionar_produto_interface).pack()

    janela_admin.mainloop()

# Função para criar a interface do Usuário
def criar_interface_usuario():
    janela_usuario = tk.Tk()
    janela_usuario.title("Interface do Usuário")

    tk.Label(janela_usuario, text="Bem-vindo, Usuário!").pack()

    # Listar produtos disponíveis
    produtos = listar_produtos()

    if produtos:
        for produto in produtos:
            tk.Label(janela_usuario, text=f"Produto: {produto.nome}, Preço: R${produto.preco}").pack()
    else:
        tk.Label(janela_usuario, text="Nenhum produto disponível").pack()

    janela_usuario.mainloop()
