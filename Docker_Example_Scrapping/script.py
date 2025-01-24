#*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:37:44 2022

@author: Juan Manuel Hernández Pérez
"""

import zipfile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import subprocess
import pandas as pd

import requests
import zipfile
import os
import subprocess

# Obtener la versión de Google Chrome instalada en el sistema
import requests
import zipfile
import os
import subprocess
import tempfile

def get_chrome_version(sistema_operativo="linux"):
    if sistema_operativo=="linux":
        version_output=subprocess.check_output(['google-chrome', '--version'], stderr=subprocess.STDOUT)
        version_str=version_output.decode('utf-8').strip()
        version=version_str.split()[2]
        return version
    else:
        version_output=subprocess.check_output(['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon', '/v', 'version'], stderr=subprocess.STDOUT)
        version=version_output.decode('utf-8').strip().split()[-1]
        return version

def get_chromedriver_url(chrome_version,sistema_operativo):
    base_url = "https://storage.googleapis.com/chrome-for-testing-public/"
    if sistema_operativo=="linux":
        return f"{base_url}{chrome_version}/linux64/chromedriver-linux64.zip"
    else:
        return f"{base_url}{chrome_version}/win64/chromedriver-win64.zip"

def download_and_extract_chromedriver(url):
    zip_file_path = "chromedriver.zip"
    extract_folder = "chromedriver"
    response = requests.get(url)
    with open(zip_file_path, 'wb') as file:
        file.write(response.content)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)
    os.remove(zip_file_path)
    print(f"Chromedriver descomprimido en la carpeta '{extract_folder}'",flush=True)


sistema_operativo = os.getenv("OS", "windows")
chrome_version = get_chrome_version(sistema_operativo)
if chrome_version:
    print(f"Versión de Google Chrome: {chrome_version}",flush=True)
    chromedriver_url = get_chromedriver_url(chrome_version,sistema_operativo)
    download_and_extract_chromedriver(chromedriver_url)
else:
    print("No se pudo obtener la versión de Google Chrome.",flush=True)




if sistema_operativo=="linux":
    chromedriver_path="/chromedriver/chromedriver-linux64/chromedriver"

else:
    chromedriver_path="./chromedriver/chromedriver-win64/chromedriver.exe"

if os.path.isfile(chromedriver_path):
    print(f"Chromedriver encontrado en: {chromedriver_path}")
    os.chmod(chromedriver_path, 0o755)
else:
    print(f"Chromedriver NO encontrado en: {chromedriver_path}",flush=True)
usuario=os.getenv("user", "---")
contraseña=os.getenv("contra", "---")
# Guardar la contraseña en un archivo de texto
# Leer la contraseña desde el archivo de textodo
# with open("password.txt", "r") as file:
#     contraseña = file.read().strip()

chrome_options = Options()

if sistema_operativo=="linux":
    chrome_options.add_argument("--headless")  # Modo headless (sin interfaz gráfica)
    chrome_options.add_argument("--no-sandbox")
    print("añado opciones en linux",flush=True)
    chrome_options.add_argument("--disable-dev-shm-usage") # Si deseas que Chrome funcione en modo headless (sin interfaz gráfica)

# Crear la instancia del servicio de ChromeDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.instagram.com/")

try:
   permitir_cookies = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[tabindex='0']"))).click()
except:
    print("no hay cookies que quitar",flush=True)
time.sleep(2.5)



#------------------------Hacemos el input del usuario y contraseña--------------------------
username=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='username']"))) #cuando nos sale tipo input en inspeccionar
#<input aria-label="Teléfono, usuario o correo electrónico" aria-required="true" autocapitalize="off" autocorrect="off" maxlength="75" name="username" type="text" class="_aa4b _add6 _ac4d" value="lolohpz">
password=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='password']")))




#-------------------------Limpiamos lo que hubiese y lo enviamos---------------------
username.clear()
password.clear()
username.send_keys(usuario)
password.send_keys(contraseña)




#-------------------Nos saltamos el mensaje de las cookies y nos loguemos. Tampoco guardamos sesión


try:
   log_in = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[class=' _acan _acap _acas _aj1- _ap30']"))).click()
except:
   try:
      log_in = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']"))).click()
   except:
      try:
          log_in = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Entrar')]"))).click()
      except:
          print("no se ha conseguido darle al botón de iniciar sesión",flush=True)
           
#<button class="_acan _acap _acas" type="submit"><div class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p _abcm">Entrar</div></button>
#<div class="_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p _abcm">Entrar</div>

print("Esperamos a que el usuario meta el código",flush=True)
time.sleep(5)
print("Sesion iniciada",flush=True)


#<div class="_ac8f"><div class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc xcdnw81 x1i0vuye xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37" role="button" tabindex="0">Ahora no</div></div>

#------------No guardamos sesión ni tampoco queremos que instagram envie notificaciones (son un poco pesados)------------

try:
   no_guardar_sesion = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='x78zum5 xdt5ytf x1e56ztr']"))).click() #cuando nos sale tipo button en inspeccionar
except:
    print("no hace falta apretar el boton de no guardar sesión",flush=True)
#<button class="_acan _acao _acas" type="button">Ahora no</button>
time.sleep(1)

try:
   no_notificaciones = WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,"//button[@class='_a9-- _ap36 _a9_1']"))).click()
except:
    print("no hace falta quitar notificaciones",flush=True)
#<button class="_a9-- _a9_1" tabindex="0">Ahora no</button>
time.sleep(3)



#-------------------Pinchamos en nuestro perfil-------------------------------------------------
try:
    pinchar_perfil = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/" +usuario+ "/']"))).click()
except:
    print("no se ha podido pinchar en el perfil",flush=True)
    driver.get("https://www.instagram.com/"+usuario)
#<a class="x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _aak1 _a6hd" href="/lolohpz/" role="link" tabindex="0">lolohpz</a>
time.sleep(2)




#------------------------Miramos nuestro numero de seguidores y seguidos----------------------
try:
   numero_seguidores=driver.find_elements(By.XPATH,"//span[@class='x5n08af x1s688f']")[1].text
   print("numero_seguidores primer intento",flush=True)
   print(numero_seguidores,flush=True)
except:
    print("numero_seguidores fallo primer intento",flush=True)
    try:
       numero_seguidores=driver.find_elements(By.XPATH,"//div[@class='_aacl _aacp _aacu _aacx _aad6 _aade']")[1].text.split(" ")[0]
       print("numero_seguidores segundo intento",flush=True)
    except:
       print("numero_seguidores fallado al segundo intento",flush=True)
#<div class="_aacl _aacp _aacu _aacx _aad6 _aade"><span class="_ac2a" title="598">598</span> seguidores</div>



try:
   numero_seguidos=driver.find_elements(By.XPATH,"//span[@class='x5n08af x1s688f']")[2].text
   print("numero_seguidos al primer intento",flush=True)
   print(numero_seguidos)
except:
    print("numero_seguidos fallo primer intento",flush=True)
    try:
       numero_seguidos=driver.find_elements(By.XPATH,"//div[@class='_aacl _aacp _aacu _aacx _aad6 _aade']")[2].text.split(" ")[0]
       print("numero_seguidos al segundo intento",flush=True)
    except:
       print("numero_seguidos fallo al segundo intento",flush=True)
#<div class="_aacl _aacp _aacu _aacx _aad6 _aade"><span class="_ac2a" title="598">598</span> seguidores</div>







#-------------------------Número de scrolls necesarios---------------------------------------------------------
#miramos el número de scrolls que tendremos que hacer para hallar todos los seguidores y seguidos. Cada scroll nos da 12 cuentas
scrolls_seguidores=int(int(numero_seguidores)/12)+2
scrolls_seguidos=int(int(numero_seguidos)/12)+2
print(scrolls_seguidores,flush=True)
print(scrolls_seguidos,flush=True)
time.sleep(3)

 
#----------Empezamos con los seguidores---------------------------------
pinchar_seguis = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/"+usuario+"/following/']"))).click()
#<div class="_aacl _aacp _aacu _aacx _aad6 _aade"><span class="_ac2a" title="598">598</span> seguidores</div>
time.sleep(5)

element = driver.find_element(By.XPATH,"//div[@class='xyi19xy x1ccrb07 xtf3nb5 x1pc53ja x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6']")


time.sleep(3)
lista_seguidos=[]
while (len(lista_seguidos)<int(numero_seguidos)-5):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element)
    seguidores=driver.find_elements(By.XPATH,"//div[@class='x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3']")
    for seguidor in seguidores:
           lista_seguidos.append((seguidor.text).split("\n")[0]) #hacemos un split ya que en las cuentas de verificados aparece de esta forma: nombre\nVerificado. El atributo tipo text nos transforma de tipo selenium a texto.
    lista_seguidos=set(lista_seguidos)
    lista_seguidos=list(lista_seguidos)
    print(len(lista_seguidos),flush=True)
    time.sleep(1)
    
time.sleep(3)  



time.sleep(5)       
       
#---------Cerramos pestaña de seguidores----------------------------------
try:       
    cerrar_pestana = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[role='dialog'] ._abl-"))).click()
#<button class="_abl-" type="button"><div class="_abm0"><svg aria-label="Cerrar" class="_ab6-" color="#262626" fill="#262626" height="18" role="img" viewBox="0 0 24 24" width="18"><polyline fill="none" points="20.643 3.357 12 12 3.353 20.647" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3"></polyline><line fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" x1="20.649" x2="3.354" y1="20.649" y2="3.354"></line></svg></div></button>       
    time.sleep(5)   
except:
    try:
        pinchar_perfil = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/" +usuario+ "/']"))).click()
    except:
        print("no se ha podido pinchar en el perfil",flush=True)
        driver.get("https://www.instagram.com/"+usuario)
        time.sleep(5)


#----------Seguimos con los seguidos---------------------------------
#<a class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _alvs _a6hd" href="/lolohpz/followers/" role="link" tabindex="0"><span class="_ac2a" title="653"><span class="html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs">653</span></span> seguidores</a>

pinchar_seguidores = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/"+usuario+"/followers/']"))).click()
#<div class="_aacl _aacp _aacu _aacx _aad6 _aade"><span class="_ac2a" title="598">598</span> seguidores</div>

time.sleep(5)
element = driver.find_element(By.XPATH,"//div[@class='xyi19xy x1ccrb07 xtf3nb5 x1pc53ja x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6']")

time.sleep(3)
lista_seguidores=[]
while (len(lista_seguidores)<int(numero_seguidores)-5):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element)
    seguidores=driver.find_elements(By.XPATH,"//div[@class='x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3']")
    for seguidor in seguidores:
           lista_seguidores.append((seguidor.text).split("\n")[0]) #hacemos un split ya que en las cuentas de verificados aparece de esta forma: nombre\nVerificado. El atributo tipo text nos transforma de tipo selenium a texto.
    lista_seguidores=set(lista_seguidores)
    lista_seguidores=list(lista_seguidores)
    print(len(lista_seguidores),flush=True)
    time.sleep(1)
    
time.sleep(5) 
    
 
    

       
#vamos a calcular cuantos de las personas que seguimos nos siguen de vuelta:

no_follow_back=[]
for seguido in lista_seguidos:
   if seguido not in lista_seguidores:
       no_follow_back.append(seguido)
       
print(no_follow_back,flush=True)

max_length = max(len(lista_seguidores), len(lista_seguidos), len(no_follow_back))

# Rellenar las listas con None o NaN para que todas tengan la misma longitud
lista_seguidores += [None] * (max_length - len(lista_seguidores))
lista_seguidos += [None] * (max_length - len(lista_seguidos))
no_follow_back += [None] * (max_length - len(no_follow_back))

data = {
   "Seguidores": lista_seguidores,
   "Seguidos": lista_seguidos,
   "No te siguen de vuelta": no_follow_back
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel
df.to_excel("seguidores_seguidos.xlsx", index=False)



#Hasta ahora hemos visto que podemos encontrar a las personas que no nos siguen y meterlas en una lista. Otra funcionalidad curiosa que instagram no te deja ver, es comparar los seguidores de dos cuentas a las que tu ya sigues:

