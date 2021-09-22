# Exercício 55 - 08.06.2020 -  Faça um programa que preencha duas lista,
#uma com os nomes e a outra com sobrenomes. Gera uma terceira lista que é
#a junção do nome e sobrenome, usando o méodo upper() para transformar em
#maiúsculo o nome e sobrenome. Imprima a terceira lista

e=2
a=[]
b=[]
c=[]

for i in range(e):
    a.append(str(input("Nome:   ")))
    b.append(str(input("Sobrenome:  ")))

for i in range(e):
    c.append (a[i].upper()+ "  "+b[i].upper())

print(c)
    
