# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 17:07:44 2020

@author: ASUS
"""
import pandas as pd
from IPython import get_ipython
import matplotlib.pyplot as plt
import seaborn as sns

#-------------------------------------- FUNCIONES BÁSICAS -----------------------------------------------------

df_ejemplo= pd.read_csv("informacion_rutina.csv")
#df3= pd.read_csv("informacion_dataframe_2.csv")

# Tabla resumen con la media y desviación estándar de todos los datos
tabla_contenido= df_ejemplo.describe()


# Diagrama de bigotes
get_ipython().run_line_magic('matplotlib', 'qt')
#var="Varianza"
var= "Estado"
dr= "Promedio espectro"
datos= pd.concat([df_ejemplo[dr],df_ejemplo[var]],axis=1)
f, ax = plt.subplots(figsize=(8, 6))
fig = sns.boxplot(x=var, y=dr, data=datos)
#fig.axis(ymin=0, ymax=0.04);
fig.axis(xmin=-1,xmax=4)
plt.title("Caja de bigotes")


#Diagrama de dispersión
set(df_ejemplo.Estado)
colors={0:"DeepPink",1:"RoyalBlue",2:"BlueViolet", 3:"Aqua"}
colores= df_ejemplo.Estado.map(colors)
fig,ax= plt.subplots()
ax.scatter(df_ejemplo.Estado,df_ejemplo.Varianza, color= colores)
plt.xlabel("Estados")
plt.ylabel("Varianza")
plt.title("Diagrama de dispersión")
plt.grid()

#Histograma
get_ipython().run_line_magic('matplotlib', 'qt')
histograma= df_ejemplo.hist(column="Estado", color="BlueViolet")   
#histograma= df_ejemplo.hist()  
plt.ylabel("Número de ciclos")
plt.title("Histograma del estado de los pacientes")
plt.xlabel("Valores representativos del estado")


# Función de probabilidad
sns.distplot(df_ejemplo["Varianza"])

#Matriz de correlación
datos_matriz= df_ejemplo.corr()
f, ax= plt.subplots(figsize=(10,8))
sns.heatmap(datos_matriz, vmax=.8, square=False,annot=True)
plt.title("Matriz de correlación")

# Regresión lineal (Según correlación)(para verificar si hay tendencia)
get_ipython().run_line_magic('matplotlib', 'qt')
datos= pd.concat([df_ejemplo["Varianza"],df_ejemplo["Promedio espectro"]],axis=1)
f, ax = plt.subplots(figsize=(8, 6))
fig = sns.regplot(x="Promedio espectro", y="Varianza", data=datos)
#fig.axis(ymin=0, ymax=0.04);
#fig.axis(xmin=-1,xmax=4)
plt.title("Regresión lineal")
plt.grid()

#Diagramas de dispersión entre estado y sus variables correlacionados
sns.set()
cols=["Estado","Varianza","Rango","Promedio móvil","Promedio espectro"]
sns.pairplot(df_ejemplo[cols], size= 2)
plt.show()






