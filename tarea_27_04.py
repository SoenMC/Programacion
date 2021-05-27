'''
Implementar con funciones tres metodos de ordenamiento 

cargar datos 
ord burbuja
ord insercion 
ord shell
salir

usar funciones
'''
print("Ingrese los valores de la lista que desea ordenar")
lista_enteros=[]
def carga_datos(lista_enteros):
    for x in range(10):
        valor=int(input("Valor: "))
        lista_enteros.append(valor)

carga_datos(lista_enteros) 



def pedirNumeroEntero():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
 
    print ("1. Opcion 1")
    print ("2. Opcion 2")
    print ("3. Opcion 3")
    print ("4. Salir")
     
    print ("Elige una opcion")
 
    opcion = pedirNumeroEntero()
 
    if opcion == 1:
        print ("Ordenamiento burbuja")
        def ord_burbuja(lista_desordenada):
            for x in range(1,len(lista_enteros)-1):
                for i in range(0,len(lista_enteros)-1):
                    if lista_enteros[i]>lista_enteros[i+1]:
                        aux=lista_enteros[i]
                        lista_enteros[i]=lista_enteros[i+1]
                        lista_enteros[i+1]=aux
                        
        ord_burbuja(lista_enteros)
        print(lista_enteros)
            
    elif opcion == 2:
        print ("Ordenamiento inserción")
        def ord_insercion(lista_desordenada):
            for x in range(1,len(lista_enteros)):

                valorActual = lista_enteros[x]
                posicion = x

                while posicion>0 and lista_enteros[posicion-1]>valorActual:
                    lista_enteros[posicion]=lista_enteros[posicion-1]
                    posicion = posicion-1

                lista_enteros[posicion]=valorActual

        #unaLista = [54,26,93,17,77,31,44,55,20]
        ord_insercion(lista_enteros)
        print(lista_enteros)

    elif opcion == 3:
        print("Ordenamiento Seleccion")
        def ord_seleccion(lista_desordenada):
            for x in range(len(lista_enteros)-1,0,-1):
                posicionDelMayor=0
                for i in range(1,x+1):
                    if lista_enteros[i]>lista_enteros[posicionDelMayor]:
                        posicionDelMayor = i

                temp = lista_enteros[x]
                lista_enteros[x] = lista_enteros[posicionDelMayor]
                lista_enteros[posicionDelMayor] = temp

        #unaLista = [54,26,93,17,77,31,44,55,20]
        ord_seleccion(lista_enteros)
        print(lista_enteros)
        

    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")
 
print ("Fin")