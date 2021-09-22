#42) Exercicio 1 - Matriz Diagonal - 20/05/2020
#Escreva um programa que preencha uma matriz de
# ordem 5X5 de elementos inteiros, calcule e mostre na tela:
#o maior número da diagonal principal da matriz;
#o maior número da coluna 2, ou seja, indice 1;
#a quantidade de números da matriz que são maiores que a média dos números da matriz;

from random import randint
matriz=[]
for i in range(5):
    linha=[]
    for j in range (5):
        linha.append(randint(10,60))
        matriz.append(linha)

soma=0
num=matriz[0][0]
maior=matriz[0][1]
qtd=0
for i in range (5):
    print(matriz[i])
    soma+=sum(matriz[i])
media=soma/25
for i in range (5):
    for j in range(5):
        if i== j and matriz[i][j] >num:
            num=matriz[i][j]
        if j==1 and matriz[i][j]>maior:
            maior= matriz[i][j]
        if matriz[i][j]>media:
            qtd+=1
            
print("o maior número da diagonal principal é: ",num)
print("o maior número da coluna 2 é:  ", maior)
print("A média da matriz é:  ", media)
print("A quantidade de números maiores que a média é:  ", qtd)


