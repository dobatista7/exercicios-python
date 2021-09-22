#Revisão 2
# Exercício 12 com for - Faça um programa que receba um número inteiro.
# Calcule o fatorial desse número e mostre na tela.


n=int(input("Digite um número:  "))

fatorial=1
for i in range (1, n+1):
    fatorial=fatorial*i
    
print("O fatorial de {} é:  ".format(n), fatorial)
