import os

ARQUIVO_USUARIOS = "usuarios.txt"

def carregar_usuarios():
    usuarios = {}
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r") as f:
            for linha in f:
                usuario, senha = linha.strip().split(",")
                usuarios[usuario] = senha
    return usuarios

def salvar_usuario(usuario, senha):
    with open(ARQUIVO_USUARIOS, "a") as f:
        f.write(f"{usuario},{senha}\n")

def cadastrar():
    usuarios = carregar_usuarios()
    print("\n============================ Tela de Cadastro ============================")
    usuario = input("Escolha um nome de usuário: ")
    
    if usuario in usuarios:
        print("Usuário já existe. Tente outro nome.")
        return
    
    senha = input("Escolha uma senha: ")
    salvar_usuario(usuario, senha)
    print("Cadastro realizado com sucesso!")

def login():
    usuarios = carregar_usuarios()
    print("\n=== Tela de Login ===")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login bem-sucedido! Bem-vindo,", usuario)
    else:
        print("Usuário ou senha incorretos.")

def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Cadastrar")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            login()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Início do programa
menu()
