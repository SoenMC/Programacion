'''
Definir una lista que almacene por asignación los nombres de 5 personas.
Contar cuantos de esos nombres tienen 5 o más caracteres
'''

lista=["Sergio","Alejandro","Sandra","Alex","Valeria"]
contador=0
x=0
while x<len(lista):
    if len(lista[x])>=5:             #La "X" pasa por cada elemento de la lista #Por ese se usa para contar
        contador=contador+1                                       
    x=x+1
print("Los nombres son:",lista)
print("Cantidad de nombres con 5 o mas caracteres:",contador)        