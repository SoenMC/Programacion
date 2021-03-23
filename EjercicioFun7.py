'''
Confeccionar una función que reciba tres enteros y nos muestre el mayor de ellos.
La carga de los valores hacerlo por teclado.
'''


def mostrar_mayor(num1,num2,num3):
    print("El mayor es")
    if num1>num2 and num1>num3:
        print(num1)
    else:
        if num2>num3:
            print(num2)
        else:
            print(num3)

def cargar_valores():
    num1=int(input("Ingrese un valor: "))   
    num2=int(input("Ingrese un valor: "))  
    num3=int(input("Ingrese un valor: "))   
    mostrar_mayor(num1,num2,num3)               

cargar_valores()     