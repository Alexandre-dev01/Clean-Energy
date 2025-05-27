import os

# ==== Arquivos ====
ARQ_USUARIOS = "usuarios.txt"
ARQ_PRODUTOS = "produtos.txt"
ARQ_FORUM = "forum.txt"
ARQ_GASTOS = "gastos.txt"
ARQ_AGENDAMENTOS = "agendamentos.txt"

# ==== Funções auxiliares ====
def carregar_usuarios():
    if not os.path.exists(ARQ_USUARIOS):
        return {}
    with open(ARQ_USUARIOS, "r") as f:
        return {u.split(",")[0]: u.strip().split(",")[1] for u in f}

def salvar_usuario(usuario, senha):
    with open(ARQ_USUARIOS, "a") as f:
        f.write(f"{usuario},{senha}\n")

def cadastrar_usuario():
    usuarios = carregar_usuarios()
    print("\n=== Cadastro ===")
    usuario = input("Usuário: ")
    if usuario in usuarios:
        print("Usuário já existe.")
        return
    senha = input("Senha: ")
    salvar_usuario(usuario, senha)
    print("Cadastro feito com sucesso!")

def login():
    usuarios = carregar_usuarios()
    print("\n=== Login ===")
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado com sucesso.")
        return usuario
    else:
        print("Usuário ou senha inválidos.")
        return None

# ==== Módulo 1: Gasto energético ====
def calcular_gasto_energetico(usuario):
    print("\n=== Cálculo de Gasto Energético ===")
    potencia = float(input("Potência do aparelho (em watts): "))
    horas = float(input("Horas de uso por dia: "))
    dias = int(input("Número de dias de uso: "))
    consumo = (potencia / 1000) * horas * dias
    preco_kwh = float(input("Preço do kWh (ex: 0.80): "))
    custo = consumo * preco_kwh
    print(f"Consumo total: {consumo:.2f} kWh")
    print(f"Custo estimado: R${custo:.2f}")

    with open(ARQ_GASTOS, "a") as f:
        f.write(f"{usuario},{consumo:.2f},{custo:.2f}\n")

# ==== Módulo 2: Marketplace ====
def marketplace(usuario):
    while True:
        print("\n=== Marketplace de Energia Limpa ===")
        print("1. Adicionar Produto")
        print("2. Ver Produtos")
        print("3. Comprar Produto")
        print("4. Voltar")

        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome do produto: ")
            preco = input("Preço: ").replace(",", ".")
            with open(ARQ_PRODUTOS, "a") as f:
                f.write(f"{nome}|{preco}|{usuario}\n")
            print("Produto adicionado.")

        elif op == "2":
            if not os.path.exists(ARQ_PRODUTOS):
                print("Nenhum produto disponível.")
                continue
            with open(ARQ_PRODUTOS, "r") as f:
                print("\n--- Produtos disponíveis ---")
                for linha in f:
                    try:
                        nome, preco, vend = linha.strip().split("|")
                        print(f"{nome} - R${preco} (Vendedor: {vend})")
                    except ValueError:
                        print("Produto com dados inválidos:", linha.strip())

        elif op == "3":
            produto = input("Digite o nome do produto que deseja comprar: ")
            comprado = False
            if os.path.exists(ARQ_PRODUTOS):
                with open(ARQ_PRODUTOS, "r") as f:
                    linhas = f.readlines()
                with open(ARQ_PRODUTOS, "w") as f:
                    for linha in linhas:
                        try:
                            nome, preco, vend = linha.strip().split("|")
                            if nome == produto and not comprado:
                                print(f"Produto '{produto}' comprado por R${preco} de {vend}.")
                                comprado = True
                            else:
                                f.write(linha)
                        except ValueError:
                            f.write(linha)  # Mantém a linha mesmo se inválida
                if not comprado:
                    print("Produto não encontrado.")
        elif op == "4":
            break
        else:
            print("Opção inválida.")


# ==== Módulo 3: Fórum ====
def forum(usuario):
    while True:
        print("\n=== Fórum de Energia Limpa ===")
        print("1. Ver posts")
        print("2. Criar post")
        print("3. Voltar")
        op = input("Escolha: ")

        if op == "1":
            if not os.path.exists(ARQ_FORUM):
                print("Nenhum post ainda.")
            else:
                print("\n--- Posts ---")
                with open(ARQ_FORUM, "r") as f:
                    for linha in f:
                        user, post = linha.strip().split(":", 1)
                        print(f"{user}: {post}")
        elif op == "2":
            texto = input("Escreva seu post: ")
            with open(ARQ_FORUM, "a") as f:
                f.write(f"{usuario}:{texto}\n")
            print("Post publicado.")
        elif op == "3":
            break
        else:
            print("Opção inválida.")

# ==== Módulo 4: Análise de Gastos ====
def analisar_gastos(usuario):
    total_kwh = 0
    total_custo = 0
    if os.path.exists(ARQ_GASTOS):
        with open(ARQ_GASTOS, "r") as f:
            for linha in f:
                user, consumo, custo = linha.strip().split(",")
                if user == usuario:
                    total_kwh += float(consumo)
                    total_custo += float(custo)
    print("\n=== Análise de Gastos ===")
    print(f"Total consumido: {total_kwh:.2f} kWh")
    print(f"Gasto total: R${total_custo:.2f}")

# ==== Módulo 5: Agendamento ====
def agendamento(usuario):
    while True:
        print("\n=== Agendamento de Instalação ===")
        print("1. Agendar serviço")
        print("2. Ver meus agendamentos")
        print("3. Voltar")
        op = input("Escolha: ")

        if op == "1":
            data = input("Data desejada (dd/mm/aaaa): ")

            print("\nEscolha o tipo de energia:")
            print("1. Energia Solar")
            print("2. Energia Eólica")
            tipo_op = input("Escolha: ")
            tipos = {"1": "Solar", "2": "Eólica"}
            tipo_energia = tipos.get(tipo_op)
            if not tipo_energia:
                print("Tipo inválido.")
                continue

            print("\nEscolha o tipo de serviço:")
            print("1. Instalação")
            print("2. Manutenção")
            servico_op = input("Escolha: ")
            servicos = {"1": "Instalação", "2": "Manutenção"}
            servico = servicos.get(servico_op)
            if not servico:
                print("Serviço inválido.")
                continue

            with open(ARQ_AGENDAMENTOS, "a") as f:
                f.write(f"{usuario},{data},{tipo_energia},{servico}\n")

            print(f"Agendamento confirmado para {data} - {tipo_energia} ({servico})")

        elif op == "2":
            print("\n--- Seus Agendamentos ---")
            if not os.path.exists(ARQ_AGENDAMENTOS):
                print("Nenhum agendamento encontrado.")
                continue

            with open(ARQ_AGENDAMENTOS, "r") as f:
                encontrados = False
                for linha in f:
                    user, data, tipo, serv = linha.strip().split(",")
                    if user == usuario:
                        print(f"Data: {data} | Energia: {tipo} | Serviço: {serv}")
                        encontrados = True
                if not encontrados:
                    print("Você ainda não tem agendamentos.")

        elif op == "3":
            break
        else:
            print("Opção inválida.")

# ==== Menu principal ====
def menu_principal():
    while True:
        print("\n=== Sistema Central ===")
        print("1. Cadastrar")
        print("2. Login")
        print("3. Sair")
        escolha = input("Escolha: ")

        if escolha == "1":
            cadastrar_usuario()
        elif escolha == "2":
            usuario = login()
            if usuario:
                while True:
                    print(f"\n=== Menu do Usuário: {usuario} ===")
                    print("1. Cálculo de Gasto Energético")
                    print("2. Marketplace de Energia Limpa")
                    print("3. Fórum")
                    print("4. Análise de Gastos")
                    print("5. Agendamentos")
                    print("6. Logout")
                    op = input("Escolha: ")

                    if op == "1":
                        calcular_gasto_energetico(usuario)
                    elif op == "2":
                        marketplace(usuario)
                    elif op == "3":
                        forum(usuario)
                    elif op == "4":
                        analisar_gastos(usuario)
                    elif op == "5":
                        agendamento(usuario)
                    elif op == "6":
                        print("Logout realizado.")
                        break
                    else:
                        print("Opção inválida.")
        elif escolha == "3":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida.")

# ==== Início do programa ====
menu_principal()
