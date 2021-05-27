'''
Interactuar con datos

Fuente de datos

1. Asignar datos desde la definicion de la estructura
'''


#Importar libreria
import pandas as pd

#Crear la estructura de datos tipo DataFrame y se le asignan los datos
datos_estudiantes=pd.DataFrame({'Estudiante':['Juan','Ana','Marta'],
                                'Apellido':['Gomez','Diaz','Arango'],
                                'Edad':['13','56','24']})

#Agregar una columna y le asignamos el mismo dato
datos_estudiantes['Vivo']='TRUE'
datos_estudiantes['Genero']='Masculino'

#Insertar una columna y se asignan los datos
datos_estudiantes.insert(3,'Genero correcto',['Masculino','Femenino','Femenino'])
datos_estudiantes.insert(4,'Semestre',['Primero','Quinto','Noveno'])

#Segunda forma de agregar columna sobreescribiendo
datos_estudiantes=datos_estudiantes.assign(Colegio=['INEM','Normal','Universitaro'])

#Consultar la estructutra
print(datos_estudiantes)
print('\n')

#Eliminar registro buscando por columna
columna=datos_estudiantes[datos_estudiantes['Apellido']!='Gomez']
print(columna)
print('\n')

df=[]
df=datos_estudiantes
print(df)
print('\n')

#Llenar con ceros cualquier valor N/A en el dataframe
nuevo=pd.DataFrame(df)
nuevo.fillna(0,inplace=True)
print(nuevo)
print('\n')

#Convertir a numeros enteros
nuevo['Edad']=nuevo.Edad.astype(int)
print(nuevo.describe())
print('\n')

#Estadisticas dato mayor 
print('Promedio',nuevo['Edad'].max())

#Promedio 
print('Promedio',nuevo['Edad'].mean())




