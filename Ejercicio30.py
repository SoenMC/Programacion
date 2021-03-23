##Realizar un programa que permita cargar dos listas de 15 valores cada una. 
#Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor
#(mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
#Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

suma_1=0
suma_2=0
x=1
while x<=15:
    val_1=int(input("Ingrese valores para la lista 1: "))
    suma_1=suma_1+val_1
    x=x+1    
x=1
while x<=15:
    val_2=int(input("Ingrese valores para la lista 2: "))
    suma_2=suma_2+val_2
    x=x+1
if suma_1 > suma_2:
    print("Lista 1 es mayor")
else:
    if suma_2 > suma_1:
        print("Lista 2 es mayor")
    else:
        print("Las dos listas son iguales")
        










