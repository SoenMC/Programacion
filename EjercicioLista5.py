'''
Definir una lista por asignación con 5 enteros.
Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.
'''

lista=[4, 7, 9, 6, 10]
x=0
print("Los numeros mayores o iguales a 7 son:")
while x<len(lista):
    if lista[x]>=7:
        print(lista[x])
    x=x+1    