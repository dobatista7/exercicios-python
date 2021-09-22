#63. Aula de 16 de junho de 2020 - Exercício 1
#Faça um programa que solicita as notas das duas provas
#feitas por cada um dos 10 alunos de uma turma e
#imprime para cada um a média das notas.
#A média deve ser feita usando uma função que recebe as duas notas e
#retorna a média

def media(n1,n2):
    calc=((n1+n2)/2)
    return (calc)

print("Programa Calcule a média do aluno")

for i in range(1,6):
    p1=(float(input(f"Nota da P1 - aluno {i} ")))
    p2=(float(input(f"Nota da P2 - aluno {i} ")))
    nota=(media(p1,p2))
    print(f"A média do aluno é {i}",nota)





    


        
