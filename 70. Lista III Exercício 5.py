#70. Lista III Exercício 5 - Escreva um programa que preencha uma matriz 4X3
#com números inteiros. Calcule e mostra na tela:
# a) A soma dos elementos que estão na 2ª e 4ª linha da matriz:
# b) A soma dos números primos

from random import randint

matriz=[]
primos=[]

for i in range (4):
    linha=[]
    for j in range (3):
        n=randint(1,50)
        linha.append(n)
    matriz.append(linha)

print("Exercício 5 Lista III - Matriz 4X3 randint 1 a 50")
print("")
for i in range(4):
    print(matriz[i])

soma=0
for i in range(4): # resolução a)
    for j in range(3):
        if i==1:
            soma=soma+matriz[i][j]
        if i==3:
            soma=soma+matriz[i][j]
       
cont_div=0
soma_1=0       
for i in range(4): # resolução b)
    for j in range(3):
        for k in range(1,matriz[i][j]+1):
            if matriz[i][j]%k==0:
                   cont_div+=1
        if cont_div==2:
            soma_1=soma_1+matriz[i][j]
            primos.append(matriz[i][j])
        cont_div=0

print("")
print("A soma dos elementos que estão na 2ª e 4ª linha da matriz: ",soma)# resolução a)
print("A soma dos números primos: ",soma_1)# resolução b)
print("Os números primos: ",primos)
        

    
