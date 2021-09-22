#Exercício 24 -  A prefeitura de uma cidade fez uma pesquisa entre 20 habitantes,
#coletando dados sobre o salário e o número de filhos,
#armazene os salários e número de filhos em listas.
#Faça um programa que calcule e mostre:
##média de salário da população;
###média do número de filhos;
###maior salário;
####percentual de pessoas com salário inferior a R$ 1000,00.

p=10
s=[]
f=[]
media_s=0
media_f=0
perc=[]
base=(float(1000))

for i in range (p):
    s.append(float(input("Salário:  ")))
    f.append(int(input("Filho (s):  ")))
    media_s=(sum(s)/p)
    media_f=(sum(f)/p)
    if s[i]< base:
        perc.append(s[i])
   

print("Média salarial:  ", media_s)
print("Média do número de filhos:  ", media_f)
print("Maior salário:  ",max(s))
print("Percentual de pessoas com salário inferior a R$1.000,00:  ",len(perc)/len(s)*100,"%")

    
    
    
    
