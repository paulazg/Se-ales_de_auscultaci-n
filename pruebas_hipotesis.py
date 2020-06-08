# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:23:26 2020

@author: ASUS
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from IPython import get_ipython

from scipy.stats import ttest_ind, mannwhitneyu

df_analisis= pd.read_csv("informacion_rutina.csv")

sano= df_analisis.loc[:,"Estado"]==0
df_sano= df_analisis.loc[sano]

estertor= df_analisis.loc[:,"Estado"]==1
df_estertor= df_analisis.loc[estertor]

sibilancia= df_analisis.loc[:,"Estado"]==2
df_sibilancia= df_analisis.loc[sibilancia]

ambos= df_analisis.loc[:,"Estado"]==3
df_ambos= df_analisis.loc[ambos]




#%%      PRUEBAS DE HIPÓTESIS

#statistics, pvalues= ttest_ind(df_sano,df_estertor)
#print(pvalues<0.0125)

# Hipótesis alternativa: 
# Hipótesis nula:


# Normales vs Estertores
#varianza_normal= df_sano.iloc[:,1]
#varianza_estertor= df_estertor.iloc[:,1]

statistic_n_e=[]
pvalue_n_e=[]

prueba_nor_est_var= mannwhitneyu(df_sano.iloc[:,0],df_estertor.iloc[:,0])
statistic_n_e.append(prueba_nor_est_var[0])
pvalue_n_e.append(prueba_nor_est_var[1])

prueba_nor_est_ran= mannwhitneyu(df_sano.iloc[:,1],df_estertor.iloc[:,1])
statistic_n_e.append(prueba_nor_est_ran[0])
pvalue_n_e.append(prueba_nor_est_ran[1])

prueba_nor_est_prom_m= mannwhitneyu(df_sano.iloc[:,2],df_estertor.iloc[:,2])
statistic_n_e.append(prueba_nor_est_prom_m[0])
pvalue_n_e.append(prueba_nor_est_prom_m[1])

prueba_nor_est_prom_e= mannwhitneyu(df_sano.iloc[:,3],df_estertor.iloc[:,3])
statistic_n_e.append(prueba_nor_est_prom_e[0])
pvalue_n_e.append(prueba_nor_est_prom_e[1])

dic_n_e={"Statistic":statistic_n_e, "Pvalue":pvalue_n_e}
df_n_e= pd.DataFrame(dic_n_e, index=["Varianza","Rango","Promedio móvil","Promedio espectro"])

# Normales vs Sibilancias
#varianza_normal= df_sano.iloc[:,1]
#varianza_estertor= df_sibilancia.iloc[:,1]

statistic_n_s=[]
pvalue_n_s=[]

prueba_nor_sib_var= mannwhitneyu(df_sano.iloc[:,0],df_sibilancia.iloc[:,0])
statistic_n_s.append(prueba_nor_sib_var[0])
pvalue_n_s.append(prueba_nor_sib_var[1])

prueba_nor_sib_ran= mannwhitneyu(df_sano.iloc[:,1],df_sibilancia.iloc[:,1])
statistic_n_s.append(prueba_nor_sib_ran[0])
pvalue_n_s.append(prueba_nor_sib_ran[1])

prueba_nor_sib_prom_m= mannwhitneyu(df_sano.iloc[:,2],df_sibilancia.iloc[:,2])
statistic_n_s.append(prueba_nor_sib_prom_m[0])
pvalue_n_s.append(prueba_nor_sib_prom_m[1])

prueba_nor_sib_prom_e= mannwhitneyu(df_sano.iloc[:,3],df_sibilancia.iloc[:,3])
statistic_n_s.append(prueba_nor_sib_prom_e[0])
pvalue_n_s.append(prueba_nor_sib_prom_e[1])

dic_n_s={"Statistic":statistic_n_s, "Pvalue":pvalue_n_s}
df_n_s= pd.DataFrame(dic_n_s, index=["Varianza","Rango","Promedio móvil","Promedio espectro"])


# Estertores vs Sibilancias
#varianza_normal= df_sano.iloc[:,1]
#varianza_estertor= df_sibilancia.iloc[:,1]

statistic_e_s=[]
pvalue_e_s=[]

prueba_est_sib_var= mannwhitneyu(df_estertor.iloc[:,0],df_sibilancia.iloc[:,0])
statistic_e_s.append(prueba_est_sib_var[0])
pvalue_e_s.append(prueba_est_sib_var[1])

prueba_est_sib_ran= mannwhitneyu(df_estertor.iloc[:,1],df_sibilancia.iloc[:,1])
statistic_e_s.append(prueba_est_sib_ran[0])
pvalue_e_s.append(prueba_est_sib_ran[1])

prueba_est_sib_prom_m= mannwhitneyu(df_estertor.iloc[:,2],df_sibilancia.iloc[:,2])
statistic_e_s.append(prueba_est_sib_prom_m[0])
pvalue_e_s.append(prueba_est_sib_prom_m[1])

prueba_est_sib_prom_e= mannwhitneyu(df_estertor.iloc[:,3],df_sibilancia.iloc[:,3])
statistic_e_s.append(prueba_est_sib_prom_e[0])
pvalue_e_s.append(prueba_est_sib_prom_e[1])

dic_e_s={"Statistic":statistic_e_s, "Pvalue":pvalue_e_s}
df_e_s= pd.DataFrame(dic_e_s, index=["Varianza","Rango","Promedio móvil","Promedio espectro"])




#%%        GRÁFICAS DE DISTRIBUCIÓN DE PROBABILIDAD


# Normales
#plt.subplot(2,2,1)
#sns.distplot(df_sano["Varianza"])
#plt.title("Varianza")
#plt.subplot(2,2,2)
#sns.distplot(df_sano["Rango"])
#plt.title("Rango")
#plt.subplot(2,2,3)
#sns.distplot(df_sano["Promedio móvil"])
#plt.subplot(2,2,4)
#sns.distplot(df_sano["Promedio espectro"])

# Estertores
#plt.subplot(2,2,1)
#sns.distplot(df_estertor["Varianza"])
#plt.title("Varianza")
#plt.subplot(2,2,2)
#sns.distplot(df_estertor["Rango"])
#plt.title("Rango")
#plt.subplot(2,2,3)
#sns.distplot(df_estertor["Promedio móvil"])
#plt.subplot(2,2,4)
#sns.distplot(df_estertor["Promedio espectro"])

# Sibilancias
#plt.subplot(2,2,1)
#sns.distplot(df_sibilancia["Varianza"])
#plt.title("Varianza")
#plt.subplot(2,2,2)
#sns.distplot(df_sibilancia["Rango"])
#plt.title("Rango")
#plt.subplot(2,2,3)
#sns.distplot(df_sibilancia["Promedio móvil"])
#plt.subplot(2,2,4)
#sns.distplot(df_sibilancia["Promedio espectro"])

#%%


