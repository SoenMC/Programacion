##Desarrollar un programa que permita cargar n números enteros y luego
#nos informe cuántos valores fueron pares y cuántos impares.
#Emplear el operador “%” en la condición de la estructura condicional
#(este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):

x=1
pares=0
impares=0
n=int(input("Cantidad de numeros a ingresar ->: "))
while x<=n:
    valor=int(input("Ingrese los valores ->: "))
    if valor%2==0:
        pares=pares+1
    else:
        impares=impares+1
    x=x+1
print(f"La cantidad de numeros pares es: {pares}")        
print(f"La cantidad de numeros impares es: {impares}")