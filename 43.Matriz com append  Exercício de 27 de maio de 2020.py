# Exercício de 27.05.2020 - Soma coluna individualmente
#Escreva um programa que leia uma matriz 5X6:,
#some as colunas individualmente e acumule as somas
#na 6ª linha da matriz. Imprima a matriz inteira e
#mostrando inclusive os valores da 6ª linha.

from random import randint
matriz=[]

for i in range(6):
    linha=[]
    for j in range(6):
        linha.append(randint(1,40))
    matriz.append(linha)

for j in range(6):
    soma=0
    for i in range(5):
        soma=soma+matriz[i][j]
    matriz[5][j]=soma

for i in range(6):
    print(matriz[i])
    
         
