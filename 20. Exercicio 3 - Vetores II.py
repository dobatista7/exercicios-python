#20. Faça um programa  que receba a idade de 10 pessoas e armazene numa lista.
##calcule e mostre:
###A quantidade de pessoas com idade superior  a  50 anos
####A média das idades
#####A quantidade de pessoas com idade menor que a média das pessoas que responderam essa pesquisa.

p=10
idades=[]
media=0
cinq=0
menor=0

for i in range (p):
    idades.append(int(input("Digite a sua idade:  ")))
    media=media+idades[i]

    if idades[i] > 50:
        cinq=cinq+1
       
media=media/p

for i in range (p):
    if idades[i] < media:
        menor=menor+1
           
print("As idades digitadas foram:   ", idades)

print("A quantidade de pessoas maiores que 50 anos:  ", cinq)

print("A média das idades foram:  ", media)

print ("O número de pessoas com idade menor que a média:  ", menor)



