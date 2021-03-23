#Desarrollar un programa que solicite 
#la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.

suma=0
for f in range(10):
    valor=int(input("Ingrese el valor: "))
    if f>=5:
        suma=suma+valor
print(suma)