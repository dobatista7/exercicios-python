i=1
while i <= 3:
   cod=int(input("Digite o código do produto "))
   descr=str(input("Informe a descrição do produto "))
   valor=float(input("Digite o preço do produto "))
   quant=int(input("Digite a quantidade do produto "))
   t=valor*quant
   if t > 100:
    desc=t*0.1
   else:
    desc=t*0.05
    descf=t-desc
   print("Desconto ", desc)
   print("Valor da compra com desconto ", descf)
   i=i+1


    




           
