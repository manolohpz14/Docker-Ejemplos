# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 22:18:46 2024

@author: manolo
"""

import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs
import re
import datetime
import os


# En primer lugar defino la url
url="https://www.larazon.es/"
response= rq.get(url)

if response.status_code==200:
    soup=bs(response.text,"html.parser")
    
    
    
    
#Lo siguiente que podemos hacer sob selectores css o buscar por etiquetas html

lista=[x.text for x in soup.select(".article__body")]

obj={}

obj["Titulo"]=lista

obj["Fecha"]=[datetime.datetime.now().strftime("%d/%m/%Y") for i in range(0, len(lista))]



dg=pd.DataFrame(obj)


print(os.getcwd())


var_entorno= os.environ.get("entorno", False)
if __name__=="__main__":
    if var_entorno==False:
        dg.to_excel(r"C:/Users/manolo/volumen_compartido/mi_excel.xlsx")
    else:
        dg.to_excel("volumen_compartido/mi_excel.xlsx")





