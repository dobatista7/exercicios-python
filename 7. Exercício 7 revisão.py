#Exercício 7 - Faça um programa que rceba a idade e as alturas de 10 atletas
# Calcule e mostre na tela:
# A maior idade
#A menor idade
#A média das alturas
#A maior altura
i=0
idade=0
maior_altura=0.00
maior_idade=0
menor_idade=0
altura=0.00
media=0.00


while i <10:
      
    idade=int(input("Entre com a idade:  "))
    altura=float(input("Digite a altura:  "))
    
       
    if idade > maior_idade:
        maior_idade=idade
       
    if idade < maior_idade:
        menor_idade=idade
        
    if altura >maior_altura:
        maior_altura=altura
    i=i+1

    media=media+altura

media=media/i

print(" A maior idade é:  ", maior_idade)
print(" A menor idade é:  ", menor_idade)
print(" A média das alturas é:  ", media)
print(" A maior altura é:   ", maior_altura)
print(" Número de participantes na pesquisa:  ", i)

   
        



