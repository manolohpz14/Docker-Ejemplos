# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 23:51:52 2024

@author: manolo
"""

import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs
import re
import datetime
import os
import re


url = "https://elpais.com/deportes/resultados/futbol/primera/jornada/"

# --Realizamos la solicitud HTTP--
response = rq.get(url)

# ---Verificamos si la respuesta fue exitosa---
if response.status_code == 200:
    # ----Procesamos el HTML con BeautifulSoup---
    soup = bs(response.text, "html.parser")
    
    # ----Ahora seleccionamos los elementos que contienen los resultados---
    lista = [re.sub(r"\s+", " ", x.text.replace("\n", "")) for x in soup.select(".list-resultado")] #\evitar secuencia de escpe #replace("/s+g/"," ") en Js sería así
    
    # ---Mostramos los resultados (esto es solo un ejemplo, ajusta según el HTML)---
    for resultado in lista:
        print(resultado)





print(lista)


obj={}
obj["Resultados"]=lista
obj["Fecha"]=[datetime.datetime.now().strftime("%d/%m/%Y") for i in range(0, len(lista))]
dg=pd.DataFrame(obj)


var_entorno= os.environ.get("entorno", False)
if var_entorno==False:
    archivo_excel=r"C:/Users/manolo/volumen_compartido/mi_excel.xlsx"
else:
    archivo_excel="/volumen_compartido/mi_excel.xlsx"





if os.path.exists(archivo_excel):
    #-----Leer las hojas del archivo existente-----
    df_resultados = pd.read_excel(archivo_excel, sheet_name='resultados')
    df_noticias = pd.read_excel(archivo_excel, sheet_name='noticias')
    
    df_resultados['Fecha'] = df_resultados['Fecha'].astype('datetime64[s]')
    dg['Fecha'] = dg['Fecha'].astype('datetime64[s]')
    
    #----Ordenar los DataFrames por la columna de 'Fecha', de más antigua a más reciente----
    df_resultados = df_resultados.sort_values(by=['Fecha'])
    dg = dg.sort_values(by='Fecha')
    
    #---Obtener la última fecha de cada DataFrame después de ordenar----
    ultima_fecha_resultados = df_resultados['Fecha'].iloc[-1] if not df_resultados.empty else None
    ultima_fecha_dg = dg['Fecha'].iloc[-1] if not dg.empty else None

    if ultima_fecha_resultados != ultima_fecha_dg:
        df_resultados = pd.concat([df_resultados, dg], ignore_index=True)
    
    #----Escribir ambos DataFrames al mismo archivo Excel----
        with pd.ExcelWriter(archivo_excel, engine='openpyxl') as writer:
            df_resultados.to_excel(writer, sheet_name='resultados', index=False)
            df_noticias.to_excel(writer, sheet_name='noticias', index=False)

else:
    #----Si el archivo no existe, crear un nuevo archivo con dos hojas----
    with pd.ExcelWriter(archivo_excel, engine='openpyxl') as writer:
        dg.to_excel(writer, sheet_name='resultados', index=False)
        pd.DataFrame({"Noticias":[], "Fecha":[]}).to_excel(writer, sheet_name='noticias', index=False)
        
        
        

"""with open(archivo_txt, 'a') as archivo: #w(sobreescribe),a,r 
    archivo.write("\n--- Nueva entrada ---\n")  # Separador claro entre entradas
    for noticia in noticias:
        archivo.write(f"Título: {noticia['titulo']}\n") #tenemos read, readline(lee solo una linea), readlines()-> [devuelve lista de lienas],..
        archivo.write(f"Fecha: {noticia['fecha']}\n")
        archivo.write("-" * 20 + "\n")"""












