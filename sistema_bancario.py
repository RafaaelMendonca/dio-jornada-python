saldo_bancario = 0.0
opcao = 0
print("Bem-vindo ao site do banco brasesquio")
numero_de_saque_diario = 0
LIMITE_DIARIO = 3
LIMITE = 500.0

while True:
    print("\n")
    print("1- Depósito")
    print("2- Saque")
    print("3- Extrato bancário")
    print("4- Encerrar sistema")
    opcao = int(input("Escolha umas das opções disponíveis: "))
    

    if(opcao == 1):
        saldo_bancario += float (input("Insira o valor a ser depositado: "))

        while(saldo_bancario <= 0):
            print("Insira um valor válido")
            saldo_bancario = float (input("Informe o valor a ser depositado: "))

    elif(opcao == 2):

        saque = float (input("Insira o valor para saque: "))

        if(saque > saldo_bancario):
            print(f"Saldo insuficiente, saldo atual R$ {saldo_bancario:.2f}")

        elif(saque > LIMITE):
                print(f"Você só pode realizar saques de até R$ {LIMITE:.2f} reais.")

        elif(numero_de_saque_diario == LIMITE_DIARIO):
            print("Limite de saque diário atingido")

        else:
            saldo_bancario -= saque
            numero_de_saque_diario += 1
            print(f"Saque realizado com sucesso. saldo atual: R$ {saldo_bancario}")

    elif(opcao == 3):
        print(f"Saldo atual da conta: R$ {saldo_bancario:.2f}")

    elif(opcao == 4):
        print("Sistema encerrado!")
        break
        
    else:
        print("Comando incorreto")

