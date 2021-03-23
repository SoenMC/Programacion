##Un comercio dispone de dos tipos de artículos en
#fichas correspondientes a diversas sucursales con los
#siguientes campos:
#• código del artículo A o B,
#• precio unitario del artículo,
#• número de artículos.
#La última ficha del archivo de artículos tiene un
#código de artículo, una letra X. Se pide:
#• el número de artículos existentes de cada categoría,
#• el importe total de los artículos de cada categoría.

import random
suma=0
def listaAleatorios(n):
    lista = []
    for i in range(n):
        lista.insert(i, random.randrange(0, 1000, 2))
    return lista

print("Ingrese cuantos numeros aleatorios desea obtener")
n = int(input())

aleatorios = listaAleatorios(n)
if listaAleatorios>0:
    suma=suma+listaAleatorios
print(aleatorios)