# Menu de opções mostrado
def menu():
    menu = '''
    ==============Menu==============
    [1] Novo usuário
    [2] Nova conta
    [3] Listar contas
    [4] Depositar
    [5] Sacar
    [6] Extrato
    [0] Sair
    ================================
    => '''
    return input(menu)

def depositar(saldo,deposito,extrato,/):
    # Estrutura condicional para realizar o depósito com sucesso
        if deposito > 0:
           saldo = saldo + deposito
           extrato = extrato + str(f"DEP: R$ +{deposito}\n")     # Operação para adicionar no extrato os depósitos
           print("Depósito realizado com sucesso!")
           print("====================================")
        else:
            print("O valor informado inválido!")
            print("====================================")
        return saldo, extrato

  
    # Estrutura condicional para limite de número de saques 
def sacar(*, saldo, saque, extrato, limite, numero_saques):
        # Estrutura condicional para  limite de valor de saque e saldo positivo
        if saque <= limite and saque <= saldo:

                print( "Saque realizado com sucesso!")
                print( "Aguarde a contagem das notas!")
                print("=================================")
                saldo = saldo - saque
                numero_saques = numero_saques + 1

                extrato = extrato + str(f"SAQ: R$ -{saque}\n")        # Operação para adicionar no extrato os saques
                print(numero_saques)

        # Retorno quando a operação está acima do limite de saque    
        elif saque > limite:
                print("Operação não realizada, o valor excede o limite por saque!\nPor favor confira o valor e tente novamente.")

        # Retorno quando a operação está acima do valor do saldo
        elif saque > saldo:
                print("Operação não realizada, saldo insulficiente!\nPor favor confira o valor e tente novamente.")
        
        return saldo, extrato, numero_saques

def exibir_extrato(saldo, / , *, extrato):
        
        print("==============Extrato==============")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}") # configuração para R$ e valor
        print("===================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    #senha = input("Crie uma senha: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)
       

def main():
    # Variáveis de operações
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0 # número de saques feitos no dia
    LIMITE_SAQUES = 3 # Limite diário de saques
    usuarios = []
    contas = []

    while True:
        opcao = menu()

    # Configurção do menu de Criação de usuário
        if opcao == "1":
            criar_usuario(usuarios)

    # Configurção do menu de Criação de Contas
        elif opcao == "2":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

    # Configurção do menu de Listar contas
        elif opcao == "3":
            listar_contas(contas)
        
    # Configurção do menu de Depósito
        elif opcao == "4":
            print("==============Depósito==============")
            deposito = float(input("Digite o valor do Depósito: "))

            saldo, extrato = depositar( saldo, deposito, extrato)

    # Configuração do menu Saque
        elif opcao == "5" and numero_saques < LIMITE_SAQUES:
            print("==============Saque==============")
            saque = float(input("Digite o valor para o saque: "))
        
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                saque=saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
            )
         # Retorno quando limite diário do número de saques é atingido
        elif opcao == "5" and numero_saques >= LIMITE_SAQUES:
            print("Operação não realizada, você atingio o limite de saques diários!")
           

    # Configuração do menu Extrato
        elif opcao == "6":
            exibir_extrato(saldo, extrato=extrato)

     # Configurção do menu de saída  
        elif opcao == "0":
              print("Obrigado por usar nossos serviços!!!")
              print("====================================")
              break 
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")  

main()