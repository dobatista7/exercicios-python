#Revisão II
#Exercício 11 - Faça um programa que receba dez números inteiros.
#Calcule e mostre:
# A soma dos números primos

soma=0

for i in range (10):
    num=int(input("Entre com número:  "))
    cont_div=0
    for j in range (1, num+1):
            if num %j==0:
                cont_div+=1
    if cont_div==2:
            soma=soma+num
            
print("Soma  dos primos:  ", soma)
    
    
