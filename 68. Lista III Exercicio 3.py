# 68. Lista III - Exercício 3 - Escreva um programa que leia uma matriz 5X4 onde 
#1ª coluna da matriz são armazenadas os nomes dos vendedores
#da 2ª coluna a 4ª coluna são armazenados os totais de vendas por mês.
#Calcule e mostre na tela: 
#a) O valor total vendido por vendedor:
#b) A maior venda do mês 1:
#c) A menor venda do mês 3:
#d) O total vendido por mês:

from random import randint
matriz=[]
e=5

print("Exercício 3 Lista III - Matriz 5X4 - random de 90,00 a 5,000")
print("")
for i in range(e):
    linha=[]
    linha.append(str(input(f"Vendedor nº: {i}  ")))
    linha.append(float(randint(90,5000)))
    linha.append(float(randint(90,5000)))
    linha.append(float(randint(90,5000)))
    matriz.append(linha)
print("")
print("Vendedor  Mês1   Mês2   Mês3")
for i in range(e):
    print(matriz[i])
print("")

vend_1=0;vend_2=0;vend_3=0;vend_4=0;vend_5=0 # resolução a)
for i in range(e): 
    for j in range(1,4):
        if i==0:
            vend_1+=matriz[0][j]
        elif i==1:
            vend_2+=matriz[i][j]
        elif i==2:
            vend_3+=matriz[i][j]
        elif i==3:
            vend_4+=matriz[i][j]
        elif i==4:
            vend_5+=matriz[i][j]
            
print("") # resolução a)
print("O valor total vendido por vendedor no trimestre ")
print(matriz[0][0],":R$", vend_1, matriz[1][0],":R$",vend_2, matriz[2][0],":R$",vend_3)
print(matriz[3][0],"R$",  vend_4, matriz[4][0],"R$", vend_5)

print("")
maior=matriz[0][1];menor=matriz[0][3]
for i in range(e):
    if matriz[i][1]>maior: # resolução b)
        maior=matriz[i][1]
    if matriz[i][3]<menor: #resolução c)
        menor=matriz[i][3]   
    
print(" A maior venda do mês 1: ",maior)
print(" A menor venda do mês 3: ", menor)

mes_1=0;mes_2=0;mes_3=0
for i in range(e): #resolução d)
    for j in range(1,4):
        if j==1:
            mes_1+=matriz[i][j]
        elif j==2:
            mes_2+=matriz[i][j]
        elif j==3:
            mes_3+=matriz[i][j]

print("")
print("O valor total vendido por mês ")
print("Mês 1: ", mes_1, "Mês 2: ",mes_2,"Mês 3:", mes_3)

        
    
            
        



    
