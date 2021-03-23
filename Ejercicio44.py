##Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a) La cantidad de valores ingresados negativos.
#b) La cantidad de valores ingresados positivos.
#c) La cantidad de múltiplos de 15.
#d) El valor acumulado de los números ingresados que son pares.

cont1=0
cont2=0
cont3=0
cont4=0
for f in range(10):
    valor=int(input("Ingrese el valor: "))
    if valor<0:
        cont1=cont1+1
    else:
        if valor>0:
            cont2=cont2+1
    if valor%15==0:
        cont3=cont3+1   
    if valor%2==0:
        cont4=cont4+valor
print(f"Cantidad de valores negativos: {cont1}")     
print(f"Cantidad de valores positivos: {cont2}")  
print(f"Cantidad de valores multiplos de 15: {cont3}")  
print(f"la suma de los valores pares es: {cont4}")  
