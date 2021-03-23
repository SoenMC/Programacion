#Desarrollar un programa que permita la carga de 10 valores por teclado
#y nos muestre posteriormente la suma de los valores ingresados y su promedio.
#Este problemaya lo desarrollamos,
#lo resolveremos empleando la estructura for para repetir la carga de los diez valores por teclado.


suma=0
for x in range(0,10):
    valor=int(input("Ingrese los valores ->: "))
    suma=suma+valor
print(f"La suma es {suma}")
promedio=suma/10
print(f"El promedio es {promedio}")    