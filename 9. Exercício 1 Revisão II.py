#Revisão parte II
#Exercício 9 Escreva um programa que leia um conjuno de 10 números inteiros.
#Calcule e mostre:
    # o menor número
    # a soma dos números pares e maiores que 10
    # a quantidade de números ímpares
    # a média dos números maiores que 100

i=0
menor_n=0
soma_pares=0
soma_impares=0
media=0
soma_cem=0
while i<10:
    n=int(input("Digite um número:  "))
    i=i+1
          
    if menor_n == 0:
        menor_n=n

    if menor_n > n:
        menor_n=n
    
    if n%2 ==0 and n >10:
        soma_pares=soma_pares+n
        
    if n%2 != 0:
        soma_impares=soma_impares+1
        
    if n>100:
        soma_cem=soma_cem+1
        media=media+n

if soma_cem>0:     
    media=media/soma_cem

print("O menor número:  ", menor_n)
print("A soma dos números pares e maiores que 10:  ", soma_pares)
print("A quantidade de números ímpares:  ", soma_impares)
print("A média dos números maiores que 100:  ", media)
