import pandas as pd 

def info_mayorista():
    mayorist_data = pd.read_csv('datos.csv', sep = ';')
    mayorist_data = mayorist_data[['Producto', 'Variedad', 'Precio MAX', 'Precio AVG', 'Precio MIN']]
    return mayorist_data

def info_plazaVea():
    plaza_vea = pd.read_csv('plazaveafinal.csv', sep = ';', engine='python')
    return plaza_vea

def info_wong():
    wong = pd.read_csv('wong.csv', engine='python')
    return wong

def info_tottus():
    tottus = pd.read_csv('tottusfinal.csv', engine='python')
    return tottus




