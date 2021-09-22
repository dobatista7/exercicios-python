for i in range (8):
    nome=str(input("Digite o nome do funcionário: "))
    salario=float(input("Digite o salário da pessoa:  "))
    if salario>600 and salario<1500:
         imposto= salario*0.1
    else:
        if salario>=1500:
             imposto=salario*0.15
        else:
             print("Salário insento de imposto")
    print("O nome do funcionário é: ", nome)
    print("A aliquota do imposto de renda é:  ",imposto)
     
