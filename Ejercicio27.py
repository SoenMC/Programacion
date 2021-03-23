##En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500,
#realizar un programa que lea los sueldos que cobra cada empleado
#e informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más de $300.
#Además el programa deberá informar el importe que gasta la empresa en sueldos al personal.

x=1
can_men=0
can_may=0
importe=0
n=int(input("Ingrese la cantidad de empleados: "))
while x<=n:
    sueldo=int(input("Ingrese el sueldo: "))
    importe=importe+sueldo
    x=x+1
    if sueldo>=100 and sueldo<=300:
        can_men=can_men+1
    else:
        can_may=can_may+1
print(f"La cantidad de empleados que cobran mas de 100 dolares y menos de 300 dolares es: {can_men}")
print(f"La cantidad de empleados que cobran mas de 300 dolares es: {can_may} ")           
print(f"El importe que gasta la empresa en el sueldo de sus empleados es de: {importe}")