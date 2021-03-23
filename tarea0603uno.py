##Escribir un programa que calcule la suma de los cuadrados de los N primeros números enteros.
#imprimmir su cuadrado y suma 



x=1
suma=0
num=int(input("Cantidad maxima: "))
while x<=num:
    num_cua=x**2
    suma=suma+num_cua
    print(f"El cuadrado de {x} es: {num_cua}")
    print(f"La suma es : {suma}")
    x=x+1
