# Exerício 53 - Lista I - Exercício 7 - Lista de Junho
#Faça um programa que receba várias idades,
#calcule e mostre a média das idades digitadas.
#Finalize digitando idade igual 0.

i=1
idade=i
cont=0
media=0
soma=0

while i > 0:
    idade=int(input("Digite a sua idade:   "))

    if idade ==0:
        i=idade
    
    if idade !=0:
        cont+=1
        soma+=idade   
       
    
media=soma/cont

print("A média das idades digitadas:  ",media)
