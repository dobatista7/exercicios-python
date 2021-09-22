# 65a. Exercício 2 - da aula de 17 de junho de 2020
# A prefeitura de uma cidade fez uma pesquisa entre 10 habitantes
#coletando dados sobre o SALÁRIO e NÚMERO de filhos.
#Calcule:

e=10
def sal(lista):
    media=sum(lista)/e
    return(media)

def fil (lista):
    media=sum(lista)/e
    return(media)

salario=[]
filhos=[]
for i in range(e):
    salario.append(float(input("Salário:  ")))
    filhos.append(int(input("Filhos:   ")))

m=sal(salario)
n=fil(filhos)

print("Média do salario:  ", m)
print("Média de filhos:   ",n)

