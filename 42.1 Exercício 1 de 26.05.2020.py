# 42.1 (Exercício: 26/05) 1) Faça um programa que preencha uma matriz 5X4:
#A primeira coluna dessa matriz deve armazenar os nomes dos alunos;
# As colunas restantes devem armazenar as notas de cada aluno:
## Calcule a média de cada aluno e armazene em uma lista.
### Depois imprima um relatório com o nome do aluno e a média.

matriz=[]
for i in range (5):
    linha=[]
    linha.append(input("Nome do aluno: "))
    linha.append(float(input("Nota 1:   ")))
    linha.append(float(input("Nota 2:   ")))
    linha.append(float(input("Nota 3:   ")))
    matriz.append(linha)

media=[0,0,0,0,0]

for i in range(5):
    media[i]=(matriz[i][1]+matriz[i][2]+matriz[i][3])/3
   
for i in range (5): 
        print("Nome: "+matriz[i][0]+ "media: " + str(media[i]))
