#Revisão 2
# Exercício 14 - Faça um programa que leia uma quantidade indeterminada de números
#positivos e conte quanto deles esão nos seguintes intervalos: [0-25], [26-50]
#[51-75], [76-99] e maiores que [100].
#A entrada de dados deverá ser encerrada quando for digitado um número negativo.

cont=0
contb=0
contc=0
contd=0
contf=0

n=0
print("*** Para encerrar digite um número negativo ******")
while n >=0:
    n=int(input("Digite um número:   "))

    if n >=0 and n<=25:
        cont+=1

    if n >=26 and n<=50:
        contb+=1

    if n >=51 and n<=75:
        contc+=1

    if n >=76 and n<=99:
        contd+=1

    if n >=100:
        contf+=1

print ("Intervalo de [0-25]:  ", cont) 
print ("Intervalo de  [26-50]:  ", contb) 
print ("Intervalo de [51-75]:  ", contc) 
print ("Intervalo de [76-99]:  ", contd) 
print ("Intervalo de maiores que [100]:  ", contf) 


