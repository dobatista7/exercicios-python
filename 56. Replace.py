# Exercício 56 - 09.06.20 - Faça um programa que preencha uma mtriz com as seguintes
#informações: código do produto, nome do produto, preço. Depois de preenchida
#a matriz deve ser feita alterações no nome do produto, use o método replace().
#Peça na tela onome do produto que será  substituido e novo nome. No final imprima
#a matriz na tela.

e=3
matriz=[]

for i in range(e):
    linha=[]
    linha.append(cod)
    linha.append(str(input("Nome Produto:  ")))
    linha.append(float(input("Preço:  ")))
    matriz.append(linha)
    cod+=1

prod=str(input("Produto a ser alterado:  "))
prod_a=str(input("Nova descrição:   "))

for i in range (e):
    if busca.lower() in matriz[i][1].lower:
        mat[i][1]=mat[i][1].replace(prod,prod_a)

for i in range (e):
    print(matriz[i])
        
