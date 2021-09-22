# 67. Lista III - Exercício 2 - Escreva um programa que preencha uma matriz 4X6 com
#números inteiros, calcule e mostre na tela:
#a) A quantidade de números que estão no intervalo entre 10 e 30:
#b) A soma dos números maiores que 10:
#c) A soma dos números que estão na quarta coluna da matriz:
#d) A média dos números da matriz que estão na terceira linha:

from random import randint
matriz=[]

for i in range(4):
    linha=[]
    for i in range(6):
        linha.append(randint(1,60))
    matriz.append(linha)

qtd=0;maiores=0;col=0;soma=0;media=0
for i in range(4):
    for j in range(6):
        if matriz[i][j] > 10 and matriz [i][j] < 30: #resolução a)
           qtd+=1
        if matriz[i][j] >10: #resolução b)
            maiores+=matriz[i][j]
        if j==3: #resolução c)
            col=(col+matriz[i][j])
        if i==2: #resolução d)
            soma=(soma+matriz[i][j])
                      
media=soma/len(matriz[i])

print("Exercício 2 Lista III - Matriz 4X6 - inteiros de 1 a 60")
print("")
for i in range(4):
    print(matriz[i])
print("")
print("A quantidade de números que estão no intervalo entre 10 e 30: ",soma)
print("A soma dos números maiores que 10:   ", maiores)
print("A soma dos números que estão na quarta coluna da matriz:   ", col)
print("A média dos números da matriz que estão na terceira linha:  ", media)
                    

