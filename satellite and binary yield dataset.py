# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 20:10:05 2022

@author: PlantPhisiology
"""
### GIT HUB REPOSIORY ####
### https://github.com/plantphysiology/Take-a-peek-of-data-set  ###
### Take a peak of Sentinel satellite bands values and binary grape yield five years data sets
import numpy as np
import pandas as pd
from scipy.stats import shapiro

###############################################################################
print("Take a peak of Sentinel satellite bands values and binary grape yield five years data sets")
############################### 2016 with B9 band #########################
df = pd.read_excel("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_con_B9_2016.xlsx")
df = df[['B8A','B04','B03','B02','B09','Yieldlevel']]
etiqueta = df[['Yieldlevel']]
df.fillna(-99999, inplace=True)
atributos = df[['B8A','B04','B03','B02','B09']]
x2016 = df[['B8A','B04','B03','B02','B09']].values
y2016 = df[['Yieldlevel']].values
feature_names = ['B8A','B04','B03','B02','B09']

print("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_con_B9_2016.xlsx")
print(feature_names)
print("Mean", np.mean(df))
print("Grape yield Normal Distribution", shapiro(y2016))
print("▄█▄ ▄█▄ ▄█▄")

############################### 2016 without B9 band #########################
df = pd.read_excel("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_sin_B9_2016.xlsx")
df = df[['B8A','B04','B03','B02','Yieldlevel']]
etiqueta = df[['Yieldlevel']]
df.fillna(-99999, inplace=True)
atributos = df[['B8A','B04','B03','B02']]
x2016 = df[['B8A','B04','B03','B02']].values
y2016 = df[['Yieldlevel']].values
feature_names = ['B8A','B04','B03','B02']

print("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_sin_B9_2016.xlsx")
print(feature_names)
print("Mean", np.mean(df))
print("Grape yield Normal Distribution", shapiro(y2016))
print("▄█▄ ▄█▄ ▄█▄")
print(" ")

############################## 2017 with B9 band #########################
df = pd.read_excel("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_con_B9_2017.xlsx")
df = df[['B8A','B04','B03','B02','B09','Yieldlevel']]
etiqueta = df[['Yieldlevel']]
df.fillna(-99999, inplace=True)
atributos = df[['B8A','B04','B03','B02','B09']]
x2017 = df[['B8A','B04','B03','B02','B09']].values
y2017 = df[['Yieldlevel']].values
feature_names = ['B8A','B04','B03','B02','B09']

print("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_con_B9_2017.xlsx")
print(feature_names)
print("Mean", np.mean(df))
print("Grape yield Normal Distribution", shapiro(y2017))
print("▄█▄ ▄█▄ ▄█▄")

############################## 2017 without B9 band #########################
df = pd.read_excel("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_sin_B9_2017.xlsx")
df = df[['B8A','B04','B03','B02','Yieldlevel']]
etiqueta = df[['Yieldlevel']]
df.fillna(-99999, inplace=True)
atributos = df[['B8A','B04','B03','B02']]
x2017 = df[['B8A','B04','B03','B02']].values
y2016 = df[['Yieldlevel']].values
feature_names = ['B8A','B04','B03','B02']

print("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_sin_B9_2017.xlsx")
print(feature_names)
print("Mean", np.mean(df))
print("Grape yield Normal Distribution", shapiro(y2017))
print("▄█▄ ▄█▄ ▄█▄")
print(" ")

############################### 2018 with B9 band #########################
df = pd.read_excel("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_con_B9_2018.xlsx")
df = df[['B8A','B04','B03','B02','B09','Yieldlevel']]
etiqueta = df[['Yieldlevel']]
df.fillna(-99999, inplace=True)
atributos = df[['B8A','B04','B03','B02','B09']]
x2018 = df[['B8A','B04','B03','B02','B09']].values
y2018 = df[['Yieldlevel']].values
feature_names = ['B8A','B04','B03','B02','B09']

print("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_con_B9_2018.xlsx")
print(feature_names)
print("Mean", np.mean(df))
print("Grape yield Normal Distribution", shapiro(y2018))
print("▄█▄ ▄█▄ ▄█▄")

############################### 2018 without B9 band #########################
df = pd.read_excel("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_sin_B9_2018.xlsx")
df = df[['B8A','B04','B03','B02','Yieldlevel']]
etiqueta = df[['Yieldlevel']]
df.fillna(-99999, inplace=True)
atributos = df[['B8A','B04','B03','B02']]
x2018 = df[['B8A','B04','B03','B02']].values
y2018 = df[['Yieldlevel']].values
feature_names = ['B8A','B04','B03','B02']

print("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_sin_B9_2018.xlsx")
print(feature_names)
print("Mean", np.mean(df))
print("Grape yield Normal Distribution", shapiro(y2018))
print("▄█▄ ▄█▄ ▄█▄")
print(" ")

############################### 2019 with B9 band #########################
df = pd.read_excel("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_con_B9_2019.xlsx")
df = df[['B8A','B04','B03','B02','B09','Yieldlevel']]
etiqueta = df[['Yieldlevel']]
df.fillna(-99999, inplace=True)
atributos = df[['B8A','B04','B03','B02','B09']]
x2019 = df[['B8A','B04','B03','B02','B09']].values
y2019 = df[['Yieldlevel']].values
feature_names = ['B8A','B04','B03','B02','B09']

print("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_con_B9_2019.xlsx")
print(feature_names)
print("Mean", np.mean(df))
print("Grape yield Normal Distribution", shapiro(y2019))
print("▄█▄ ▄█▄ ▄█▄")

############################### 2019 without B9 band #########################
df = pd.read_excel("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_sin_B9_2019.xlsx")
df = df[['B8A','B04','B03','B02','Yieldlevel']]
etiqueta = df[['Yieldlevel']]
df.fillna(-99999, inplace=True)
atributos = df[['B8A','B04','B03','B02']]
x2019 = df[['B8A','B04','B03','B02']].values
y2019 = df[['Yieldlevel']].values
feature_names = ['B8A','B04','B03','B02']

print("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_sin_B9_2019.xlsx")
print(feature_names)
print("Mean", np.mean(df))
print("Grape yield Normal Distribution", shapiro(y2019))
print("▄█▄ ▄█▄ ▄█▄")
print(" ")






############################### 2020 with B9 band #########################
df = pd.read_excel("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_con_B9_2020.xlsx")
df = df[['B8A','B04','B03','B02','B09','Yieldlevel']]
etiqueta = df[['Yieldlevel']]
df.fillna(-99999, inplace=True)
atributos = df[['B8A','B04','B03','B02','B09']]
x2020 = df[['B8A','B04','B03','B02','B09']].values
y2020 = df[['Yieldlevel']].values
feature_names = ['B8A','B04','B03','B02','B09']

print("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_con_B9_2020.xlsx")
print(feature_names)
print("Mean", np.mean(df))
print("Grape yield Normal Distribution", shapiro(y2020))
print("▄█▄ ▄█▄ ▄█▄")

############################### 2020 without B9 band #########################
df = pd.read_excel("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_sin_B9_2020.xlsx")
df = df[['B8A','B04','B03','B02','Yieldlevel']]
etiqueta = df[['Yieldlevel']]
df.fillna(-99999, inplace=True)
atributos = df[['B8A','B04','B03','B02']]
x2020 = df[['B8A','B04','B03','B02']].values
y2020 = df[['Yieldlevel']].values
feature_names = ['B8A','B04','B03','B02']

print("C:/Users/EMA\.spyder-py3/bandas01/bandas_moda_sin_B9_2020.xlsx")
print(feature_names)
print("Mean", np.mean(df))
print("Grape yield Normal Distribution", shapiro(y2020))
print("▄█▄ ▄█▄ ▄█▄")
print(" ")




