# 66. Lista III - Exercício 1 -Escreva um programa que leia uma matriz de ordem 3X5
#de elementos inteiros. Calcule e mostre na tela:
# a) o menor número da matriz;
# b) a soma dos números múltiplos de 3 da matriz;
# c) a média dos números da matriz.

from random import randint 
matriz=[]

for i in range(3):
    linha=[]
    for j in range(5):
        linha.append(randint(1,50))
    matriz.append(linha)

menor=matriz[i][j]
media=0
soma=0
soma_1=0
for i in range(3):
    for j in range(5):
        if matriz[i][j]<menor: # resolução a)
            menor=matriz[i][j]
        if matriz[i][j]%3==0: # resolução b)
            soma+=matriz[i][j]
    soma_1+=(sum(matriz[i]))

media=((soma_1)/(len(matriz))) # resolução c)

print("Exercício 1 Lista III - Matriz 3X5 - Inteiros de 1 a 50")
print("")
for i in range (3):
    print(matriz[i])
print("")
print("O menor número da matriz:  ", menor)
print("A soma dos números múltiplos de 3 da matriz:  ", soma)
print("A média dos números da matriz:   ", media)


  
        
