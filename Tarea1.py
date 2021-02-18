##Leer nombre de un estudiante, las notas de los tres parciales, el acomulado de inasistencias y calcular
##la nota definitiva sabiendo que primer parcial tiene un porcentaje de 35%, el swgundo parcial 35%
##y el tercer parcial 30%. 
##Imprimir la nota definitiva mas un concepto: 
# Ganó academicamente        fallas < a 12 y nota definitiva >= 3 
# perdió academicamente      fallas < a 12 y nota definitiva < 3 
# perdio inasistencia         fallas > a 12 y nota definitiva no importa se divide por la mitad
# perdió academicamente y por inasistencia > a 12 y nota definitiva < 3


Nombre=input("Ingrese el nombre ")
par1=int(input("Ingrese nota del primer parcial "))
par2=int(input("Ingrese nota del segundo parcial "))
par3=int(input("Ingrese nota del tercer parcial ")) 
tot_InAsis=int(input("Ingrese el total de las inasistencias "))
not_def=(par1+par2+par3)/3
print("La nota definitiva es ")
print(not_def)
if tot_InAsis<12 and not_def>=3:
    print("Ganó academicamente")
if tot_InAsis<12 and not_def<3:
    print("Perdió academicamente")    
if tot_InAsis>12 and not_def==not_def:
    print("Perdió por inasistencia")   
if tot_InAsis>12 and not_def<3:
    print("y academicamente")