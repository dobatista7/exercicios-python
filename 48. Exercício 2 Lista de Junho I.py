#Exercício 48 Lista II - 2) Faça um programa que receba dez números inteiros. Calcule e mostre:
#a) a soma dos números primos:
#b) a média dos números multiplos de 3 que são maiores que 10

e=10
soma=0
media=0


for i in range(e):
    n=int(input("Digite um número: "))
    cont_div=0
    for j in range(1,n+1):
        if n %j==0:
            cont_div+=1
    if cont_div==2:
        soma+=n

    if n % 3 ==0 and n > 10:
        media+=n

media=media/e

print("Soma dos primos:   ", soma)
print("A média dos números multiplos de 3 que são maiores que 10:    ",media)
