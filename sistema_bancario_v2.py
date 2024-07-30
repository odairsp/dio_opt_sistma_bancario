import textwrap


def menu():

    menu = f"""\n
    {" BEM VINDO! ".center(50, "-")}\n
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] SAIR

    [nu] Novo Usuário
    [nc] Nova Conta 
    [lc] Listar Contas

    Escolha uma opção => """
    return input(textwrap.dedent(menu))


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    print(" SACAR ".center(50, "-") + "\n")
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saques:
        print("ERRO - Excedeu quantidade de saques diários!")

    else:

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite

        if excedeu_saldo:
            print(f"ERRO - Saldo = R$ {saldo:.2f} insuficiente! Digite outro valor!")

        elif valor <= 0:
            print("ERRO - Valor inválido! Repita a operação!")

        elif excedeu_limite:
            print(f"ERRO - Valor acima do limite de R$ {limite:.2f}.! Digite outro valor!")

        else:
            saldo -= valor
            numero_saques += 1
            extrato += "Saque ".ljust(40, "-") + " R$" + f"{valor:.2f}\n".rjust(10)
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            print(f"Saldo atual é de R$ {saldo:.2f}.")

    input(" Press Enter para voltar! ".center(50, "-"))
    return saldo, extrato, numero_saques


def depositar(saldo, valor, extrato, /):
    print(" DEPOSITAR ".center(50, "-")+"\n")

    if valor > 0:
        saldo += valor
        extrato += "Depósito ".ljust(40,"-")+" R$"+f"{valor:.2f}\n".rjust(10)

    else:
        print("ERRO - Valor inválido! Repita a operação!")

    input(" Press Enter para voltar! ".center(50, "-"))

    return saldo, extrato


def ver_extrato(saldo, /, *, extrato):
    print(" EXTRATO ".center(50, "-")+"\n")
    print("Nenhuma operação realizada!"if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}.")
    input(" Press Enter para voltar! ".center(50, "-"))


def novo_usuario(usuarios): 
    cpf = input("Entre com o cpf do novo usuário! --SOMENTE NUMEROS-- ")
    existe_usuario =  verifica_usuario(cpf, usuarios)
    if existe_usuario:
        print("Usuário já existe! ")
        input(" Press Enter para voltar! ".center(50, "-"))
    else:
        new_usuario = {
            "nome": input("Nome Completo: ").title(),
            "data_nascimento": input("Data de Nascimento (dd-mm-yyyy): "),
            "cpf": cpf,
            "endereco": input("Endereço completo (logradouro - nro - bairro - cidade/sigla estado)")
        }
        usuarios.append(new_usuario)
        print(f"\nUsuario - {new_usuario["nome"].title()}, criado com sucesso!")
        input(" Press Enter para voltar! ".center(50, "-"))
        return usuarios


def verifica_usuario(cpf, usuarios):

    user = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    return user[0] if user else None


def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Entre com o cpf do usuário! --SOMENTE NUMEROS-- ")
    usuario = verifica_usuario(cpf, usuarios)

    if usuario:
        print(f"Conta Ag. {agencia} - CC: {numero_conta}, Cliente {usuario["nome"]}, criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário inexistente! Tente novamente!")
        input(" Press Enter para voltar! ".center(50, "-"))


def listar_contas(contas):
    print(f"\n{" Contas Cadastradas! ".center(50, "-")}")
    for conta in contas:
        print(textwrap.dedent(f"""
            Agência\t\t{conta["agencia"]}
            CC.\t\t{conta["numero_conta"]}
            Titular\t\t{conta["usuario"]["nome"]}
            {"".center(50, "-")}
              """))    
    input(" Press Enter para voltar! ".center(50, "-"))


def program():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    contas = []
    usuarios = []
    AGENCIA = "0001"

    while True:
        print()        
        opcao = menu()

        if opcao == "d":
            valor = float(input("Digite o valor para depósito: => "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Digite o valor de saque: =>"))
            saldo, extrato, numero_saques = sacar(saldo = saldo, valor = valor, extrato= extrato,
                                                  limite = limite, numero_saques = numero_saques,
                                                  limite_saques = LIMITE_SAQUES)

            print(numero_saques, saldo)

        elif opcao == "e":
            ver_extrato(saldo, extrato=extrato)  

        elif opcao == "nu":
            usuarios = novo_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas)+1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":

            listar_contas(contas)

        elif opcao == "q":
            break


        else:
            print("Opção inválida, tente novamente!")

    print("Obrigado por usar nosso sistema!\n")


program()
