import pandas as pd 

def info_mayosrista():
    mayorist_data = pd.read_csv('datos.csv', sep = ';')
    mayorist_data = mayorist_data[['Producto', 'Variedad', 'Precio MAX', 'Precio AVG', 'Precio MIN']]

def info_plazaVea():
    plaza_vea = pd.read_csv('plazavea.csv')
    name = plaza_vea['name']
    precio = plaza_vea['entero'] + plaza_vea['decimal']
    plaza_vea = pd.concat([name, precio], axis=1, ignore_index=True)

def info_wong():
    wong = pd.read_csv('wong.csv', engine='python')
    



