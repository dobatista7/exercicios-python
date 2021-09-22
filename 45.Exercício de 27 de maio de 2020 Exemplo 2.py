#45) Exercício de 27 de maio de 2020
#Faça um programa que, leia uma matriz 4x3 com os números inteiros.
#Calcule e mostre na tela:
#◦A média dos números da 3ª linha
#◦A Soma dos números da 2ª coluna

from random import randint
matriz=[]
for i in range (4):
    linha=[]
    for j in range(3):
        n=randint(1,10)
        linha.append(n)
    matriz.append(linha)

for i in range(4):
    print(matriz[i])

print()

soma_col=0
soma=0
media=0

for i in range(4):
    for j in range(3):
        if j==1:
            soma_col=soma_col+matriz[i][j]
        if i ==2:
            soma=soma+matriz[i][j]

media=soma/3

print("Soma da 2ª coluna: ", soma_col)
print("Média da 3ª linha:  ", media)
