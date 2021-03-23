##Escribir un programa que solicite ingresar 10 notas de alumnos y 
#nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores


x=1
can_not=10
can_may=0
can_men=0
while x<=can_not:
    n=float(input("Ingrese las notas: "))
    if n>=7:
        can_may=can_may+1
    else:
        can_men=can_men+1    
    x=x+1
print(f"La cantidad de notas mayores o iguales a 7 es: {can_may}")
print(f"La cantidad de notas menores a 7 es: {can_men}")

            