negativa_conta=0
resp="S"
while resp =="S":
        nome_cliente=str(input("Informe o nome do cliente  "))
        num_conta=int(input("Digite o número da conta do cliente  "))
        saldo_conta=float(input("Digite o saldo da conta do cliente  "))
        if saldo_conta>=0:
            print("Saldo positivo")
        else:
            negativa_conta=negativa_conta+1
            print("Saldo negativo")
        print("Dados da Conta Bancária: Cliente:", nome_cliente , "; conta: ", num_conta , "; saldo da conta:", saldo_conta)
        resp=str(input("Deseja continuar a Cadastrar mais clientes? S/N  "))
        if resp=="N":
            resp2=str(input("Deseja imprimir o total de contas com saldo negativo? S/N  "))
            if  resp2=="S":
                 print("Exiba o total de contas negativas ", negativa_conta)

