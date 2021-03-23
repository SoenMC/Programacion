'''
Definir por asignación una lista con 8 elementos enteros.
Contar cuantos de dichos valores almacenan un valor superior a 100
'''

lista=[101, 13, 333, 65, 8, 4554, 4, 1198]
contador=0
x=0
while x<len(lista):
    if lista[x]>100:
        contador=contador+1
    x=x+1
print("La cantidad de valores mayores a 100 es:",contador)    