#Exercício 36 - Vetores-
#Elaborar um programa  que leia 10 números e armazene-os numa lista A.
A=[]
B=[]

for i in range (10):
    A.append(int(input("Digite um número:  ")))
    B.append(A[i]/2)
A.sort()
A.reverse()
B.sort()
print("A",A)
print("B",B)
