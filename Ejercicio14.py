##Confeccionar un programa que lea por teclado tres números enteros distintos y nos muestre el mayor.

num1=int(input("ingrese el primer valor "))
num2=int(input("ingrese el segundo valor "))
num3=int(input("ingrese el tercer valor "))
print("El valor mayor es")
if num1>num2 and num1>num3:
    print(num1)
else:
    if num2>num3:
        print(num2)
    else:
        print(num3)       