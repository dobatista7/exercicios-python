#Exercício de 19.05.20 para entrega em 25.05.2020
#Faça um programa que leia duas matrizes A e B 2x2 de inteiros e
#imprima a matriz C que é a soma das matrizes A e B.

M_A=[]
M_B=[]
for i in range (2):
    linha=[]
    for j in range(2):
        linha.append(int(input("Digite o valor:    ")))
        M_A.append(linha)

for i in range(2):
    print("Matriz A", M_A)

for i in range (2):
    linha=[]
    for j in range(2):
        linha.append(int(input("Digite o valor:    ")))
        M_B.append(linha)

for i in range (2):
    print("Matriz B", M_B[i])

M_C=[]
for i in range(2):
    linha=[]
    for j in range(2):
        linha.append(M_A[i]+M_B[i])
        M_C.append(linha)
       

for i in range (2):
    print("Matriz C", M_C[i])

        

