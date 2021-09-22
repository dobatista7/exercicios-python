#Exercício 27 - Faça um programa que receba a temperatura média de cada mês do ano
#armazene-as em uma lista. Após isto, calcule a média anual das temperaturas
#mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (
##mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

p=12
tm=[]
mes=[]
media=0
meses=[]



for i in range (p):
    mes.append(str(input("Mês do ano:    ")))
    tm.append(float(input("Temperatura média do mês:   ")))

media=sum(tm)/p
print("A média da temperatura anual foi de     ", media)
print("Meses com temperatura maior que a média")
for i in range (p):
    if tm[i]>media:
        print(tm[i],mes[i])


        

      
        

    
