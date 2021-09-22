#Exercício 58 - Lista II - Exercício 1 - Escreva um programa que leia a idade de 10 pessoas e armazene-as em uma lista.
#Calcule e mostre:
#a) a menor idade:
#b) a média das idades:
#c) a quantidade de pessoas que tem idade entre 20 e 30 anos (inclusive)
#d) a quantidade de pessoas com idade maior que a média

e=10
L=[]
menor=0
qtd_a=0
qtd_b=0


for i in range (e):
    L.append(int(input("Idade:   ")))
media=(sum(L)/e)

for i in range (e):
    if menor==0:
        menor=L[i]
    if L[i] < menor:
        menor=L[i]
    if L[i] >= 20 and L[i] <=30:
        qtd_a+=1
    if L[i] > media:
        qtd_b+=1

print(L)
print("a menor idade:  ", menor)
print("a média das idades",  media)
print("a quantidade de pessoas que tem idade entre 20 e 30 anos (inclusive)  ", qtd_a)
print("a quantidade de pessoas com idade maior que a média  ", qtd_b)
