#Exercício 1 - Faça um programa que receba a idade e
# conforme a faixa etária  exiba a mensagem se é
#criança, adolescente, adulto ou idoso

idade=int(input("Digite a sua idade: "))
if idade >=0 and idade <=12:
    print ("Sou uma criança")
elif idade >= 13 and idade <=17:
     print ("Sou um adolescente")
elif idade >= 18 and idade <=59:
     print ("Sou um adulto")
elif idade >= 60:
    print ("Sou um idoso")
else:
    print("Sou imortal")       

