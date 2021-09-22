# Exercício - 32(13/05/2020) Faça um programa que preencha uma matriz 2X4. Calcule e mostre:
#a quantidade de elmentos pares:
# a soma dos elementos ímpares.

matriz=[]
for i in range (2):
    linha=[]
    for j in range (4):
        linha.append(int(input("digite o valor de: ")))
        matriz.append(linha)
pares=0
impares=0
soma_impar=0
for i in range(2):
    for j in range(4):
        if matriz[i][j]%2==0:
            pares=pares +1
        else:
            impares=impares+1
            soma_impar=(soma_impar)+(matriz[i][j])
for i in range(4):
    print(matriz[i])
print(" A matriz contém", pares, "números pares")
print(" A matriz contém", impares, "número impares")
print("A a soma dos elementos ímpares", soma_impar)
