# Exercício 59 - Lista II - Exercício 2 - Faça um programa que preencha uma lista com 10 cores diferentes.
#Depois permita fazer uma pesquisa se uma determinada cor existe armazenada na lista
#se existir deve ser impresso na tela a cor e em qual posição (índice) esta cor está armazenada.
#A pesquisa deve ser feita até que seja digitado FIM na cor a ser pesquisada na lista

e=10
L=[]
p=str

for i in range (e):
    L.append(str(input("Digite a cor:  ")))
       
print("A lista de cores:  ", L)
    
while (p != "FIM"):
    p=str(input("Pesquise a cor ou digite FIM  para encerrar: "))
    for i in range(i+1):
        if p in L[i]:
            print("A cor ", p, "consta na lista e a sua posição é ", [i])

print("Programa encerrado")
    
    
        


