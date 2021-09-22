#Exercício 7 (8) Faça um programa que receba dois números inteiros e a opção do tipo
#cálculo:
# 1-soma;
# 2 - subtração;
# 3 - multiplicação
# 4 - divisão

#Mostre o resultado na tela, conforme a opção de cálculo escolhida.

n=float(input("Digite um número:  "))
nn=float(input("Digite o segundo número:  "))
oper=int(input("Escoha a operação 1-Soma  2-Subtração  3-Multiplicação  4-Divisão:  "))
total=0.00

if oper==1:
         total=n+nn
         
       
elif oper==2:
    if nn>n:
        total=nn-n
    if n>nn:
        total=n-nn


elif oper==3:
    total=n*nn

    

elif oper==4:
    total=n/nn


print("O resultado da operação é:  ", total)
    
