#calculadora
resp="s"
while resp=="s":
    n1=float(input("Digite o primeiro número:  "))
    n2=float(input("Digite o segundo número:   "))
    print("Escolha a operação desejada a partir da seguinte legenda")
    print("Soma =1 , Subtração = 2, Divisão = 3 e Multiplicação=4")
    op=int(input("Digite o número correspondente a operação desejada  "))
    if op==1:
           result=n1+n2
    elif op==2:
           result=n1-n2
    elif op==3:
           result=n1/n2
    elif op==4:
            result=n1*n2
    else:
         print("Operação não encontrada")
    print("O resultado da operação foi:  ", result)
    resp=str(input("Deseja continuar? S/N:  "))
print("Fim do programa")
   




   
