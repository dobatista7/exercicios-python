# Exercício 31

matriz=[]
for i in range(3):
    linha=[]
    for j in range(3):
        linha.append(int(input("Diite o valor de:   ")))
        matriz.append(linha)
pares=0
for i in range(3):
    for j in range(3):
        if matriz[i][j]%2==0:
            pares=pares+1
for i in range(3):
    print(matriz[i])
print("A matriz contém",pares, "números pares")
