#Exercício 41 

mat=[]
for i in range(5):
    lin=[]
    lin.append(input("Nome: "))
    lin.append(float(input("Nota 1: ")))
    lin.append(float(input("Nota 2: ")))
    lin.append(float(input("Nota 3: ")))
    mat.append(lin)
    
med=[0,0,0,0,0]
for i in range(5):
    med[i]=(mat[i][1]+mat[i][2]+mat[i][3])/3

# resultados
for i in range(5):
    print("Nome: "+mat[i][0]+ " média : "+str(med[i]))
