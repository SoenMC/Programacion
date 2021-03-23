##Calcular la suma de los n primeros números enteros utilizando la estructura desde.


suma=0
x=0
n=int(input("Cantidad de numeros a sumar: "))
while x<n:
    valor=int(input("Ingrese los valores: "))
    suma=valor+suma
    x=x+1
print(suma)   