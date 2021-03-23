##Diseñar el algoritmo para imprimir la suma de los números impares menores o iguales que n.



suma_tot=1
suma_imp=1
x=1
n=int(input("Ingrese el numero mayor: "))
while x<n:
    suma_imp=suma_imp+2
    suma_tot=suma_tot+suma_imp
    x=x+2
    print(suma_tot)
   
    
    

