##Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el plano.
#Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto cuadrante.
#Al comenzar el programa se pide que se ingrese la cantidad de puntos a procesar.

cont1=0
cont2=0
cont3=0
cont4=0
n=int(input("Ingrese la cantidad de puntos a procesar: "))
for f in range(n):
    coo_x=int(input("Ingrese el valor en x: "))
    coo_y=int(input("Ingrese el valor en y: "))
    if coo_x>0 and coo_y>0:
        cont1=cont1+1
    else:
        if coo_x<0 and coo_y>0:
            cont2=cont2+1
        else:
            if coo_x<0 and coo_y<0:
                cont3=cont3+1
            else:
                if coo_x>0 and coo_y<0:
                    cont4=cont4+1        
print(f"En el primer cuadrante se ingresaron {cont1} puntos")   
print(f"En el segundo cuadrante se ingresaron {cont2} puntos") 
print(f"En el tercer cuadrante se ingresaron {cont3} puntos") 
print(f"En el cuarto cuadrante se ingresaron {cont4} puntos")                      