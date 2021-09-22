#1) Exercicio 1 - Matriz Diagonal - 20/05/2020
#Escreva um programa que preencha uma matriz de
# ordem 5X5 de elementos inteiros, calcule e mostre na tela:
#o maior número da diagonal principal da matriz;
#o maior número da coluna 2, ou seja, indice 1;
# a quantidade de números da matriz que são maiores que
# a média dos números da matriz;

matriz=[]
for i in range(3):
    linha=[]
    for j in range (3):
        linha.append(int(input("Digite um número: ")))
    matriz.append(linha)
print(matriz)

diagonal=[]
maior=0
for i in range (3):
    for j in range (3):        
           if [i]==[j]:
               diagonal.append(i+j)
               if diagonal[i]>maior:
                   maior=maior+diagonal[i]
                   if matriz[0][1]>matriz[i][j]
print(diagonal)
print(maior)



