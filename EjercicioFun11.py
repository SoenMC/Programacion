'''
Confeccionar una función que le enviemos como parámetro un string
y nos retorne la cantidad de caracteres que tiene.
En el bloque principal solicitar la carga de dos nombres por teclado
y llamar a la función dos veces. 
Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.
'''

def largo(string):
    return len(string)

nombre1=input("Ingrese el primer nombre: ")    
nombre2=input("Ingrese el segundo nombre: ")   
largo1=len(nombre1)
largo2=len(nombre2)
if largo1==largo2:
    print("Los nombres",nombre1,nombre2, "Son iguales")
else:
    if largo1>largo2:
        print(nombre1,"Es mas largo")
    else:
        print(nombre2,"Es mas largo")        