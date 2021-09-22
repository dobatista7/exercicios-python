#Exercício 5 - Faça um programa que verifique se um número é perfeito ou não.
#Um número é dito perfeito quando ele é igual a soma dos seus divisores
#excetuando ele próprio. (Ex: 6 é perfeito, 6=1+2+3, que são seus divisores).
#Exiba uma mensagem na tela informando se o número é ou não perfeito
soma=0
n=int(input("Digite um número:  "))
for d in range(1,n):
    if n%d==0:
        soma=soma+d
        
if n==soma:
    print("Esse número é perfeito")
    
else:
    print("Esse número é imperfeito")

            

        
  
    
