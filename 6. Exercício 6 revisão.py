#Exercício 6 Faça um programa que receba a idade e os respectivos pesos
#de um número indeterminado de pessoas. Para finalizar a entrada deve ser
#digitado idade zero ou negativa. Calcule e mostre na tela:
#a maior idade
#A quantidade de pessoas que pesam mais que 90 quilos
#a média de idade das pessoas que pesam menos que 50 quilos

idade=0
maior_idade=0
peso=0
soma=0
media=0
soma2=0

print("Para encerrar entre com valor negativo no campo idade E zero no campo peso")
while idade >=0:
    
    idade=int(input("Entre com a idade:  "))
    peso=float(input("Digite o peso:  "))
    
    if idade > maior_idade:
        maior_idade=idade
       
    if peso > 90:
        soma=soma+1
        
    if idade >=0 and peso < 50:
        soma2=soma2+1
        media=media+idade
        
        
media=media/soma2
print(" A maior idade é:  ", maior_idade)
print("O número de pessoas com mais de 90 kilos é:  ", soma)
print("A média de idade das pessoas que pesam menos de cinquenta kilos é:   ", media)
