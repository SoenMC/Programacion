'''
Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.
'''

lista=[5, 10, 20, 15, 10]
suma=0
x=0
while x<len(lista):
    suma=suma+lista[x]
    x=x+1 

print("Los elementos de la lista son: ",lista)
print("La suma es: ",suma)    