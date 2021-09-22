#Exercicio 19 - Gere uma lista contendo os múltiplos de 3 entre 1 e 50.

L=[]

for i in range (3,50,3):
    L =[i]+L
    
L.reverse()        
print(L)
