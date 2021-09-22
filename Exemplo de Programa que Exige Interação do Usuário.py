resp="s"
soma=0
while resp =="s":
    n=int(input("Digite um número "))
    if n>=10:
        print("Você venceu")
        soma=soma+n
        print("Soma: ", soma)
    else:
        print("Você perdeu")
    resp=str(input("Deseja Continuar? S/N "))
print("Fim do programa")
