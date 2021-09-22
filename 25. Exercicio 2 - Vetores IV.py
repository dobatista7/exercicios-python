#Exercicio 25 Faça um programa que preencha uma lista com 10 nomes diferentes,
#e uma segunda lista com os telefones.
#Depois permita fazer uma pesquisa se um determinado nome existe
#armazenado na lista, se existir deve ser impresso na tela o nome e o telefone,
#a pesquisa deve ser feita até que seja digitado FIM no nome a ser pesquisado
#na lista.

p=2
n=[]
f=[]
v=0

for i in range(p):
    n.append(str(input("Nome:  ")))
    f.append(str(input("Fone:  ")))

while v != "fim":
    v=str(input("Digite um nome ou fim para encerrar o programa:  "))
    for i in range (p):
        if v in n[i]:
            print(n[i],f[i])
        else:
            print("Nome não existe. Retorne a pesquisa")
print("fim")
    

    

