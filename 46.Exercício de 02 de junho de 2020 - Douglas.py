
#Exercicio 46 -  de 02 de junho de 2020 (Douglas Oliveira Batista

e=5
matriz=[]

for i in range (e):
    linha=[]
    linha.append(str(input("Nome:  ")))
    linha.append(float(input("Salário:  ")))
    linha.append(int(input("Idade: ")))
    linha.append(int(input("Filhos: ")))
    matriz.append(linha)    

for i in range(e):
    print(matriz[i])

print()

soma=0
qtd=0
res=matriz[0][1]
pos=i

for i in range (e):              
        soma+= matriz[i][1]
        if matriz[i][2] > 25 and matriz [i][2] <=40: 
            qtd+=1
        if matriz[i][1] > res:
              res=(matriz[i][1])
              pos=i
                
media=soma/e
print("Média de Salários:   ", media)
print("Quantidade de alunos:  ", qtd)
print("Maior salário"+str(res), "salário do: " + matriz[pos][0])

              

                         
                         
