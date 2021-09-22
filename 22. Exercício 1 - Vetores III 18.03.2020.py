#22 - 18.03 -  Faça um Programa que leia duas listas com 10 números cada.
#Gere uma terceira lista com 20 números;
#cujos valores deverão ser compostos pelos números intercalados das duas outras listas.

e=10
L1=[]
L2=[]
L3=[]

for i in range (e):
    L1.append(int(input("Digite número L1:  ")))
    L2.append(int(input("Digite número L2:  ")))
    
print("L1", L1)
print("L2", L2)

for j in range (e):
    L3.append(L1[j])
    L3.append(L2[j])

L3.sort()

print("L3", L3)


    
 
