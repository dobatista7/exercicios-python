#Exercício 50 - Lista I - Exercício 4 - lista de junho -
#Cada espectador de um cinema respondeu a um questionário no qual constava sua idade
#e sua opinião em relação ao filme (3- ótimo;2- bom;1-regular).
#Faça um programa que receba a idade e a opinião de um número indeterminado de pessoas.
#Para finalizar a entrada deve ser digitado uma idade negativa ou zero.
#Calcule e mostre:
#• A média das idades das pessoas que responderam ótimo;
#• A quantidade de pessoas que responderam regular;
#• A quantidade de pessoas que responderam bom.

idade=0
cont=0
soma=0
n=0
reg=0
bom=0
oti=0


print("O programa encerra com valor negativo no campo idade e Zero no campo Avalie o Filme")
while idade >=0:
    idade=int(input("Digite a sua idade:   "))
    cont+=1
    n=int(input("Avalie o filme. Digite 1-Regular; 2-Bom ou 3-Ótimo:  "))
    if n == 1:
        reg+=1
    elif n==2:
        bom+=1
    elif n==3:
        oti+=1
        soma+=idade
media=soma/oti
                
print("A média das idades das pessoas que responderam ótimo:   ", media)
print("A quantidade de pessoas que responderam regular:         ",reg)
print("A quantidade de pessoas que responderam bom:         ",bom)

