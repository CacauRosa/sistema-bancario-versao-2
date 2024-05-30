def menu(menu):
    menu = f"""
========== MENU ==========

1 - Depositar
2 - Sacar
3 - Extrato
4 - Criar usuário
5 - Criar conta corrente
6 - Listar contas
0 - Sair

==========================

Insira sua opção aqui: """

    return menu


def deposito(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R${valor_deposito:.2f} \n"
        print(f"\nDepósito de R${valor_deposito} realizado com sucesso!")

    else:
        print(f"\nValor inválido. Tente novamente inserindo um valor válido para o depósito.")
    
    return saldo, extrato


def saque(*, saldo, valor_saque, extrato, limite, num_saques, LIMITE_SAQUES):
    if valor_saque > saldo:
        print(f"\nSaldo insuficiente. Tente novamente.")

    elif valor_saque > limite:
        print(f"\nValor limite de saque de R${limite} ultrapassado. Tente novamente.")

    elif num_saques >= LIMITE_SAQUES:
        print(f"\nLimite de {LIMITE_SAQUES} saques diários ultrapassado. Volte amanhã!")

    elif valor_saque > 0:
        num_saques += 1
        saldo -= valor_saque
        extrato += f"Saque: R${valor_saque:.2f} \n" 
        print(f"\nSaque de R${valor_saque} realizado com sucesso!")

    else:
        print(f"\nValor inválido. Tente novamente inserindo um valor válido para o saque.")
    
    return saldo, extrato, num_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Nenhuma operação foi realizada." if not extrato else extrato)
    print(f"\nSaldo da conta: R${saldo:.2f}")
    print("=============================")


def criar_usuario(usuarios):
    cpf = input(f"\nInforme seu CPF (apenas números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print(f"\nJá existe um usuário com esse CPF! Tente novamente com outro CPF.")
        return

    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe seu endereço (logradouro, num - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})

    print(f"\nUsuário criado com sucesso!")


def filtrar_usuarios(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario


def criar_conta(AGENCIA, num_conta, usuarios, contas):
    cpf = input(f"\nInforme seu CPF (apenas números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print(f"\nConta criada com sucesso!")
        contas.append({"agencia": AGENCIA, "num_conta": num_conta, "usuario": usuario})
        return True
    
    print(f"\nUsuário não encontrado! Tente novamente com um usuário válido.")


def listar_contas(contas):
    for conta in contas:
        exibir = f"""
==========================

Agência: {conta["agencia"]}
Conta:   {conta["num_conta"]}
Usuário: {conta["usuario"]["nome"]}"""
        print(exibir)


def sair():
    print(f"\nObrigado pela preferência!")


def informacoes():
    saldo = 0
    limite = 500
    extrato = ""
    num_saques = 0
    LIMITE_SAQUES = 3

    AGENCIA = "0001"
    usuarios = []
    contas = []
    num_conta = 1

    while True:
        opcao = input(menu(menu))

        if opcao == "1":
            valor_deposito = float(input("Informe o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor_deposito, extrato)

        elif opcao == "2":
            valor_saque = float(input("Informe o valor que deseja sacar: "))
            saldo, extrato, num_saques = saque(saldo=saldo, valor_saque=valor_saque, extrato=extrato, limite=limite, num_saques=num_saques, LIMITE_SAQUES=LIMITE_SAQUES)

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            if criar_conta(AGENCIA, num_conta, usuarios, contas):
                num_conta += 1

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            sair()
            break

        else:
            print(f"\nOpcão inválida. Tente novamente selecionando uma das opções listadas no menu.")

informacoes()
