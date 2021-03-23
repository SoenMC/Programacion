##Escribir un programa que calcule la suma de los cuadrados de los 100 primeros números enteros.




suma=0
for f in range(100):
    num_cua=f**2
    suma=suma+num_cua
print(f"La suma total de todos los cuadrados es: {suma}")   