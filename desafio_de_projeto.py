
# Menu de opções mostrado
menu = '''
==============Menu==============
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
================================
=> '''

# Variáveis de operações
saldo = 0
limite = 500
extrato = ""
numero_saques = 0 # número de saques feitos no dia
LIMITE_SAQUES = 3 # Limite diário de saques

while True:

    opcao = input(menu)
# Configurção do menu de Depósito
    if opcao == "1":
        print("==============Depósito==============")
        deposito = float(input("Digite o valor do Depósito: "))
    # Estrutura condicional para realizar o depósito com sucesso
        if deposito > 0:
           saldo = saldo + deposito
           extrato = extrato + str(f"DEP: R$ +{deposito}\n")     # Operação para adicionar no extrato os depósitos
           print("Depósito realizado com sucesso!")
           print("====================================")

# Configuração do menu Saque  
    # Estrutura condicional para limite de número de saques         
    elif opcao == "2" and numero_saques < LIMITE_SAQUES:
        print("==============Saque==============")
        saque = float(input("Digite o valor para o saque: "))
        # Estrutura condicional para  limite de valor de saque e saldo positivo
        if saque <= limite and saque <= saldo: 

                print( "Saque realizado com sucesso!")
                print( "Aguarde a contagem das notas!")
                print("=================================")
                saldo = saldo - saque
                numero_saques = numero_saques + 1
                extrato = extrato + str(f"SAQ: R$ -{saque}\n")        # Operação para adicionar no extrato os saques

        # Retorno quando a operação está acima do limite de saque    
        elif saque > limite:
                print("Operação não realizada, o valor excede o limite por saque!\nPor favor confira o valor e tente novamente.")

        # Retorno quando a operação está acima do valor do saldo
        elif saque > saldo:
                print("Operação não realizada, saldo insulficiente!\nPor favor confira o valor e tente novamente.")

    # Retorno quando limite diário do número de saques é atingido
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação não realizada, você atingio o limite de saques diários!")

# Configuração do menu Extrato
    elif opcao == "3":
        print("==============Extrato==============")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}") # configuração para R$ e valor
        print("===================================")

# Configuração do menu Sair
    elif opcao == "0":
        print("Obrigado por usar nossos serviços!!!")
        print("====================================")
        break
       

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


