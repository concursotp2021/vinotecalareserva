from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fp.fp import FreeProxy
import os
import requests

f = open("lista_enlaces.txt","r")
for x in f:
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(x)
    print(driver.find_element_by_xpath('//img[1]').get_attribute('src'))
    v_url = driver.find_element_by_xpath('//img[1]').get_attribute('src')

    driver.close()

f.close()    
