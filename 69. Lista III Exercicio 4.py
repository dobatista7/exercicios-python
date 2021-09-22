#69. Lista III - Exercício 4 - Escreva um programa que armazene em uma matriz 
#o nome e duas notas de 5 alunos. Calcule e armazene em uma lista a média de cada aluno
#e em outra lista o status(media>=6,"aprovado", caso contrário, "reprovado")
#faça uma opção para que o usuário possa fazer uma pesquisa por nome.
# Se encontrar exiba na tela: 
#a) posição em que foi encontrado (indice);
#b) nome do aluno:
#c) as duas notas e a média:
#d) status:

e=5
matriz=[]
media=[]
status=[]

print("Exercício 4 Lista III - Matrizes")
print("")
for i in range (e):
    linha=[]
    linha.append(str(input("Nome do Aluno:  ")))
    linha.append(float(input("Nota 1:   ")))
    linha.append(float(input("Nota 2:   ")))
    matriz.append(linha)

print("")
print("Aluno Nota1 Nota2")
for i in range(e):
    print(matriz[i])

print("")
print("")

for i in range(e):
    m=((matriz[i][1]+matriz[i][2])/2)
    media.append(m)
    if m >=6:
        status.append("Aprovado")
    else:
        status.append("Reprovado")

pesquisa=(str(input("Pesquise o nome do aluno:  ")))
for i in range(e):
    if pesquisa==matriz[i][0]:
        print(f" Posição na lista: {i}")#a) posição em que foi encontrado (indice)
        print(" Nome do Aluno", matriz[i][0])#b) nome do aluno
        print(" Nota 1:", matriz[i][1], "Nota 2:", matriz[i][2])#c)as duas notas
        print(" Média Final do aluno: ",media[i])#c) a média:
        print(" Status: ", status[i])#d) status
            
        
            
        
        
    

