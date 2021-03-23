##Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

x=1
cantidad=0
n=int(input("Ingrese la cantidad de alturas: "))
while x<=n:
    altura=float(input("Ingrese la altura: "))
    cantidad=cantidad+altura
    x=x+1
promedio=cantidad/n
print(f"El promedio de las alturas es: {promedio}")
    