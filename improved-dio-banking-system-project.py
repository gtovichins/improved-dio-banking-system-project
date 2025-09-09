import re
from datetime import datetime, date


usuarios = []


contas = []


def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def formatar_cpf(cpf_numeros):
    cpf_numeros = re.sub(r'\D', '', cpf_numeros)
    if len(cpf_numeros) != 11:
        return None
    return f"{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:]}"

def validar_nome(nome_str):
    return bool(nome_str) and not any(char.isdigit() for char in nome_str)

def validar_endereco(endereco_str):
    padrao = r'^(.+),\s*(\d+)\s*-\s*(.+),\s*(.+)/([A-Za-z]{1,2})$'
    match = re.match(padrao, endereco_str.strip())
    if not match:
        return False
    numero = match.group(2)
    if not numero.isdigit():
        return False
    return True


def cadastrar_usuario():
    print("\n=== CADASTRO DE USUÁRIO ===")
    while True:
        nome = input("Nome completo: ").strip()
        if nome.lower() == "cancelar":
            print("Cadastro cancelado.\n")
            return
        if validar_nome(nome):
            break
        else:
            print("Formato incorreto para o nome. Não use números. Tente novamente.")

    while True:
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
        if data_nascimento.lower() == "cancelar":
            print("Cadastro cancelado.\n")
            return
        if validar_data(data_nascimento):
            break
        else:
            print("Formato incorreto para a data de nascimento. Tente novamente.")

    while True:
        cpf_input = input("CPF (apenas números): ").strip()
        if cpf_input.lower() == "cancelar":
            print("Cadastro cancelado.\n")
            return
        cpf_formatado = formatar_cpf(cpf_input)
        if not cpf_formatado:
            print("CPF inválido. Deve conter 11 números. Tente novamente.")
            continue
        if any(u['cpf'] == cpf_formatado for u in usuarios):
            print("Erro: já existe um usuário cadastrado com este CPF! Tente outro.")
            continue
        break

    while True:
        endereco = input("Endereço (Logradouro, número - Bairro, Cidade/UF): ").strip()
        if endereco.lower() == "cancelar":
            print("Cadastro cancelado.\n")
            return
        if validar_endereco(endereco):
            break
        else:
            print("Formato incorreto para o endereço. Número não pode ter letras e UF aceita no máximo 2 letras. Tente novamente.")

    usuario = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf_formatado,
        'endereco': endereco
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!\n")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.\n")
        return
    print("\n=== LISTA DE USUÁRIOS ===")
    for u in usuarios:
        print(f"Nome: {u['nome']}")
        print(f"Data de nascimento: {u['data_nascimento']}")
        print(f"CPF: {u['cpf']}")
        print(f"Endereço: {u['endereco']}")
        print("-" * 40)
    print()

def deletar_usuario():
    print("\n=== DELETAR USUÁRIO ===")
    cpf_input = input("Digite o CPF do usuário que deseja deletar (apenas números): ").strip()
    cpf_formatado = formatar_cpf(cpf_input)
    if not cpf_formatado:
        print("CPF inválido.\n")
        return
    usuario = next((u for u in usuarios if u['cpf'] == cpf_formatado), None)
    if not usuario:
        print("Usuário não encontrado.\n")
        return
    confirm = input(f"Tem certeza que deseja deletar o usuário {usuario['nome']}? (s/n): ").strip().lower()
    if confirm == 's':
        usuarios.remove(usuario)
        # Remove também todas as contas associadas
        contas_associadas = [c for c in contas if c['usuario']['cpf'] == cpf_formatado]
        for c in contas_associadas:
            contas.remove(c)
        print(f"Usuário {usuario['nome']} e suas contas foram deletados.\n")
    else:
        print("Operação cancelada.\n")


def criar_conta():
    if not usuarios:
        print("Não há usuários cadastrados.\n")
        return

    print("Para cancelar a operação a qualquer momento, digite 'cancelar'.\n")

    while True:
        cpf_input = input("Digite o CPF do usuário para criar a conta (apenas números): ").strip()
        if cpf_input.lower() == "cancelar":
            print("Operação cancelada.\n")
            return
        cpf_formatado = formatar_cpf(cpf_input)
        if not cpf_formatado:
            print("CPF inválido. Deve conter 11 números. Tente novamente.\n")
            continue

        usuario = next((u for u in usuarios if u['cpf'] == cpf_formatado), None)
        if not usuario:
            print("Usuário não encontrado. Tente novamente.\n")
            continue

        numero_conta = len(contas) + 1
        conta = {
            'agencia': "0001",
            'numero': numero_conta,
            'usuario': usuario,
            'saldo': 0.0,
            'extrato': [],
            'limite_saque': 500.0,
            'saques_max': 3,
            'numero_saques': 0,
            'numero_transacoes': 0,
            'limite_transacoes': 10,
            'data_ultima_transacao': None
        }
        contas.append(conta)
        print(f"Conta criada com sucesso! Agência: 0001, Número da conta: {numero_conta}, Titular: {usuario['nome']}\n")
        break

def acessar_conta():
    if not contas:
        print("Não há contas cadastradas.\n")
        return

    print("Para cancelar a operação a qualquer momento, digite 'cancelar'.\n")

    while True:
        cpf_input = input("Digite o CPF do usuário (apenas números): ").strip()
        if cpf_input.lower() == "cancelar":
            print("Operação cancelada.\n")
            return
        cpf_formatado = formatar_cpf(cpf_input)
        if not cpf_formatado:
            print("CPF inválido. Deve conter 11 números. Tente novamente.\n")
            continue

        usuario = next((u for u in usuarios if u['cpf'] == cpf_formatado), None)
        if not usuario:
            print("Usuário não encontrado. Tente novamente.\n")
            continue

        contas_usuario = [c for c in contas if c['usuario']['cpf'] == cpf_formatado]
        if not contas_usuario:
            print("Este usuário não possui contas.\n")
            return

        print(f"\nContas do usuário {usuario['nome']}:")
        for c in contas_usuario:
            print(f"Agência: {c['agencia']}, Número da conta: {c['numero']}")
        print()

        while True:
            conta_input = input("Digite o número da conta que deseja acessar: ").strip()
            if conta_input.lower() == "cancelar":
                print("Operação cancelada.\n")
                return

            try:
                numero_conta = int(conta_input)
            except ValueError:
                print("Número de conta inválido. Tente novamente.\n")
                continue

            conta = next((c for c in contas_usuario if c['numero'] == numero_conta), None)
            if not conta:
                print("Conta não encontrada. Tente novamente.\n")
                continue

            menu_conta(conta)
            return


def verificar_limite_diario(conta):
    hoje = date.today()
    if conta['data_ultima_transacao'] != hoje:
        conta['numero_transacoes'] = 0
        conta['numero_saques'] = 0
        conta['data_ultima_transacao'] = hoje


def depositar(saldo, valor, extrato, numero_transacoes, limite_transacoes, /):
    if numero_transacoes >= limite_transacoes:
        print("Limite diário de 10 transações atingido. Operação não permitida.\n")
        return saldo, extrato, numero_transacoes
    if valor <= 0:
        print("Valor inválido. Deve ser maior que zero.")
        return saldo, extrato, numero_transacoes
    saldo += valor
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    extrato.append(f"{agora} | Depósito | R${valor:.2f}")
    numero_transacoes += 1
    restante = limite_transacoes - numero_transacoes
    print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    print(f"Transações restantes hoje: {restante}\n")
    return saldo, extrato, numero_transacoes

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, numero_transacoes, limite_transacoes):
    if numero_transacoes >= limite_transacoes:
        print("Limite diário de 10 transações atingido. Operação não permitida.\n")
        return saldo, extrato, numero_saques, numero_transacoes
    if numero_saques >= limite_saques:
        print("Número máximo de saques atingido.")
        return saldo, extrato, numero_saques, numero_transacoes
    if valor <= 0:
        print("Valor inválido. Deve ser maior que zero.")
        return saldo, extrato, numero_saques, numero_transacoes
    if valor > saldo:
        print("Saldo insuficiente.")
        return saldo, extrato, numero_saques, numero_transacoes
    if valor > limite:
        print(f"Saque excede o limite de R${limite:.2f}.")
        return saldo, extrato, numero_saques, numero_transacoes

    saldo -= valor
    numero_saques += 1
    numero_transacoes += 1
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    extrato.append(f"{agora} | Saque    | R${valor:.2f}")
    restante = limite_transacoes - numero_transacoes
    print(f"Saque de R${valor:.2f} realizado com sucesso!")
    print(f"Transações restantes hoje: {restante}\n")
    return saldo, extrato, numero_saques, numero_transacoes

def consultar_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(f"{'Data/Hora':<20} | {'Operação':<8} | {'Valor':>10}")
        print("-"*50)
        for movimento in extrato:
            data_hora, tipo, valor = movimento.split(" | ")
            print(f"{data_hora:<20} | {tipo:<8} | {valor:>10}")
    print(f"\nSaldo: R${saldo:.2f}")
    print("==========================================\n")


def menu_conta(conta):
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[t] Transações restantes
[q] Sair
=> """
    while True:
        opcao = input(menu).lower()
        verificar_limite_diario(conta)
        if opcao == "d":
            while True:
                try:
                    valor = float(input("Informe o valor do depósito: "))
                except ValueError:
                    print("Valor inválido. Tente novamente.")
                    continue
                conta['saldo'], conta['extrato'], conta['numero_transacoes'] = depositar(
                    conta['saldo'], valor, conta['extrato'], conta['numero_transacoes'], conta['limite_transacoes']
                )
                conta['data_ultima_transacao'] = date.today()
                break
        elif opcao == "s":
            while True:
                try:
                    valor = float(input("Informe o valor do saque: "))
                except ValueError:
                    print("Valor inválido. Tente novamente.")
                    continue
                conta['saldo'], conta['extrato'], conta['numero_saques'], conta['numero_transacoes'] = sacar(
                    saldo=conta['saldo'],
                    valor=valor,
                    extrato=conta['extrato'],
                    limite=conta['limite_saque'],
                    numero_saques=conta['numero_saques'],
                    limite_saques=conta['saques_max'],
                    numero_transacoes=conta['numero_transacoes'],
                    limite_transacoes=conta['limite_transacoes']
                )
                conta['data_ultima_transacao'] = date.today()
                break
        elif opcao == "e":
            consultar_extrato(conta['saldo'], extrato=conta['extrato'])
        elif opcao == "t":
            restante = conta['limite_transacoes'] - conta['numero_transacoes']
            print(f"Transações restantes hoje: {restante}\n")
        elif opcao == "q":
            print(f"Saindo da conta {conta['usuario']['nome']}...\n")
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_principal():
    while True:
        print("---- BANCO ----")
        print("[1] Cadastrar usuário")
        print("[2] Listar usuários")
        print("[3] Criar conta")
        print("[4] Acessar conta")
        print("[5] Deletar usuário")
        print("[6] Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            criar_conta()
        elif opcao == "4":
            acessar_conta()
        elif opcao == "5":
            deletar_usuario()
        elif opcao == "6":
            print("Saindo do banco...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# --------------------------
# Executar programa
# --------------------------
menu_principal()
