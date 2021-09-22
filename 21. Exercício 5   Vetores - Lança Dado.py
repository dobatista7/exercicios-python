#Exercício 21 Faça um programa que simule um lançamento de dados.
#Lance o dado 10 vezes e armazene em uma lista.
#Depois mostre quantas vezes cada valor foi conseguindo.

from random import randint
L=[0]*7
n=0

for i in range (10):
    n=randint(1, 6)
    print("Número:  ", n)
    lista[n]=lista[n]+1

for i in range (1,7):
    print("Número: ", i,"qtde:   ", lista[i]) 



    
