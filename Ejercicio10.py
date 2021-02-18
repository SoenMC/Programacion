##Realizar un programa que solicite la carga por teclado de dos números,
# si el primero es mayor al segundo informar su suma y diferencia,
# en caso contrario informar el producto y la división del primero respecto al segundo.

num1=int(input("Ingrese el primer valor "))
num2=int(input("Ingrese el segundo valor "))
if num1>num2:
    suma=num1+num2
    diferencia=num1-num2
    print("El resultado es mayor")
    print("La suma de los dos valores es")
    print(suma)
    print("La diferencia de los dos valores es")
    print(diferencia)
else:
    division=num1/num2
    producto=num1*num2
    print("El resultado es menor")
    print("La division de los dos valores es")
    print(division)
    print("El producto de los dos valores es")
    print(producto)       