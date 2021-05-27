
matriz_numeros=[[12,72,45,97],
                [34,3,67,89],
                [12,52,8,25]]
print(matriz_numeros)

#Imprimir posicion fija
print(matriz_numeros[0][2])
print(matriz_numeros[1][1])

#Imprimir filas
print("Fila 0",matriz_numeros[0])
print("Fila 1",matriz_numeros[1])
print("Fila 2",matriz_numeros[2])

#Solicitar la posicion al usuario 

fil=int(input("Fila: "))
col=int(input("Columna: "))
print("La posicion es: ",matriz_numeros[fil][col])

#Imprimir columna
for f in range(3):
    print(matriz_numeros[f][1])

#Imprimir columna que pide el usuario 
col=int(input("Columna: "))
for f in range(3):
    print(matriz_numeros[f][col])    

#Sumar todos los elementos d la matriz
suma_m=0
for f in range(3):
    for c in range(4):
        suma_m=suma_m+matriz_numeros[f][c]
print("La suma es:",suma_m)        
        

#Suma cada fila
print("Sumar elementos de cada fila")
suma_m=0
for f in range(3):
    for c in range(4):
        suma_m=suma_m+matriz_numeros[f][c]
    print("La suma es:",suma_m) 
    suma_m=0