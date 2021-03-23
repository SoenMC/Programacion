'''
Desarrollar una funcion que reciba un string como parametro y nos muestre la cantidad de vocales.
Llamarla desde el bloque principal del programa 3 veces con string distintos.
'''


def contar_vocales(string):
    cont=0
    for x in range(len(string)):
        if  string[x]== "a" or string[x]== "e" or string[x]== "i" or string[x]== "o" or string[x]== "u":
            cont=cont+1
    print("La cantidad de vocales de", string, "es", cont)

contar_vocales("Hola mundo")
contar_vocales("Parangacutiminicuaro")
contar_vocales("Sergio")