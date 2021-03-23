'''
Desarrollar un programa con dos funciones.
La primer solicite el ingreso de un entero y muestre el cuadrado de dicho valor.
La segunda que solicite la carga de dos valores y muestre el producto de los mismos.
LLamar desde el bloque del programa principal a ambas funciones.
'''

def val_entero():
    import math
    cua=0
    num=int(input("Digite un numero: "))
    cua=pow(num,2)
    print("El cuadrado es:", cua)

def val_producto():
    prod=0
    num1=int(input("Digite un numero: "))
    num2=int(input("Digite un numero: "))
    prod=num1*num2
    print("El producto es:", prod)

val_entero()
val_producto()    