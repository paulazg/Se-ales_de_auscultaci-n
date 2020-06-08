# -*- coding: utf-8 -*-
"""
Created on Sun May 31 19:09:49 2020

@author: ASUS
"""
import glob
import numpy as np
import pandas as pd

from pre_procesamiento import preprocesamiento_senal
from ciclos_respiratorios import ciclos_respiratorios_f
from operaciones_ciclos import indices
import matplotlib.pyplot as plt
import seaborn as sns
import librosa
from IPython import get_ipython



ruta_archivo= r"C:\Users\ASUS\Desktop\7 SEMESTRE PAULA\bioseñales y sistemas\proyecto 3\respiratory-sound-database\Respiratory_Sound_Database\Respiratory_Sound_Database\audio_and_txt_files"  #Ruta donde se encuentra los archivos de audio y los archivos txt

archivos_audio= glob.glob(ruta_archivo + "\*.wav") #Se generan todas las rutas de archivo correspondientes a los archivos de audio
archivos_texto= glob.glob(ruta_archivo + "\*.txt") #Se generan todas las rutas de archivo correspondientes a los archivos de texto


estado=[] #Lista donde se guarda la información correspondiente al estado de cada ciclo
varianza=[] #Lista donde se guarda la información correspondiente a la varianza de cada ciclo
rango=[] #Lista donde se guarda la información correspondiente al rango de cada ciclo
sma=[] #Lista donde se guarda la información correspondiente a el promedio móvil de cada ciclo
welch=[] #Lista donde se guarda la información correspondiente a el promedio espectral de cada ciclo

cont_arch_t=-1
for archivo in archivos_audio: #For que recorre todos los archivos de audio y texto
#for archivo in range(2):
    
    cont_arch_t=cont_arch_t+1 #Cuenta cada archivo
    print(cont_arch_t)
    #print(archivos_audio[cont_arch_t])
    preprocesado= preprocesamiento_senal(archivo)[2] #Se realiza el procesado a cada archivo de audio
    #preprocesado= preprocesamiento_senal(archivos_audio[cont_arch_t])[2]
    inf_ciclos_est_sib= ciclos_respiratorios_f(preprocesado,archivos_texto[cont_arch_t]) #Se crea el diccionario donde irá la información de todos los ciclos
    
    #inf_indices= indices(inf_ciclos_est_sib["ciclo1"][0])
    
#    inf_ciclos_est_sib= ciclos_respiratorios(archivos_audio[0],archivos_texto[0])
    
    #espectro= espectro_frecuencia(ciclos_est_sib["ciclo1"][0])
    
    
    
# prueba audio
    #librosa.output.write_wav("ensayo_audio_1.wav",preprocesado, 22050)
    
    
    
    cont=0
      # 0:ok   1:estortor   2: sibilancia   3: ambos
    for ciclo in inf_ciclos_est_sib: #Es un for para saber que estado tiene el ciclo
        cont=cont+1
        #print(inf_ciclos_est_sib[ciclo][1])
        if int(inf_ciclos_est_sib[ciclo][1])==0:
            if int(inf_ciclos_est_sib[ciclo][2])==0: #Estado normal
                #estado.append("Normal")
                estado.append(0)
            if int(inf_ciclos_est_sib[ciclo][2])==22050: # Sibilancia
                #estado.append("Sibilancia")
                estado.append(2)
        
        if int(inf_ciclos_est_sib[ciclo][1])==22050:
            if int(inf_ciclos_est_sib[ciclo][2])==0: #Estertor
                #estado.append("Estertor")
                estado.append(1)
            if int(inf_ciclos_est_sib[ciclo][2])==22050: #Ambos
                #estado.append("Ambos")
                estado.append(3)
                
        inf_indices= indices(inf_ciclos_est_sib["ciclo"+str(cont)][0]) #Se sacan todos los índices explicados en la tesis
        varianza.append(inf_indices[0]) # Se generan las lstas que contendrá cada índice
        rango.append(inf_indices[1])
        sma.append(inf_indices[2])
        welch.append(inf_indices[3])
        

#-------------------------------------------DATAFRAME---------------------------------------------------------------

diccionario_dataframe={"Varianza": varianza, "Rango": rango, "Promedio móvil": sma, "Promedio espectro": welch, "Estado": estado} #Se genera un diccionario con todos los índices y el estado del ciclo
df= pd.DataFrame(diccionario_dataframe) #Se genera el dataframe de una manera organizada para visualizar mejor los datos

# Guardado dataframe como csv
#df.to_csv("informacion_dataframe_2.csv", index= False)
#df_2_2= pd.read_csv("informacion_dataframe_2.csv")

df.to_csv("informacion_rutina_1_est_separado.csv", index= False) #Se carga el dataframe anteriormente creado y guardado en un archivo csv
#rutina_total= pd.read_csv("informacion_rutina_1.csv")


