from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fp.fp import FreeProxy
import os
from slugify import slugify
import requests
import os
from urllib.parse import urlparse
import urllib.request

f = open("lista_enlaces.txt","r")
i = 0
for line in f:
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(line)
    v_url = driver.find_element_by_xpath('//img[1]').get_attribute('src')
    v_filename = urlparse(line)
    v_filename = os.path.basename(v_filename.path)
    v_filename = "escudo_ciudad_"+str(slugify(v_filename))+".png"
    urllib.request.urlretrieve(v_url, "/home/pi/Desktop/"+v_filename)
    f2 = open ("lista_enlaces_salida.txt","a")
    #print(driver.find_element_by_xpath('//img[1]').get_attribute('src'))
    v_line = line[:-1]
    f2.write(v_line+";;"+v_url+";;"+v_filename+"\n")
    f2.close
    driver.close()
    i = i +1
f.close()
print("finish")
