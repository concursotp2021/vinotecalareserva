from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fp.fp import FreeProxy
import os
import requests

f = open("lista_enlaces.txt","r")
for line in f:
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(line)
    v_url = driver.find_element_by_xpath('//img[1]').get_attribute('src')
    f2 = open ("lista_enlaces_salida.txt","a")
    #print(driver.find_element_by_xpath('//img[1]').get_attribute('src'))
    f2.write(v_url+"\n")
    f2.close
    driver.close()

f.close()
print("finish")

