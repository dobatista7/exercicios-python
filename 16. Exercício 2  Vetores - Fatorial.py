#Exercício 16 - Calcule o Fatorial
#Vetores - 
n=10
lista=[]
resultado=[]


for i in range (n):
    lista.append(int(input("Digite um número:    ")))
    fatorial=1
    for z in range(1,lista[i]+1):
        fatorial=fatorial*z
    resultado.append(fatorial)

for y in range (n):
    print(lista[y],resultado[y])
