# Exercício 37 - Uma empresa de ônibus precisa de um sistema para facilitar a venda de passagens.
#O ônibus possui 40 lugares e o usuário pode escolher a poltrona informando um número de 1 a 40,
#se a poltrona estiver ocupada deverá ser exibido uma mensagem informando que a
#poltrona já está ocupada, caso contrário a poltrona deve ser reservada.
#O sistema deve ser encerrado quando for digitado zero no número da poltrona.
#No final deve ser exibido na tela: 
#a quantidade de poltronas ocupadas
#a quantidade de poltronas livres
#Obs: deve ser usado listas para resolver este problema

i=1
n=i
u=40
p=[]

print("******Sistema Cometa******")
print("**Digite zero para sair**")
print("***Poltronas de 1 a 40***")

while n!=0 and i <=u:
    n=int(input("Escolha a poltrona:  "))
    if n==0:
        p.sort()
        
        print("As poltronas reservadas foram ", p, "!")
        print("O número de poltronas reservadas foi: ",len(p), "!")
        print("O número de poltronas vazias é: ",u-len(p), "!")
    else:
        if n in p:
            print("A poltrona", n, "está indisponível!")
        else:
            p.append(n)
            print("A poltrona", n, "foi reservada com sucesso!")
            i+=1
   
        
                    

                 
