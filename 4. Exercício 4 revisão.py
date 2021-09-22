#Exercício 4 - Escreva um programa que leia 10 notas e
#informe  a média dos alunos 
n=0
i=0
media=0
while i <10:
    n=float(input("Entre com as dez notas do aluno: "))
    i=i+1
    media=media+n
media=media/10
print ("A média das dez notas digitadas é: ", media)
    
