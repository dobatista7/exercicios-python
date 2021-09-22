# Exercício 28

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
   
        
                    

                 
