#26 - Faça um programa que preencha uma lista com os nomes de 10 alunos,
#e outra lista com a idade dos alunos.
#Calcule e mostre:
##    1)a quantidade de alunos que tem idade superior a 15;
###   2)a média das idades dos alunos;
####  3)a quantidade de alunos que tem idade abaixo da média;
##### 4)a maior idade e o nome do aluno;
######5)a menor idade e o nome do aluno.

p=10
n=[]
ida=[]
q=0
s=0
mx=0
mn=0

for i in range (p):
    n.append(str(input("Nome do aluno:  ")))
    ida.append(int(input("Idade do aluno:  ")))

    if ida[i]>15:
        q+=1
        
m=(sum(ida)/p)

for i in range(p):
    if ida[i]<m:
        s+=1
    if ida[i]==max(ida):
        mx=n[i]
    if ida[i]==min(ida):
        mn=n[i]
        
print("A quantidade de alunos que tem idade superior a 15:  ",q)
print("A média das idades dos alunos:   ",m)
print("A quantidade de alunos que tem idade abaixo da média:  ", s)
print("A maior idade é ", max(ida), "o nome do aluno é:  ",mx)
print("A menor idade é ", min(ida), "o nome do aluno é:  ",mn)


