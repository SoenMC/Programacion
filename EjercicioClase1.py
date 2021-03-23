##Leer 3 numeros enteros positivos e imprimirlos de mayor a menor 

a=int(input("Primer numero -> "))
b=int(input("Segundo numero -> "))
c=int(input("Tercer numero -> "))
if a>b and a>c:
    print(a)
    if b>c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)   
elif b>a and b>c:
    print(b)
    if a>c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
elif c>a and c>b:
    print(c)
    if a>b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)        