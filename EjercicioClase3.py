##Calcular la definitiva para N estudiantes 
#Definitiva por estudiante 
#Calcular la cantidad de estudiantes que aprobaron 
#Calcular la cantidad de estudiantes que reprobaron 
#calcular el promedio del grupo
#Calcular el promedio de los estudiantes que aprobaron 
#Calcular el promedio de los esttudiantes que reprobaron 
#Identificar la maxima nota
#Identificar la minima nota

aprobaron=0
reprobaron=0
prom_rep=0
prom_apr=0

n=int(input("Ingrese la cantidad de estudiantes: "))
for f in range(n):
    nom_est=(input("Ingrese el nombre del estudiante: "))
    nota1=float(input("Ingrese la primera nota: "))
    nota2=float(input("Ingrese la segunda nota: "))
    nota3=float(input("Ingrese la tercera nota: "))          
    not_def=(nota1+nota2+nota3)/3  
    print(f"La definitiva de este estudiante es: {not_def:.2f}") 
    if not_def>=3:
        aprobaron=aprobaron+1
        prom_apr=not_def/aprobaron     
    else:
        reprobaron=reprobaron+1
        prom_rep=not_def/reprobaron
    if nota1>nota2 and nota1>nota3:
        print(f"La nota {nota1} es la maxima")
    else:
        if nota2>nota1 and nota2>nota3:
            print(f"La nota {nota2} es la maxima")
        else:
            print(f"La nota {nota3} es la maxima")
    if nota1<nota2 and nota1<nota3:
        print(f"La nota {nota1} es la minima")
    else:
        if nota2<nota1 and nota2<nota3:
            print(f"La nota {nota2} es la minima")
        else:
            print(f"La nota {nota3} es la minima")            
       
prom_gru=not_def/n     
 
print(f"La cantidad de estudiantes que aprobaron: {aprobaron:.2f}")
print(f"La cantidad de estudiantes que reprobaron: {reprobaron:.2f}")
print(f"El promedio del grupo es: {prom_gru:.2f}")
print(f"Promedio de los estudiantes reprobados: {prom_rep:.2f}")
print(f"Promedio de los estudiantes aprobados: {prom_apr:.2f}")  