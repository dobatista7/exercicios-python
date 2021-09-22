#Exercício 62 - Lista II - Exercício 5 - Faça um programa que preencha uma lista com os nomes de 5 produtos
#e outra lista com o valor dos produtos. Calcule e mostre:
#a) a quantidade de produtos que o valor é abaixo de 10 reais;
#b) a média dos valores dos produtos;
#c) a quantidade de produtos que valor acima da média;
#d) o maior valor e o nome do produto;
#e) faça uma listagem que imprima na tela (Nome   Vlr do produto)
#Mostres as três listas na tela.
e=5
n=[]
v=[]
media=0
m=[]

for i in range (e):
    n.append(str(input("Nome:  ")))
    v.append(float(input("Valor: ")))

media=(sum(v)/e)
qtd=0
valor=0
mv=0

for i in range(e): 
    if v[i] < 10.0:
        qtd+=1
    if v[i]>media:
        valor+=1
    if v[i]> mv:
        mv=v[i]
        nv=n[i]
    m.append(n[i])
    m.append(v[i])
    
    
print("a quantidade de produtos que o valor é abaixo de 10 reais:  ", qtd)
print("a média dos valores dos produtos:  ", media)
print("a quantidade de produtos que valor acima da média:  ", valor)
print("o maior valor", mv," e o nome do produto:  ",nv)
print("                                                                ")
print("faça uma listagem que imprima na tela (Nome   Vlr do produto", m)
print("              Ou                                               ")
for i in range (e):
    print("Produto",[i],n[i]," ", v[i])
print("                               ")
print("Mostres as três listas na tela:  ")
print("Produtos:  ", n)
print("Valores:    ",v)
print("Lista Prod e Valores", m)



