##Leer 100 números. Determinar la media de los números positivos y la media de los números negativos


x=0
suma=0
suma_neg=0
cant_neg=0
cant_pos=0
promedio=0
promedio_neg=0
while x<10:
    num=int(input("Ingrese valores: "))
    if num>0:
        suma=suma+num
        x=x+1
        cant_pos=cant_pos+1
        promedio=suma/cant_pos
    else:
        suma_neg=suma_neg+num
        cant_neg=cant_neg+1
        x=x+1
        promedio_neg=suma_neg/cant_neg 
if suma==0:
    print("Sin valores positivos")
else:
    if suma_neg==0:
        print("Sin valores negativos")            
print(promedio)  
print(promedio_neg) 
