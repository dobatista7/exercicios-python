municipio=str(input("Informe o nome do município "))
eleitores=int(input("Digite o número de eleitores aptos "))
candidato_1=int(input("Digite o número de votos recebidos pelo candidato 1 "))
candidato_2=int(input("Digite o número de votos recebidos pelo candidato 2 "))
if candidato_1>candidato_2:
    print("Candidato 1  recebeu",candidato_1, "votos!")
    if (eleitores>20000 and candidato_1 or candidato_2) < eleitores/2:
     print("Haverá segundo turno") 
else:
    print("Candidato 2 recebeu",candidato_2, "votos!")
