#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from selenium.webdriver import ActionChains
import lxml
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import csv
from selenium.webdriver.support.ui import WebDriverWait
import time
inicio = time.time()

chrome_path = r'/usr/local/bin/chromedriver' #path from 'which chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)

urls = [
    'https://www.vademecum.es/medicamentos-a_1',
    'https://www.vademecum.es/medicamentos-b_1',
    'https://www.vademecum.es/medicamentos-c_1',
    'https://www.vademecum.es/medicamentos-d_1',
    'https://www.vademecum.es/medicamentos-e_1',
    'https://www.vademecum.es/medicamentos-f_1',
    'https://www.vademecum.es/medicamentos-g_1',
    'https://www.vademecum.es/medicamentos-h_1',
    'https://www.vademecum.es/medicamentos-i_1',
    'https://www.vademecum.es/medicamentos-j_1',
    'https://www.vademecum.es/medicamentos-k_1',
    'https://www.vademecum.es/medicamentos-l_1',
    'https://www.vademecum.es/medicamentos-m_1',
    'https://www.vademecum.es/medicamentos-n_1',
    'https://www.vademecum.es/medicamentos-o_1',
    'https://www.vademecum.es/medicamentos-p_1',
    'https://www.vademecum.es/medicamentos-q_1',
    'https://www.vademecum.es/medicamentos-r_1',
    'https://www.vademecum.es/medicamentos-s_1',
    'https://www.vademecum.es/medicamentos-t_1',
    'https://www.vademecum.es/medicamentos-u_1',
    'https://www.vademecum.es/medicamentos-v_1',
    'https://www.vademecum.es/medicamentos-w_1',
    'https://www.vademecum.es/medicamentos-x_1',
    'https://www.vademecum.es/medicamentos-y_1',
    'https://www.vademecum.es/medicamentos-z_1',
]

products=[] 
laboratory=[]
atc=[]
ipt_element=[]
ipt_final=[]
for url in urls:
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content)
    
    for block in soup.findAll('div', attrs={'class':'listColaMmi'}):
        details = driver.find_elements_by_css_selector(".listColaMmi a")
        
        for i in range(len(details)):
            x = driver.find_elements_by_css_selector(".listColaMmi a")[i]
            products.append(x.text)
            x.click()
            
            if (driver.find_elements_by_css_selector(".laboratorioTxt a") and driver.find_elements_by_css_selector(".laboratorioTxt a")[0] ):
                atc_element = driver.find_elements_by_css_selector(".laboratorioTxt a")[0].text
            else:
                atc_element = ''
            atc.append(atc_element)
            
            lab = driver.find_elements_by_xpath("//*[contains(text(), 'Laboratorio Comercializador')]")[0] if driver.find_elements_by_xpath("//*[contains(text(), 'Laboratorio Comercializador')]")[0] else '' 
            name_lab = lab.text.split(":")
            laboratory.append('-' if lab=='' else name_lab[1])
            
            prueba = driver.find_elements_by_css_selector(".panel-pub-right")
            for i in prueba:
                #print(i)
                ipts = i.find_elements_by_css_selector("b");
                for ipt in ipts:
                    if (ipt):
                        ipt_element.append(ipt.text)
            ipt_final.append(ipt_element)
            ipt_element=[]
            
            driver.get(url)

driver.close()

df = pd.DataFrame({'Medication':products, 'atc':atc , 'lab':laboratory, 'ipt':ipt_final })
df.to_csv('MostPopularDrugs.csv', index=False, encoding='utf-8-sig', sep="|", quoting=csv.QUOTE_NONE, quotechar="",  escapechar=" ")

fin = time.time()
print(fin-inicio) 
