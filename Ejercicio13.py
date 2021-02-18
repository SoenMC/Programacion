#Confeccionar un programa que pida por teclado tres notas de un alumno,
#calcule el promedio e imprima alguno de estos mensajes:
#Si el promedio es >=7 mostrar "Promocionado".
#Si el promedio es >=4 y <7 mostrar "Regular".
#Si el promedio es <4 mostrar "Reprobado".

not1=int(input("Ingrese la primera nota "))
not2=int(input("Ingrese la segunda nota "))
not3=int(input("Ingrese la tercera nota "))
promedio=(not1+not2+not3)/3
if promedio>=7:
    print("Promocianado")
else:
    if promedio>=4:
        print("Regular")
    else:
        print("Reprobado")    