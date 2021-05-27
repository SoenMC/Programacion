#import os

#Variables
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
pos_menor=0
pos_mayor=0
 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	#os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - primera opción")
	print ("\t2 - segunda opción")
	print ("\t3 - tercera opción")
	print ("\t4 - tercera opción")
	print ("\t5 - tercera opción")
	print ("\t6 - tercera opción")
	print ("\t7 - tercera opción")
	print ("\t9 - salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
		print ("Cargamos los datos de la lista")
		#pedimos las notas
		for x in range(5):
			notas=float(input("Ingrese la nota: "))
			#Adicionar notas a la lista
			lista_notas.append(notas)
		print(lista_notas)

	elif opcionMenu=="2":
		print ("Sumar datos de la lista")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
		#sumar las notas
		for x in range(len(lista_notas)):
			suma_notas=suma_notas+lista_notas[x]
		print("La suma es:",suma_notas)

	elif opcionMenu=="3":
		print ("Promediar los datos")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
		#promedio notas
		promedio_notas=suma_notas/len(lista_notas)
		print("El promedio es:",promedio_notas)

	elif opcionMenu=="4":
		print ("Nota mayor y posición en la que se encuentra")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
		for x in range(len(lista_notas)):
			if lista_notas[x]>nota_mayor:
				nota_mayor=lista_notas[x]
				pos_mayor=x
		print("La nota mayor es:",nota_mayor)
		print("La posicion del numero mayor es:",pos_mayor)


	elif opcionMenu=="5":
		print ("Nota menor y la posición en la que se encuentra")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")	
		#Nota menor
		for x in range(len(lista_notas)):
			if lista_notas[x]<nota_menor:
				nota_menor=lista_notas[x]
				pos_menor=x
		print("La nota menor es:",nota_menor) 
		print("La posicion del numero menor es:",pos_menor)

	elif opcionMenu=="6":
		print ("Cuantos estudiantes aprobaron y reprobaron la asignatura")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
		#Cantidad de aprobados y reprobados 
		for x in range(len(lista_notas)):
			if lista_notas[x]>=3:
				cant_aprobados +=1
			else:
				cant_reprobados +=1
		print("La cantidad de aprobados es:",cant_aprobados)
		print("La cantidad de reprobados es:",cant_reprobados) 		

	elif opcionMenu=="7":
		print ("Cuantos estudiantes obtuvieron notas de acuerdo a la siguiente escala 0 a 1 - 1.1 a 2.0 - 2.1 a 2.9 - 3.0 a 4.0 - 4.1 a 5.0 ")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
		#Los rangos 
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

	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")