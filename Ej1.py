'''
Crear un arreaglo unidimensional de 10 posiciones y realizar:
1. Almacenar datos de tipo entero
2. Sumas los datos
3. Promediar datos
4. Imprimir el mayor e informar en qu posicion se encuentra
5. Imprimir el menor e informar en qu posicion se encuentra
6. Imprimir cuantos estudiantes aprobaron la asignatura
7. Imprimir cuantos estudiantes reprobaron la asignatura
8. Cuantos estudiantes obtuvieron notas de acuerdo a la siguiente escala
    0 a 1 - 1.1 a 2.0 - 2.1 a 2.9 - 3.0 a 4.0 - 4.1 a 5.0 
'''

lista_notas = []
suma_notas = 0.0
promedio_notas = 0.0
nota_mayor = 0.0
nota_menor = 9999999999999999999999999
nota_total = 0.0
cant_aprobados=0
cant_reprobados=0
est_cero_uno=0
est_uno1_dos=0
est_dos1_dos9=0
est_tres_cuatro=0
est_cuatro1_cinco=0
#pedimos las notas
for x in range(5):
    notas=float(input("Ingrese la nota: "))
    #Adicionar notas a la lista
    lista_notas.append(notas)
print(lista_notas)

#sumar las notas
for x in range(len(lista_notas)):
    suma_notas=suma_notas+lista_notas[x]
print("La suma es:",suma_notas)

#promedio notas
promedio_notas=suma_notas/5
print("El promedio es:",promedio_notas)  

for x in range(len(lista_notas)):
    if lista_notas[x]>nota_mayor:
        nota_mayor=lista_notas[x]    
print("La nota mayor es:",nota_mayor)


for x in range(len(lista_notas)):
    if lista_notas[x]<nota_menor:
        nota_menor=lista_notas[x]
print("La nota menor es:",nota_menor) 

for x in range(len(lista_notas)):
    if lista_notas[x]>=3:
        cant_aprobados +=1
    else:
        cant_reprobados +=1
print("La cantidad de aprobados es:",cant_aprobados)
print("La cantidad de reprobados es:",cant_reprobados) 

for x in range(len(lista_notas)):
    if lista_notas[x]==0.0 or lista_notas[x]==0.1 or lista_notas[x]==0.2 or lista_notas[x]==0.3 or lista_notas[x]==0.4 or lista_notas[x]==0.5 or lista_notas[x]==0.6 or lista_notas[x]==0.7 or lista_notas[x]==0.8 or lista_notas[x]==0.9 or lista_notas[x]==1.0:
        est_cero_uno +=1
    else:
        if lista_notas[x]==1.1 or lista_notas[x]==1.2  or lista_notas[x]==1.3 or lista_notas[x]==1.4 or lista_notas[x]==1.5 or lista_notas[x]==1.6 or lista_notas[x]==1.7 or lista_notas[x]==1.8 or lista_notas[x]==1.9 or lista_notas[x]==2.0:
            est_uno1_dos +=1
        else:
            if lista_notas[x]==2.1 or lista_notas[x]==2.2  or lista_notas[x]==2.3 or lista_notas[x]==2.4 or lista_notas[x]==2.5 or lista_notas[x]==2.6 or lista_notas[x]==2.7 or lista_notas[x]==2.8 or lista_notas[x]==2.9:
                est_dos1_dos9 +=1
            else:
                if lista_notas[x]==3.0 or lista_notas[x]==3.1  or lista_notas[x]==3.2 or lista_notas[x]==3.3 or lista_notas[x]==3.4 or lista_notas[x]==3.5 or lista_notas[x]==3.6 or lista_notas[x]==3.7 or lista_notas[x]==3.8 or lista_notas[x]==3.9 or lista_notas[x]==4.0:
                    est_tres_cuatro +=1
                else:
                    if lista_notas[x]==4.1 or lista_notas[x]==4.2  or lista_notas[x]==4.3 or lista_notas[x]==4.4 or lista_notas[x]==4.5 or lista_notas[x]==4.6 or lista_notas[x]==4.7 or lista_notas[x]==4.8 or lista_notas[x]==4.9 or lista_notas[x]==5.0:
                        est_cuatro1_cinco +=1    

print("Cantidad de estudiantes en la escala 0 a 1:",est_cero_uno)
print("Cantidad de estudiantes en la escala 1.1 a 2:",est_uno1_dos)
print("Cantidad de estudiantes en la escala 2.1 a 2.9:",est_dos1_dos9)
print("Cantidad de estudiantes en la escala 3.0 a 4.0:",est_tres_cuatro)
print("Cantidad de estudiantes en la escala 4.1 a 5.0:",est_cuatro1_cinco)