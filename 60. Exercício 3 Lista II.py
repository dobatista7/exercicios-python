#Exercício 60 - Lista II - Exercício 3 - Faça um programa que preencha duas listas, Lista A
#e Lista B. Depois calcule e mostre na tela a quantidade de números pefeitos.
#Um número é perfeito quando ele é igual a soma dos seus divisores excetuando
#ele próprio. (Ex: 6 é perfeito, 6=1+2+3, qu são seus divisores).

e=3
A=[]
B=[]
cont=0
soma=0
perf=[]

for i in range(e):
    n=int(input("A:  "))
    A.append(n)
    n=int(input("B:  "))
    B.append(n)
C=A+B
for i in range(len(C)):
    for j in range (1,C[i]):
        if C[i]%j==0:
            soma+=j
    if soma == C[i]:
        cont+=1
        perf.append(C[i])
    soma=0
    
print("Conjunto A:  ",A)
print("Conjunto B:  ",B)
print("Quantidades de Nº Perfeitos: ",cont)
print("Números Perfeitos: ", perf)
    
             
