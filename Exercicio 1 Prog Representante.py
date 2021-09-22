'''Programa Representante'''
nome_candidato1=str(input("Digite o nome do candidato 1  "))
nome_candidato2=str(input("Digite o nome do candidato 2  "))
candidato1=int(input("Digite os votos do candidato 1  "))
candidato2=int(input("Digite os votos do candidato 2  "))
if candidato1>candidato2:
    voto=candidato1
    print(nome_candidato1, "- Candidato 1- ganhou", voto,"votos")
else:
    voto=candidato2
    print(nome_candidato2,"- Candidato 2 - ganhou", voto, "votos")
