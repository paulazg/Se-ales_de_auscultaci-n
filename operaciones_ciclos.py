# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:09:41 2020

@author: ASUS
"""
import numpy as np
from scipy.fftpack import fft
from scipy import signal

def varianza(ciclo):
    var_ciclo= np.var(ciclo) #Se obtiene la varianza del ciclo
    return(var_ciclo)
    
#der= varianza(ciclos_est_sib["ciclo1"][0])
    
def rango(ciclo):
    val_max= max(ciclo) #Se obtiene el valor máximo del ciclo
    val_min= min(ciclo) #Se obtiene el valor mínimo del ciclo
    rs= abs(val_max-val_min) #Se obtiene el valor absoluto de la resta del máximo menos el mínimo
    return(rs) #Retorna el rango
    
#der= rango(ciclos_est_sib["ciclo2"][0])
    
def media_movil_simple(ciclo):
    suma= [] #Se genera la lista donde se guarda la información
    for valor in range(len(ciclo)-1):
        oper=abs(ciclo[valor]-ciclo[valor+1]) #Se obtiene el valor absoluto de la resta de una muestra menos la muestra anterior
        suma.append(oper) #Se agrega el resultado anterior a la lista
    sma= sum(suma) #Se realiza la suma de los valores de la lista
       
    
#    sma_ventanas=[]
#    for r in range(0,len(ciclo),800):
#        parte1= ciclo[r:r+800]
#        for g in range(0,len(parte1),100):
#            parte2= parte1[g:g+100]
#            
#            for valor in range(len(parte2)-1):
#                oper=abs(parte2[valor]-parte2[valor+1])
#                suma.append(oper)
#            sma= sum(suma)
#            sma_ventanas.append(sma)
#    sma_total= max(sma_ventanas)
#    
    return(sma) #Se retorna el promedio móvil grueso
            
    
    
#der= media_movil_simple(inf_ciclos_est_sib["ciclo2"][0])
    
def espectro_frecuencia(ciclo):
    fwelch_c, Pxxwelch_c = signal.welch(ciclo,22050, "hamming",1024,scaling="density"); #Se aplica el periodograma de Welch
    X= np.mean(Pxxwelch_c) # Se saca el promedio del espectro de welch
#    X= fft(ciclo)
#    X= np.mean(X)
    return(X) #Se retorna el promedio del espectro de welch
    
#espectro= espectro_frecuencia(inf_ciclos_est_sib["ciclo1"][0])
    
def indices(ciclo):
    varianza_rt= varianza(ciclo) #Se obtiene la varianza del ciclo mediante la función creada anteriormente
    rango_rt= rango(ciclo) #Rango del ciclo mediante la función creada anteriormente
    sma_rt= media_movil_simple(ciclo) #Promedio móvil del ciclo mediante la función creada anteriormente
    welch_rt= espectro_frecuencia(ciclo) #Promedio del espectro del ciclo mediante la función creada anteriormente
    return(varianza_rt,rango_rt,sma_rt,welch_rt) #Retorna todos los índices
    


