# 57. Exercício da aula de 10 de  junho de 2020
# Crie uma função que receba um número inteiro como parâmetro
# Verifique se ele é primo ou não e
# exibindo uma mensagem dentro da função.

def check (num):
    soma=0
    for i in range(1,num+1):
        if num%i==0:
            soma+=1
    if soma==2:
        print(f"O número {num} é primo")
    else:
        print(f"O número {num} não é primo")

n=int(input("Digite um número e verifique se ele é primo:  "))
check(n)
        
    
