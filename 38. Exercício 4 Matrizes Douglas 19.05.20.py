#Exercício 38 - Matrizes - Aula 19/05/2020 - Faça uma programa que leia
#uma matriz 3X3 de inteiros e retorne a linha de maior soma.
#Imprima na tela a matriz, a linha de maior soma e a soma.

matriz=[]

for i in range (3):
    linha=[]
    for j in range (3):
        linha.append(int(input("Digite o valor:   ")))
        matriz.append(linha)

somas=[]
som=0

for i in range (3):
    som=sum(matriz[i])
    somas.append(som)

maior=somas[0]
pos=0

for i in range(3):
    if (somas[i]>maior):
        maior=somas[i]
        pos=i
            
print("***Matriz****")
for i in range(3):
      print(matriz[i])

print()
print("Lista com a maior soma ")
print(matriz[pos])
print("A soma dessa linha é:  ", maior)


