#Exercício 15 - Vetores 
# Faça um programa para calcular o IMC de 5 pessoas.

nome=[]
peso=[]
altura=[]
imc=[]

for i in range (5):
    nome.append(str(input("Digite o seu nome:  ")))
    peso.append(float(input("Digite o seu peso:   ")))
    altura.append(float(input("Digite  a sua altura:  ")))

    imc.append(float(peso[i]/(altura[i]*altura[i])))

for z in range (5):

    print(nome[z],imc[z])

    
