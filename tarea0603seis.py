###Imprimir las treinta primeras potencias de 10,
#es decir, 10 elevado a 1, 10 elevado a 2, etc. además sumar las potencias calculadas





suma=0
x=1
while x<=30:
    pot=10**x
    print(pot)
    x=x+1
    suma=suma+pot
print(suma)    