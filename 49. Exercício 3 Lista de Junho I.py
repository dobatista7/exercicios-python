#Exercício 49 - Lista II -  Exercício 3 Lista de Junho.
#Foi realizada uma pesquisa para determinar o índice de mortalidade infantil em um certo período.
#Faça um programa que: 
#a. Leia o número de crianças nascidas no período:
#b. Identifique o sexo (M ou F)
#c. Identifique o tempo de vida de cada criança em meses 
# O programa deve calcular:
#• A percentagem de crianças do sexo masculino mortas no período
#• A percentagem de crianças do sexo feminino mortas no período
#• A percentagem de crianças que viveram 24 meses ou menos no período

i=1
n=i
cont=0
nasc=0
fal=0
t=0
fem=0
masc=0
viv=0
percent_masc=0
percent_fem=0
percent_viv=0

print("Digite =0 para encerrar")
while n>0:
    n=int(input("Digite 1= Nascido ou 2=Falecido  "))
    if n==0:
        i=n
    gen=str(input("Digite F=Feminino ou M=Masculino  "))
    cont+=1
    if n == 1:
        nasc+=1
    if n == 2:
        fal+=1
        t=int(input("Informe o tempo de vida em meses: "))
        if gen =="F" or "f":
            fem+=1
            if gen =="M" or "m":
                masc+=1
                if t <= 24:
                    viv+=1

percent_masc=masc/cont*100
percent_fem=fem/cont*100
percent_viv=viv/cont*100

print("Número de crianças vivas no período pesquisado:   ", nasc)
print("Número de crianças falecidas no mesmo periódo:   ", fal)
print("A percentagem de crianças do sexo masculino mortas no período  ",percent_masc)
print("A percentagem de crianças do sexo feminino mortas no período    ",percent_fem)
print("A percentagem de crianças que viveram 24 meses ou menos no período   ",percent_viv)



