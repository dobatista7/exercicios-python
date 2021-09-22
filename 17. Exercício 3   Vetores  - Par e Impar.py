#Exercício 17 - Vetores
#Faça um programa que leia 10 números inteiros e armazene em uma lista

lista=[0]*10
listapar=[]
listaimpar=[]

for i in range (10):
    lista[i]=int(input("Digite um número:  "))
    if lista[i]% 2 ==0:
        listapar.append(lista[i])
    else:
        listaimpar.append(lista[i])

print(lista)
print(listapar)
print(listaimpar)
    
    
