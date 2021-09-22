mat=[]
for i in range(3):
    linha=[]
    for j in range(3):
        linha.append(int(input("Entre c/ numero: ")))
    mat.append(linha)
# Exercício 4 - Material Python Matriz
somas=[]
som=0
for i in range(3):
    som=sum(mat[i])
    somas.append(som)

maior=somas[0]
pos=0

for i in range(3):
    if (somas[i] > maior):
        maior=somas[i]
        pos=i
        
print(" *** Matriz *** ")
for i in range(3):
    print(mat[i])
print()
print(" Linha com maior soma ")
print(mat[pos])
print("A soma dessa linha é: ",maior)

                     

                     
                     
