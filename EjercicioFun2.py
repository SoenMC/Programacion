'''
Confeccionar una aplicación que solicite la carga de dos valores enteros y muestre su suma.
Repetir la carga e impresion de la suma 5 veces.
Mostrar una línea separadora después de cada vez que cargamos dos valores y su suma.
'''

def carga_valores():
    val1=int(input("Digite un valor: "))
    val2=int(input("Digite un valor: "))
    suma=0
    suma=val1+val2
    print("La suma es :", suma)
      
for x in range(5):
    carga_valores()