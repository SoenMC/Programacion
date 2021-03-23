'''
Hallar el perimetro de un triangulo rctagunlo conociendo dos catetos
'''


import math

cateto_1=0
cateto_2=0

def titulo():
    print("Vamos a calcular la hipotenusa")

def calcular_hipotenusa(cateto_1,cateto_2):
    redicando=0
    hipotenusa=0
    redicando=math.pow(cateto_1,2)+math.pow(cateto_2,2)
    hipotenusa=math.sqrt(redicando)  
    print(hipotenusa)  


titulo()
cateto_1=int(input("Cateto 1: "))
cateto_2=int(input("Cateto 2 :"))
calcular_hipotenusa(cateto_1,cateto_2) 
