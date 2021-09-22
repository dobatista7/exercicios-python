# Exercício 34 -  da Aula de 05.05.2020 - Vetores
# Faça um programa em Python que preencha uma lista com 6 números inteiros.
#Calcule e mostre na tela:
# 1)Os números pares
# 2)A soma dos números pares
# 3)Os números ímpares
# 4)A média dos números ímpares

e=6
lista=[]
par=[]
impar=[]
soma_par=0
media_impar=0



for i in range (e):
    lista.append(int(input("Digite um número:  ")))

    if lista[i] % 2 ==0:
        par.append(lista[i])

    else: 
       impar.append(lista[i])
       
    

soma_par=(sum(par))
media_impar=(sum(impar)/len(impar))
    


print("Lista ", lista)
print("Números Pares ", par)
print("Soma Pares ",soma_par)
print("Números ímpares ", impar)
print("Média ímpares ", media_impar)


