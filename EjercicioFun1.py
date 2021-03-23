'''
Confeccionar una aplicación que muestre una presentación en pantalla del programa. Solicite
la carga de dos valores y nos muestre la suma. Mostrar finalmente un mensaje de despedida del programa.
'''


def presentación():
    print("******************************************")
    print("Bienvenido a la aplicación")
    print("******************************************")

def carga_valores():
    suma=0
    num1=int(input("Ingrese un valor: "))
    num2=int(input("Ingrese un valor: "))   
    suma=num1+num2
    print("La suma es: ",suma)

def despedida():
    print("******************************************")
    print("Esperamos que te haya gustado ^^")
    print("******************************************")

presentación()
carga_valores()
despedida()