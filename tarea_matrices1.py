import random


fil=int(input("Ingrese numero de filas: "))
col=int(input("Ingrese numero de columnas: "))

matriz=[[random.randint(1,100) for i in range(fil)] for j in range(col)]


for f in range(fil):
        for x in range(col):
                print(matriz[f][x],end=' ')
        print()               

fila1=matriz[0]
print(fila1)
     
