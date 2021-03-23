##Escribir un programa que solicite por teclado 10 notas de alumnos 
#y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.



aprob=0
reprob=0
for f in range(10):
    notas=float(input("Ingrese las notas: "))
    if notas>=7:
        aprob=aprob+1
    else:
        reprob=reprob+1  
print(f"La cantidad de notas mayores o iguales a 7 es: {aprob}")
print(f"La cantidad de notas menores a 7 es: {reprob}")        