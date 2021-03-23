'''
Desarrollar un programa que permita ingresar el lado de un cuadrado.
Luego preguntar si quiere calcular y mostrar su perímetro o su superficie.
'''

def mostrar_perimetro(lado):
    per=lado*4
    print("El perimetro es",per)

def mostrar_superficie(lado):
    sup=lado*lado
    print("La superficie es",sup)

def lado():
    lado=int(input("Ingrese un lado del cuadrado: "))
    respuesta=input("Quiere calcular el perimetro o la superficie [ingresar texto: perimetro/superficie]?: ")
    if respuesta=="perimetro":
        mostrar_perimetro(lado)
    if respuesta=="superficie":
        mostrar_superficie(lado)

lado()                    