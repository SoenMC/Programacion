##Leer las notas de una clase de informática y deducir
#todas aquellas que son NOTABLES (>= 7 y < 9).


cant=0
n=int(input("Ingrese la cantidad de calificaciones; "))
for f in range(n):
    cal=float(input("Ingrese la calificacion: "))
    if cal>=7 and cal<9:
        print("Notable")
    else:
        print("NO Notable")    
        