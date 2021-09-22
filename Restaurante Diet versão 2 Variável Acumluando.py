#criar um algoritimo que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deveria informar o prato, a sobremesa e a bebida
print("Restaurante Só Diet")
print("Opções de Pratos quentes: 1-Vegetariano , 2-Peixe ,3-Frango , 4-Carne")
calorias=0
prato=int(input("Digite o número do Prato Quente Desejado:  "))
if prato == 1:
    calorias=180+calorias
elif prato == 2:
    calorias=230+calorias
elif prato==3:
    calorias=250+calorias
elif prato==4:
    calorias=350+calorias
else:
    print("Menu inexistente ")
print("Opções de Sobremesa: 5-Abacaxi , 6-Sorvete, 7 - Mousse, 8-Torta")
sobremesa=int(input("Digite o número da Sobremesa Desejada:  "))
if sobremesa==5:
    calorias=75+calorias
elif sobremesa==6:
    calorias=110+calorias
elif sobremesa==7:
    calorias=170+calorias
elif sobremesa==8:
     calorias=200+calorias
else:
     print("Menu inexistente ")
print("Opções de Bebida: 9- Chá, 10- Suco de Laranja , 11-Suco de Melão, 12-Refrigerante")
bebida=int(input("Digite o número da Bebida Desejada:  "))
if bebida==9:
    calorias=200+calorias
elif bebida==10:
    calorias=70+calorias
elif bebida==11:
    calorias=100+calorias
elif bebida==12:
    calorias=65+calorias
else:
    print("Menu inexistente ")
print("A refeição escolhida tem: ", calorias, "calorias")
