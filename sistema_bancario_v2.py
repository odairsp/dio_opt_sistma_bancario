
def menu(): 
    menu =" BEM VINDO! ".center(50,"-") + """
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
 
    Escolha uma opção => """
    return input(menu)


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    print(" SACAR ".center(50,"-")+"\n")
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saques: 
        print(f"ERRO - Excedeu quantidade de saques diários!")
    
    else: 
        saque = float(input("Digite o valor de saque: =>"))
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        
        if excedeu_saldo:
            print(f"ERRO - Saldo = R$ {saldo:.2f} insuficiente! Digite outro valor!")
            
        elif saque <= 0:
            print("ERRO - Valor inválido! Repita a operação!")
            
        elif saque > limite:
            print(f"ERRO - Valor acima do limite de R$ {limite:.2f}.! Digite outro valor!")
            
        else:  
            saldo -= saque
            numero_saques += 1
            extrato += "Saque ".ljust(40,"-") + " R$"+ f"{saque:.2f}\n".rjust(10)
            print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
            print(f"Saldo atual é de R$ {saldo:.2f}.")
            
    print("".center(50,"-")+"\n")


    return saldo, extrato, numero_saques

def depositar(saldo, valor, extrato, /):
    print(" DEPOSITAR ".center(50,"-")+"\n")

    if valor > 0:
        saldo += valor
        extrato += "Depósito ".ljust(40,"-")+" R$"+f"{valor:.2f}\n".rjust(10)
        
    else:
        print("ERRO - Valor inválido! Repita a operação!")
    
    print("".center(50,"-")+"\n")
               
    return saldo, extrato

def ver_extrato(saldo, /, *, extrato):
    print(" EXTRATO ".center(50,"-")+"\n")
    print("Nenhuma operação realizada!"if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}.")
    input(" Press Enter para voltar! ".center(50, "-"))

def nova_conta():
    return False
def listar_contas():
    return False
def novo_usuario(usuarios): 
    cpf = input("Entre com o cpf do novo usuário! --SOMENTE NUMEROS-- ")
    existe_usuario =  verifica_usuario(cpf)
    if existe_usuario:
        print("Usuário já existe! ")
    else:
        novo_usuario = {
            "nome": input("Nome Completo"),
            "data_nascimento": input("Data de Nascimento (dd-mm-yyyy): "),
            "cpf": cpf,
            "endereco": input("Endereço completo (logradouro - nro - bairro - cidade/sigla estado)")
        }
        usuarios.append(novo_usuario)
    return usuarios
def verifica_usuario(cpf, usuarios):
    user = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    
    return user[0] if user else None

def program():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    contas = []
    usuarios=[]

    while True:
        print()        
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Digite o valor para depósito: => "))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":
            saldo, extrato,numero_saques = sacar(saldo=saldo, valor=valor,extrato=extrato,limite=limite,\
                                   numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)
                
        elif opcao == "e":
            ver_extrato(saldo, extrato=extrato)  
            
        elif opcao == "nu":
            usuarios = novo_usuario(usuarios)

        elif opcao == "q":
            break
            
        
        else:
            print("Opção inválida, tente novamente!")
        
    print("Obrigado por usar nosso sistema!\n")

program();