'''
1. Buscar un excel en internet con la poblacion y area por departamentos de colombia

2. Calcular
    2.1 Total de area del pais
    2.2 Promedio de area por departamento
    2.3 Departamento con mayor poblacion
    2.4 Departamento con menor poblacion 
    2.5 Promedio de poblacion por departamento
    2.6 Relacion de poblacion y area

3.Graficar
    3.1 Grafico de barras de departamento y poblacion
    3.2 Grafico de barras de departamento y area
    3.3 Grafico de barras de departamento y poblacion - HORIZONTAL
    3.4 Grafico de barras departamento y areas - HORIZONTAL
    3.5 Grafico de torta para poblacion por departamento
    3.6 Grafico de toratas para area por departamento 
'''

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


archivo=pd.read_excel("C:\\Users\\Usuario\\Documents\\DocP.xlsx")
n_dep=archivo['Departamento']
pob=archivo['Poblacion']
area=archivo['Area']

def calc_area():
    total_area=archivo['Area'].sum()
    return total_area

#promedio de area por departamento 
def prom_adep():
    sum_area=archivo['Area'].sum()
    prom_adep=sum_area/len(n_dep)
    return prom_adep

#Departamento con mayor poblacion
def dep_mayp():
    pob_may=0
    for x in range(len(n_dep)):
        var=archivo.loc[x,'Poblacion']
        if var>pob_may:
            pob_may=var
    return pob_may   

#departamento con menor poblacion 
def dep_menp():
    pob_men=9999999999
    for x in range(len(n_dep)):
        var2=archivo.loc[x,'Poblacion']
        if var2<pob_men:
            pob_men=var2
    return pob_men         

#promedio de poblacion por departamento
def prom_pobd():
    pob_tot=archivo['Poblacion'].sum()
    prom=pob_tot/len(n_dep)  
    return prom          

#Habitantes por km^2
def hab_km():
    hab_tot=archivo['Poblacion'].sum()
    area_tot=archivo['Area'].sum()
    tot=hab_tot/area_tot
    return tot   

        
print("El area total del País es:",calc_area())
print(f"El promedio de area por departamento es: {prom_adep():.0f}","km^2")
print("El departamento con mayor poblacion es ?, con:",dep_mayp(),"habitantes")
print("El departamento con menor poblacion es ?, con:",dep_menp(),"habitantes")
print(f"El promedio de poblacion por departamento es: {prom_pobd():.0f}")
print(f"Hay {hab_km():.0f}","habitantes por km^2 en Colombia")

fig, ax=plt.subplots()
ax.set_title('GRAFICO DE DEPARTAMENTO Y POBLACION')
ax.set_ylabel('Poblacion')
ax.set_xlabel('Departamento')
#Crear grafico
plt.bar(n_dep,pob)
plt.show()


fig, ax=plt.subplots()
ax.set_title('GRAFICO DE DEPARTAMENTO Y AREA')
ax.set_ylabel('AREA km^2')
ax.set_xlabel('Departamento')
#Crear grafico
plt.bar(n_dep,area)
plt.show()
