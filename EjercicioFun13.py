'''
Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado
'''

def perimetro_cuadrado(lado):
    per=lado*4
    return per

lado=int(input("Lado: "))
print("El perimetro del cuadrado es: ",perimetro_cuadrado(lado))    