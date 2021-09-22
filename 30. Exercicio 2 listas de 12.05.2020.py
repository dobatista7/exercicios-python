# Exercício 30 - Faça uma programa que leia 2 listas de números inteiros,
#tendo cada um 10 e 20 elementos (pode ser usado a função randint) e
#apresente na tela os elementos que não são comuns nas duas listas.

from random import randint
L1=[]
L2=[]
L3=[]


for i in range (10):
    L1.append(randint(0,30))

for i in range (20):
   L2.append(randint(0,30))
   
   if ((L2[i] not in L1) and (L2[i] not in L3)):
       L3.append(L2[i])
       
for i in range (10):
    if ((L1[i] not in L2) and (L2[i] not in L3)):
       L3.append(L1[i])

 
   
print(L1)
print(L2)
print(L3)
       
    
   




