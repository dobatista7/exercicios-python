#Criar o cadastero de uma pessoa recebendo o nome , a cidade e a sigla do estado.
nome=str(input("Digite o nome: "))
cidade=str(input("Digite a cidade de origem:  "))
sigla=str(input("Escolha  a sigla de um dos Estados: RJ - Rio de Janeiro SP - São Paulo MG - Minas Gerais : "))
if sigla == "RJ":
    print("Você é Carioca")
elif sigla == "SP":
    print("Você é Paulista")
elif sigla == "MG":
    print("Você é Mineiro")
else:
    print("Outros Estados")
