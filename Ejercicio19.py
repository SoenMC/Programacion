#Se ingresan tres valores por teclado, si todos son iguales
#se imprime la suma del primero con el segundo y a este resultado se lo multiplica por el tercero.

num1=int(input("Ingrese el primer numero "))
num2=int(input("Ingrese el segundo numero "))
num3=int(input("Ingrese el tercer numero "))
suma=num1+num2
prod=suma*num3
if num1==num2 and num1==num3:
    print(f"La suma es {suma}")
    print(f"El producto es {prod}")