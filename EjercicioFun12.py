'''
Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos
'''

def promedio_enteros(num1,num2,num3):
    prom=(num1+num2+num3)/3
    return prom

num1=int(input("Numero: "))    
num2=int(input("Numero: "))   
num3=int(input("Numero: ")) 
print("El promedio de los numeros es: ",promedio_enteros(num1,num2,num3))  