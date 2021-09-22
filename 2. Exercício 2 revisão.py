#Exercício 2 Faça um programa que receba dez números, calcule e mostre na tela:
# a soma dos números pares
# a quantidade de números inferiores a 10

soma=0
i=0
inf=0
while i <10:
    num=int(input("Digite um número:  "))
    if num % 2 ==0:
        soma=soma+num
    if num < 10:
        inf=inf+1
    i=i+1
print("A soma dos números pares digitados totalizou  ", soma)
print(" A quantidade de números digitados inferiores a 10 foram  ", inf)
