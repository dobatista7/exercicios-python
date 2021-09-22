# Exercício 33 -(13.05.2020 entrega em 20.05.2020) Faça um programa que
#preencha uma matriz 3X4, calcule e mostre:
#A média de todos os elementos:
#A quantidade de elementos maiores que a média

matriz=[]
for i in range (3):
    linha=[]
    for j in range (4):
        linha.append(int(input("Digite o valor de :   ")))
        matriz.append(linha)

soma=0
quan=0
for i in range(3):
    soma+=sum(matriz[i])
    qtd+=len(matriz[i])
media=soma/quan
maior=0    
for i in range(3):
    for j in range(4):
        if matriz[i][j]>media:
            maior+=1
            
for i in range(3):
    print(matriz[i])

print("Soma dos elementos da Matriz", soma)
print("Quantidade de elementos na Matriz", quan)
print("A média de todos os elementos ", media)
print("A quantidade de elementos maiores que a média ", maior)

