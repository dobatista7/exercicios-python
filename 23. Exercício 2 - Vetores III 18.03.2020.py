#23. Faça um programa que simule um lançamento de dados.
#Lance o dado 20 vezes e armazene os resultados em uma lista.
#Depois, mostre quantas vezes cada valor foi conseguido.
#Dica: use um vetor de contadores(1-6) e a função (randint)
#para gerar números aleatórios, simulando os lançamentos dos dados.

from random import randint
e=20
L=[]
n=0
cont1=0
cont2=0
cont3=0
cont4=0
cont5=0
cont6=0

for i in range (e):
    n=randint(1,6)
    if n == 1:
        cont1+=1
    if 2 == n:
        cont2+=1
    if 3 == n:
        cont3+=1
    if 4 == n:
        cont4+=1
    if 5 == n:
        cont5+=1
    if 6==n:
        cont6+=1
    L.append(n)
    
print("Resultados dos dados ", L)
print("Por", cont1, "vezes apareceu o número 1!")
print("Por", cont2, "vezes apareceu o número 2!")
print("Por", cont3, "vezes apareceu o número 3!")
print("Por", cont4, "vezes apareceu o número 4!")
print("Por", cont5, "vezes apareceu o número 5!")
print("Por", cont6, "vezes apareceu o número 6!")
print("Total de", len(L),"lançamentos")

