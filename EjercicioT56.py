#Se desea leer las calificaciones de una clase de informática
#y contar el número total de aprobados (5 omayor que 5).



cant=0
n=int(input("Ingrese la cantidad de calificaciones; "))
for f in range(n):
    cal=float(input("Ingrese la calificacion: "))
    if cal>=5:
        cant=cant+1
print(f"El total de aprobados es: {cant}")
        
