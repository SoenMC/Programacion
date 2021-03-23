'''
En el bloque principal del programa cargar los lados de dos rectángulos
y luego mostrar cual de los dos tiene una superficie mayor.
'''

  
def retornar_superficie(lado1,lado2):
    superficie=lado1*lado2
    return superficie


# bloque principal

print("Primer rectangulo")
lado1=int(input("Base: "))
lado2=int(input("Altura: "))
print("Segundo rectangulo")
lado3=int(input("Base: "))
lado4=int(input("Altura: "))
if retornar_superficie(lado1,lado2)==retornar_superficie(lado3,lado4):
    print("Los dos rectangulos tiene la misma superficie")
else:
    if retornar_superficie(lado1,lado2)>retornar_superficie(lado3,lado4):
        print("El primer rectangulo tiene una superficie mayor")
    else:
        print("El segundo rectangulo tiene una superficie mayor")

