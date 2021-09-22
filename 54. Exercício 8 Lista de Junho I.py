# Exercício 54 - Lista I Exercício 8 - Lista de Junho
#Faça um programa que receba um número:
#calcule e mostre a tabuada desse número na tela.

n=int(input("Digite um número:   "))
for i in range (11):
    tab=n*i
    print("A tabuada do número", n, "X", i,"=", tab)
   
    
