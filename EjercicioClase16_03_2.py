'''
Leer 2 numeros y calcular la combinatoria de esos 2 numeros 
'''

fac_m=1
fac_n=1
fac_mn=1
x=1

m=int(input("Valor m:  "))
n=int(input("Valor n: "))


for i in range(1,m+1,1):
    fac_m=fac_m*i
print("Factorial m:",fac_m)

while x<=n:
    fac_n=fac_n*x
    x=x+1
print("Factorial n:",fac_n)  

fac_dif=m-n
for j in range(1,fac_dif+1,1):
    fac_mn=fac_mn*j
print("Factorial m-n:",fac_mn)  

combinatoria_mn=fac_m/(fac_n*fac_mn)
print("La combinatoria es:",combinatoria_mn)