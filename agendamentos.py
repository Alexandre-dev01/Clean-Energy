from Marketingplace import ARQ_AGENDAMENTOS


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
