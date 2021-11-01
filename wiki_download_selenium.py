from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fp.fp import FreeProxy
import os
import requests

# En este fichero ponemos las urls de donde queremos descargar las imagenes
#ejemplo: https://es.wikipedia.org/wiki/Melgar de Abajo
f = open("lista_enlaces.txt","r")
for line in f:
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(line)
    v_url = driver.find_element_by_xpath('//img[1]').get_attribute('src')
    # En este fichero guardamos las urls que vamos encontrando
    # Ejemplo: https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Escudo_de_Melgar_de_Abajo_%28Valladolid%29.svg/87px-Escudo_de_Melgar_de_Abajo_%28Valladolid%29.svg.png
    f2 = open ("lista_enlaces_salida.txt","a")
    f2.write(v_url+"\n")
    f2.close
    driver.close()

f.close()
print("se acabo lo vailao")

