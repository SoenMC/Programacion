'''
Desarrollar un programa que solicite la carga de tres valores y muestre el menor.
Desde el bloque principal del programa llamar 2 veces a dicha función 
(sin utilizar una estructura repetitiva)
'''


def carga_valores():
    num1=int(input("Valor -> "))
    num2=int(input("Valor -> "))
    num3=int(input("Valor -> "))

    if num1<num2 and num1<num3:
        print("El menor es: ", num1)    
    else:
        if num2<num3:
            print("El menor es: ", num2)
        else:
            print("El menor es: ", num3) 

carga_valores()
carga_valores()
            