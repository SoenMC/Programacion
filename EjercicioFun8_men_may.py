'''
Confeccionar una función que reciba tres enteros y los muestre ordenados de menor a mayor.
En otra función solicitar la carga de 3 enteros por teclado
y proceder a llamar a la primer función definida.
'''

def ordenar_enteros(num1,num2,num3):
    if num1<num2 and num1<num3:
        print(num1)
        if num2<num3:
            print(num2)
            print(num3)
        else:
            print(num3)
            print(num2)   
    elif num2<num1 and num2<num3:
        print(num2)
        if num1<num3:
            print(num1)
            print(num3)
        else:
            print(num3)
            print(num1)
    elif num3<num1 and num3<num2:
        print(num3)
        if num1<num2:
            print(num1)
            print(num2)
        else:
            print(num2)
            print(num1) 
        
def cargar_numeros():
    num1=int(input("Primer numero -> "))
    num2=int(input("Segundo numero -> "))
    num3=int(input("Tercer numero -> "))
    ordenar_enteros(num1,num2,num3)        

cargar_numeros()    