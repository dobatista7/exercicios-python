#Exercício 47 - Lista I 1) Escreva um programa que leia um conjunto de 10 números inteiros. Calcule e mostre:
#a) o menor número:
#b) a soma dos números pares e maiores que 10
#c) a quantidade de números ímpares:
#d) a média dos números maiores que 20

e=10
menor=0
soma=0
qtd=0
media=0
for i in range(e):
    n=(int(input("Digite um número: ")))
    if menor == 0:
        menor=n

    if menor > n:
        menor=n
        
    if n %2==0 and n >10:
        soma+=n
        
    if n%2 !=0:
        qtd+=1
    media=(media+n)
media= media/e


print("O menor número digitado:    ",menor)
print("A soma dos números pares e maiores que 10 ", soma)
print("A quantidade de números ímpares:  ", qtd)
print("A média dos números maiores que 20  ", media)
