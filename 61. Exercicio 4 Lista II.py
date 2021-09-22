# Exercício 61 - Lista II - Exercício 4 - Faça um programa que preencha duas listas
#com 10 elementos em cada. Depois percorra essas duas listas e gere
#uma terceira lista com os números que se repetem nas duas listas.
#Mostres as três listas na tela.

from random import randint
e=10
A=[]
B=[]
C=[]

for i in range(e):
    A.append(randint(1,20))
    B.append(randint(1,20))
    if A[i] in B :
        C.append(A[i])
        
A.sort()
B.sort()
C.sort()
print("Lista A", A)
print("Lista B", B)
print("Lista C", C)

             
