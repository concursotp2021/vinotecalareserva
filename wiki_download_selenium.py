from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fp.fp import FreeProxy
import os
import requests

# En este fichero ponemos las urls de donde queremos descargar las imagenes
f = open("lista_enlaces.txt","r")
for line in f:
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(line)
    v_url = driver.find_element_by_xpath('//img[1]').get_attribute('src')
    # En este fichero guardamos las urls de las imagenes que queremos
    f2 = open ("lista_enlaces_salida.txt","a")
    f2.write(v_url+"\n")
    f2.close
    driver.close()

f.close()
print("se acabo lo vailao")

