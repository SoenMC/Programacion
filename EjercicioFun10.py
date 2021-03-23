'''
Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.
'''

def retornar_mayor(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

num1=int(input("Numero: "))      
num2=int(input("Numero: "))
print(retornar_mayor(num1,num2))     