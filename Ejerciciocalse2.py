##Leer 3 numeros enteros, escribo 1 o 2 si la quiere de mayor a menor(1) o de menor a mayor(2)
##tambien dar por si los numeros son iguales 

x=int(input("Numeros de mayor a menor digite 1 "))
z=int(input("Numeros de menor a mayor digite 2 "))
a=int(input("primer numero ->: "))
b=int(input("segundo numero ->: "))
c=int(input("tercer numero ->: "))
if x==1:
    print("Numeros de mayor a menor ")
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
            print(a)
            print(c)
    elif c>a and c>b:
        print(c)
        if a>b:
            print(a)
            print(b)
        else:
            print(b)
            print(a)        
if z==2:
    print("Numeros de menor a mayor")
    if a<b and a<c:
        print(a)
        if b<c:
            print(b)
            print(c)
        else:
            print(c)
            print(b)
    elif b<a and b<c:
        print(b)
        if a<c:
            print(a)
            print(c)
        else:
            print(a)
            print(c)
    elif c<a and c<b:
        print(c)
        if a<b:
            print(a)
            print(b)
        else:
            print(b)
            print(a)
if a==b and a==c and b==a and b==c and c==a and c==b:
    print("Todos los numeros son iguales")                 
      

