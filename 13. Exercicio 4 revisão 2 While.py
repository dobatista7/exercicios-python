#Revisão 2
# Exercício 13 com while - Faça um programa que receba um número inteiro.
# Calcule o fatorial desse número e mostre na tela.

n=int(input("Digite um número:  "))
cont=1
fatorial=1
while cont <=n:
    fatorial=fatorial*cont
    cont=cont+1

print("O fatorial de {} é " .format( n), fatorial)
    
