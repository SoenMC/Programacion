##Realizar un programa que lea los lados de n triángulos, e informar:
#a) De cada uno de ellos, qué tipo de triángulo es:
#equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
#b) Cantidad de triángulos de cada tipo.


cont1=0
cont2=0
cont3=0
n=int(input("Ingrese la cantidad de triangulos: "))
for f in range(n):
    lado1=int(input("Ingrese el lado 1: "))
    lado2=int(input("Ingrese el lado 2: "))
    lado3=int(input("Ingrese el lado 3: "))
    if lado1==lado2 and lado1==lado3:
        print("Es un triangulo equilátero")
        cont1=cont1+1
    else:
        if lado1==lado2 or lado1==lado3 or lado2==lado3:
            print("Es un triangulo isósceles")
            cont2=cont2+1
        else:
            print("Es un triangulo escaleno")
            cont3=cont3+1  
print(f"La cantidad de triangulos equiláteros es: {cont1}")
print(f"La cantidad de triangulos Isósceles es : {cont2}")
print(f"La cantidad de triangulos escalenos es: {cont3}")