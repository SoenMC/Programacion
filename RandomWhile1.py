#Escribir un programa que genere aleatoriamente 100 datos
#y sume todos los números, los negativos, los positivos y calcule el promedio de todos los números,
#de los positivos y los negativos;
#además que calcule el mayor y el menor de todos los números, de los positivos y los negativos



import random


x=1
num=0
can_num=0
can_num_pos=0
can_num_neg=0
suma_tot=0
suma_pos=0
suma_neg=0
prom_tot=0
prom_pos=0
prom_neg=0
num_may=0
num_menor=0

max_num=int(input("Ingrese la cantidad de numeros: "))
while x<=max_num:
    num=random.randint(-100, 100)
    print(num)
    suma_tot=suma_tot+num
    can_num=can_num+1
    prom_tot=suma_tot/can_num
    if num>0:
        suma_pos=suma_pos+num
        can_num_pos=can_num_pos+1
        prom_pos=suma_pos/can_num_pos
    else:
        suma_neg=suma_neg+num
        can_num_neg=can_num_neg+1
        prom_neg=suma_neg/can_num_neg 
    x=x+1   
  
print(f"La suma total es: {suma_tot}")
print(f"La suma de positivos es: {suma_pos}")
print(f"La suma de negativos es: {suma_neg}")   
print(f"El promedio total es: {prom_tot}")
print(f"El promedio positivo es: {prom_pos}")
print(f"El promedio negativo es: {prom_neg}")         