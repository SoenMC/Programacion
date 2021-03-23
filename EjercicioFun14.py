'''
Confeccionar una función que calcule la superficie de un rectángulo y la retorne,
la función recibe como parámetros los valores de dos de sus lados:
'''

def superficie_rectangulo(lado1,lado2):
    sup=lado1*lado2
    return sup

lado1=int(input("Base : "))   
lado2=int(input("Altura: ")) 
print("La superficie del rectangulo es: ",superficie_rectangulo(lado1,lado2)) 