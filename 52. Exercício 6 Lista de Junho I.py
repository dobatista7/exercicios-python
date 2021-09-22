#Exercício 52 - Lista I - Exercício 6 - Lista de Junho
#Faça um programa que receba 10 números inteiros.
#Calcule o fatorial de cada número e mostre na tela.

for i in range(10):
    n=int(input(" Digite N:  "))
    fatorial=1
    for j in range (1, n+1):
        fatorial=fatorial*j
    print("O fatorial de {}:".format(n), "é", fatorial)


    
    
