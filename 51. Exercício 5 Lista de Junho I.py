#Exercício 51- Lista I - 5) Faça um programa que receba dez números inteiros. Calcule e mostre:
#• A quantidade de números primos:
#• A soma dos números ímpares:
#• A média dos pares.

cont_prim=0
cont_par=0
par=0
impar=0

for i in range(10):
    n=int(input("Digite um número:  "))
    cont_div=0
    for j in range(1,n+1):
            if n %j==0:
                cont_div+=1         
    if cont_div==2:
        cont_prim+=1
    
    if n % 2 ==0:
        cont_par+=1
        par+=n

    if n % 2 != 0:
        impar+=n

media=par/cont_par

print("A quantidade de números primos: ", cont_prim)
print("A soma dos números ímpares:    ", impar)
print("A média dos pares  ", media)
 
