##Confeccionar un programa que lea n pares de datos, 
#cada par de datos corresponde a la medida de la base y la altura de un triángulo.
#El programa deberá informar:
#a) De cada triángulo la medida de su base, su altura y su superficie.
#b) La cantidad de triángulos cuya superficie es mayor a 12.

tri_m=0
n=int(input("Cuantos triangulos va a ingresar: "))
for f in range(n):
    base=int(input("Ingrese la base: "))
    altura=int(input("Ingrese la altura "))
    print(f"La base es : {base}")
    print(f"La altura es : {altura}")   
    superficie=base*altura/2
    print(f"La superficie es : {superficie}")
    if superficie>12:
        tri_m=tri_m+1
print(f"La cantidad de triangulos con superficie mayor a 12 es: {tri_m} ")
        
