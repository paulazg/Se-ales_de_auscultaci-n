# -*- coding: utf-8 -*-
"""
Created on Wed May 27 18:15:49 2020

@author: ASUS
"""

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.io as sio;
from IPython import get_ipython
import os.path

from IPython import get_ipython

#audio="./example_data/101_1b1_Pr_sc_Meditron.wav"


#audio = '101_1b1_Al_sc_Meditron.wav'


def ciclos_respiratorios_f(ruta_audio,ruta_anotaciones):
    
    #tipo= type(ruta_audio) is str
    
#    if tipo== True:
#        audio= ruta_audio
#        print("raro")
#        senal_c, sr = librosa.load(audio) 
#        audio_texto= sr*np.loadtxt(ruta_anotaciones)
#    
#    else:
    senal_c=ruta_audio #Recibe señal de audio preprocesada
    audio_texto= 22050*np.loadtxt(ruta_anotaciones) #Se carga el archivo txt y se multiplican los datos por la frecuencia de muestreo
        
    inf_ciclos_est_sib={} #Se crea el diccionario donde irá guardada la información correspondiente a cada ciclo y si tiene sibilancia o estertor
    
    cont=0
    for ciclo in range(len(audio_texto[:,0])): 
        cont=cont+1
        tramo1= int(round(audio_texto[ciclo,0])) #Extrae el valor donde empieza el ciclo
        tramo2= int(round(audio_texto[ciclo,1])) #Extrae el valor donde termiina el ciclo
        estertor= int(round(audio_texto[ciclo,2])) #Se obtiene la información del estertor
        sibilancia= int(round(audio_texto[ciclo,3])) #Se obtiene la información de la sibilancia
        ciclo= senal_c[tramo1:tramo2] #Se extrae el ciclo de la señal de audio con los valores anteriores
        info=[] #Se crea una lista donde se agrega el ciclo, estertor y sibilancia
        info.append(ciclo)
        info.append(estertor)
        info.append(sibilancia)
        inf_ciclos_est_sib["ciclo" + str(cont)]=info #Se va generando las claves del diccionario
        
    return(inf_ciclos_est_sib) #Se retorna el diccionario con la información
    

#ciclos_est_sib= ciclos_respiratorios_f("/Users/ASUS/Desktop/7 SEMESTRE PAULA/bioseñales y sistemas/proyecto 3/respiratory-sound-database/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/101_1b1_Al_sc_Meditron.wav","/Users/ASUS/Desktop/7 SEMESTRE PAULA/bioseñales y sistemas/proyecto 3/respiratory-sound-database/Respiratory_Sound_Database/Respiratory_Sound_Database/audio_and_txt_files/101_1b1_Al_sc_Meditron.txt")



