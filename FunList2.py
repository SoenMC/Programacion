'''
Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros.
Implementar una función que imprima el mayor y el menor valor de la lista.
'''

def mayor_menor(lista):
    men=lista[0]
    may=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
        else:
            if lista[x]<men:
                men=lista[x]
    print("El mayor de la lista es:",may)
    print("EL menor de la lista es:",men)       

lista=[]
for x in range(5):
    valor=int(input("Valor: "))
    lista.append(valor)
print(lista)    
mayor_menor(lista)                     