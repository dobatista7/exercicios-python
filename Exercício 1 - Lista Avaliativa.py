#Exercício 1 da 2ª Lista Avaliativa
cont_casada=0
cont_solteira=0
cont_viuva=0
media_viuva=0
cont_divorciados=0
porcentagem_divorciados=0
cont=0
idade=int(input("Digite a sua idade ou para encerrar o programa digite zero:  "))
while idade>0:    
    civil=int(input("Digite o seu estado civil: 1.Casado,2.Solteiro,3.Viúvo ou 4.Divorciado "))
    if civil ==1:
         civil="Casado"
         cont_casada=cont_casada+1
    elif civil ==2:
         civil="Solteiro"
         cont_solteira=cont_solteira+1
    elif civil==3:
         civil="Viúvo"
         cont_viuva=cont_viuva+1
    elif civil ==4:
         civil="Divorciado"
         cont_divorciados=cont_divorciados+1
    else:
        print("Código inválido")
    cont=cont+1        
    idade=int(input("Digite a sua idade:  "))
media_viuva=(media_viuva+idade)/cont_viuva
porcentagem_divorciados=(cont_divorciados/cont)*100
print("Exiba o número de pessoas casadas:  ", cont_casada)
print("Exiba o número de pessoas solteiras: ",cont_solteira)
print("Exiba a média das idades das pessoas viúvas:  ", media_viuva)
print("Exiba a porcentagem de divorciados:  ", porcentagem_divorciados, "%")


          
          

