#Se ingresa por teclado un número positivo de uno o dos dígitos (1..99)
# mostrar un mensaje indicando si el número tiene uno o dos dígitos.
#(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

num=int(input("Ingrese uno o dos digitos "))
if num<10:
    print("Tiene un digito")
else:
    print("Tiene dos digitos")