'''
Realizar la carga del nombre de una persona y luego mostrar
el primer caracter del nombre y la cantidad de letras que lo componen.
'''


def primer_caracter(nombre):
    print("El primer caracter es: ",nombre[0])
    

def cantidad_caracter(nombre):
    print("La cantidad de caracteres es: ",len(nombre))    

def nombre():
    nombre=input("Ingrese el nombre: ")
    primer_caracter(nombre)
    cantidad_caracter(nombre)

nombre()    