#Exercício 35 

i=1
n=i
u=40
p=[]

print("**Digite zero para sair**")
print("***Poltronas de 1 a 40***")

while n!=0 and i <=u:
    n=int(input("Escolha a poltrona:   "))
    if n==0:
        p.sort()

        print("As poltronas reservadas foram ", p, "!")
        print("O número de poltronas reservadas foi: ",len(p), "!")
        print("O número de poltronas vazias é: ",u-len(p), "!")

        if n < 0 and n > 42:

            print("Essa poltrona não existe")

            if n==41:

                print("As poltronas reservadas foram:  ", len(p), "!")


                if n==42:

                    print("As poltronas vazias foram: ",u-len(p), "!"
                          

     else:
        if n in p:
            print("A poltrona", n, "está indisponível!")
             
        else:
            p.append(n)
            print("a poltrona", n, "foi reservada com sucesso!")
            i+=1


            

