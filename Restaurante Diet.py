#criar um algoritimo que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deveria informar o prato, a sobremesa e a bebida
print("Restaurante Só Diet")
print("Opções de Pratos quentes: 1-Vegetariano , 2-Peixe ,3-Frango , 4-Carne")
print("Opções de Sobremesa: 5-Abacaxi , 6-Sorvete, 7 - Mousse, 8-Torta")
print("Opções de Bebida: 9- Chá, 10- Suco de Laranja , 11-Suco de Melão, 12-Refrigerante")
prato=int(input("Digite o número do Prato Quente Desejado:  "))
sobremesa=int(input("Digite o número da Sobremesa Desejada:  "))
bebida=int(input("Digite o número da Bebida Desejada:  "))
if prato == 1:
    pcal=180
elif prato == 2:
    pcal=230
elif prato==3:
    pcal=250
elif prato==4:
    pcal=350
else:
    print("Menu inexistente ")
if sobremesa==5:
    scal=75
elif sobremesa==6:
    scal=110
elif sobremesa==7:
    scal=170
elif sobremesa==8:
     scal=200
else:
     print("Menu inexistente ")
if bebida==9:
    bcal=200
elif bebida==10:
    bcal=70
elif bebida==11:
    bcal=100
elif bebida==12:
    bcal=65
else:
    print("Menu inexistente ")
cal=pcal+scal+bcal
print("O prato escolhido tem: ", cal, "calorias")
    
    
