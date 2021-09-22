#Revisão II
# Exercício 10 - Faça um algoritmo que receba um número e verifique se esse número
# é divisivel por 3 e 5. Exibindo a mensagem na tela se o número é ou
# não divisível por 3 e 5

n=int(input("Entre com um número:  "))

if n !=0:
    if n % 3 ==0 and n % 5 ==0:
        print("Esse número é divisivel por 3 e 5")
    
    else:
       print("Esse número não é divisivel por 3 e 5")
else:
    print("Esse número é nulo")
      
