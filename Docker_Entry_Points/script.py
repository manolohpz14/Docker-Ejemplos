import sys
import os
import pandas as pd

lista=sys.argv


booleano= os.environ.get("VAR", "False")

if (booleano=="True"):
    for elem in lista:
        print(elem)



datos = {
    "col1":[1,2,3],
    "col2":[1,2,3],
    "col3":[1,2,3]
}

df=pd.DataFrame(datos)

df.to_excel("archivo.xlsx", index=False)
print("arhivo subido")