##Se cuenta con la siguiente información:
#Las edades de 5 estudiantes del turno mañana.
#Las edades de 6 estudiantes del turno tarde.
#Las edades de 11 estudiantes del turno noche.
#Las edades de cada estudiante deben ingresarse por teclado.
#a) Obtener el promedio de las edades de cada turno (tres promedios)
#b) Imprimir dichos promedios (promedio de cada turno)
#c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un promedio de edades mayor.


suma1=0
suma2=0
suma3=0

for f in range(5):
    edad_m=int(input("Ingrese la edad de los 5 estudiantes de la mañana: "))
    suma1=suma1+edad_m
    prom_m=suma1/5
for f in range(6):
    edad_t=int(input("Ingrese la edad de los 6 estudiantes de la tarde: "))
    suma2=suma2+edad_t
    prom_t=suma2/6
for f in range(11):
    edad_n=int(input("Ingrese la edad de los 11 estudiantes de la noche: "))
    suma3=suma3+edad_n
    prom_n=suma3/11 
if prom_m>prom_t and prom_m>prom_n:
    print("El primedio de edades mayor es el turno de la mañana")
else:
    if prom_t>prom_m and prom_t>prom_n:
        print("El primedio de edades mayor es el turno de la tarde")
    else:
        print("El primedio de edades mayor es el turno de la noche")        
print(f"El promedio de edad de los de la mañana es: {prom_m:.2f}")
print(f"El promedio de edad de los de la tarde es: {prom_t:.2f}")
print(f"El promdeio de edad de los de la noche es: {prom_n:.2f}")