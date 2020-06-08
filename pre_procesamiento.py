# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:25:44 2020

@author: ASUS
"""
import pywt
import numpy as np
import librosa
import librosa.display
from linearFIR_1 import filter_design, mfreqz
import scipy.signal as signal
import matplotlib.pyplot as plt

from IPython import get_ipython

#%%
#------------------------------------------ FILTRO ------------------------------------------------------------

def filtro(senal_audio):
    

    y, sr= librosa.load(senal_audio)
    #print(y[0])
    fs = sr;
    #print(sr)
    #design3
    order, lowpass = filter_design(fs, locutoff = 0, hicutoff = 1000, revfilt = 0); #Filtro pasa-bajas con frec de corte de 1000Hz
    #plot
    #mfreqz(lowpass,1,order, fs/2);
    
    order, highpass = filter_design(fs, locutoff = 100, hicutoff = 0, revfilt = 1);#Filtro pasa-altas con frec de corte de 100Hz
    #plot
    #mfreqz(highpass,1,order, fs/2);
    
    y_hp = signal.filtfilt(highpass, 1, y); #Se aplica el filtro pasa altas
    y_bp = signal.filtfilt(lowpass, 1, y_hp); #Se aplica el filtro pasa bajas
    
    
    y_bp = np.asfortranarray(y_bp)
    #print(y_bp.shape)
    
    #librosa.display.waveplot(y_bp, sr=sr);
    return(y_bp,sr) #Se retorna la señal filtrada y la frecuencia de muestreo
    
#ensayo_fl= filtro("101_1b1_Al_sc_Meditron.wav")[0]

#senal_ensayo= filtro("101_1b1_Al_sc_Meditron.wav")
#librosa.display.waveplot(senal_ensayo[0], senal_ensayo[1]);



#%%
#------------------------------------------------- WAVELET----------------------------------------------------------

def wthresh(coeff,thr):
    y   = list();
    s = wnoisest(coeff);
    for i in range(0,len(coeff)):
        y.append(np.multiply(coeff[i],np.abs(coeff[i])>(thr*s[i])));
    return y;
    
def thselect(signal):
    Num_samples = 0;
    for i in range(0,len(signal)):
        Num_samples = Num_samples + signal[i].shape[0];
    
    thr = np.sqrt(2*(np.log(Num_samples)))
    return thr

def wnoisest(coeff):
    stdc = np.zeros((len(coeff),1));
    for i in range(1,len(coeff)):
        stdc[i] = (np.median(np.absolute(coeff[i])))/0.6745;
    return stdc;


def wavelet_p(senal):
    #data, sr= librosa.load(senal)
    data, sr = filtro(senal) #se obtiene la señal filtrada por el filtro lineal
    #data = np.squeeze(mat_contents['senal']);
    #print(sr)
    LL = int(np.floor(np.log2(data.shape[0])));
    
    coeff = pywt.wavedec( data, 'db6', level=LL );
    
    thr = thselect(coeff);
    coeff_t = wthresh(coeff,thr);
    
    x_rec = pywt.waverec( coeff_t, 'db6');
    
    x_rec = x_rec[0:data.shape[0]]; #Se obtiene la señal filtrada por wavelet
    
#    plt.plot(data[0:1500],label='Original')
#    plt.plot(x_rec[0:1500],label='Umbralizada por Wavelet')
    
    x_filt = np.squeeze(data - x_rec); #Se obtiene la señal preprocesada
#    plt.plot(x_filt[0:1500],label='Original - Umbralizada')
#    plt.legend()
    return(data,x_rec,x_filt,sr) #Retorna la señal sin filtrar, filtrada por el filtro lineal, preprocesada y la frecuencia de muestreo

#get_ipython().run_line_magic('matplotlib', 'qt')    
#s= wavelet_p("101_1b1_Al_sc_Meditron.wav")
#s= wavelet_p("101_1b1_Al_sc_Meditron.wav")
#plt.plot(s[0],label='Señal Original')
#plt.plot(s[1][0:1500],label='Umbralizada por Wavelet')
#plt.plot(s[2],label='Señal preprocesada')
#plt.xlabel("Muestras")
#plt.ylabel("Magnitud")
#plt.legend()

#wer= wavelet_p("101_1b1_Al_sc_Meditron.wav")[2][794]

#%%
# ------------------------------------------ PREPROCESAMIENTO -----------------------------------------------------

def preprocesamiento_senal(senal):
    #senal_filtrada= filtro(senal)
    #senal_filtro_wavelet= reconstruccion_senal("Hard threshold","Multiple level noise","Minimax",senal_filtrada[0])
    #senal_preprocesada= (senal_filtrada[0] - senal_filtro_wavelet)
    senal_preprocesada= wavelet_p(senal) #Se obtiene la señal preprocesada
    
#    return(senal_preprocesada,senal_filtrada,senal_filtro_wavelet)
    return(senal_preprocesada) #Se retorna la señal preprocesada
    
    
 
#preprocesado= preprocesamiento_senal("101_1b1_Al_sc_Meditron.wav")[2]
#plt.subplot(2,1,1)
#plt.plot(preprocesado[0], "b")
#plt.title("Señal procesada")
#plt.subplot(2,1,2)
#plt.plot(preprocesado[1][0])
#plt.title("Señal sin procesar")
#plt.show()

#get_ipython().run_line_magic('matplotlib', 'qt')
#plt.plot(preprocesado)
#plt.show()

# ------------------------------------- -------------------------------------------------------------------------


    
























