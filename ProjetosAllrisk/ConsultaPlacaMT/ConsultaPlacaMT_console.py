# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import sys
import re
import codecs
from optparse import OptionParser
import os.path

import csv
import requests
import os

options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--start-maximized") 
options.add_argument('-headless')
#options.binary_location = ""

driver = webdriver.Chrome('chromedriver.exe',options=options)
TipoPesquisa = 'P'
PlacaChassi = ''

def Pesquisar():	  
    driver.get('https://portal.sesp.mt.gov.br/portaldaseguranca/pages/veiculo/consultaVeiculoRoubado.seam');
    time.sleep(0.5) # Let the user actually see something!
    
    if (TipoPesquisa.upper()=='P'):
        driver.find_element_by_css_selector("#consultaVeiculo\:busca\:veiculoOpcao [value='PLACA']").click()
        time.sleep(0.5)
        oplaca = driver.find_element_by_css_selector("#consultaVeiculo\\:j_id46\\:placa")
        oplaca.send_keys(PlacaChassi)
        driver.find_element_by_css_selector("#consultaVeiculo\:consultar").click()
    else:
        #driver.find_element_by_css_selector("#consultaVeiculo\:busca\:veiculoOpcao [value='PLACA']").click()
        #time.sleep(1)
        ochassi = driver.find_element_by_css_selector("#consultaVeiculo\:chassi\:descricao")
        ochassi.send_keys(PlacaChassi)
        driver.find_element_by_css_selector("#consultaVeiculo\:consultar").click()
    
    strMarcaModelo = ''
    strPlaca = ''
    strAnos = ''
    strCor = ''
    strChassi = ''
    
    time.sleep(0.5)
    
    pattern = re.compile('\n', re.MULTILINE)
    
    # marca/modelo
    try:
       elemento = driver.find_element_by_xpath('//*[@id="situacao-veiculo"]/div[2]/ul/li[2]')
       strMarcaModelo = elemento.get_attribute("innerText")
       strMarcaModelo = pattern.sub('', strMarcaModelo)    
    
    except:
       pass
    # placa
    try:
       elemento = driver.find_element_by_xpath('//*[@id="situacao-veiculo"]/div[2]/ul/li[3]')
       strPlaca = elemento.get_attribute("innerText")
       strPlaca = pattern.sub('', strPlaca)    
    except:
       pass
    # anos
    try:
       elemento = driver.find_element_by_xpath('//*[@id="situacao-veiculo"]/div[2]/ul/li[4]')
       strAnos = elemento.get_attribute("innerText")
       strAnos = pattern.sub('', strAnos)    
    except:
       pass
    # cor
    try:
       elemento = driver.find_element_by_xpath('//*[@id="situacao-veiculo"]/div[2]/ul/li[5]')
       strCor = elemento.get_attribute("innerText")
       strCor = pattern.sub('', strCor)    
    except:
       pass
    # chassi
    try:
       elemento = driver.find_element_by_xpath('//*[@id="situacao-veiculo"]/div[2]/ul/li[6]')
       strChassi = elemento.get_attribute("innerText")
       strChassi = pattern.sub('', strChassi)    
    except:
       pass
    
    print(strPlaca)
    print(strMarcaModelo)
    print(strAnos)
    print(strCor)
    print(strChassi)
    print('')

#---- ENTRADA DE DADOS PELO CONSOLE

loop = 's'

while loop == 's':

      TipoPesquisa = input('Informe o Tipo de Pesquisa: C-chassi, P-placa ou S-para sair:') or 'P'

      if (TipoPesquisa=='S'):
          loop = 'N'
      
      elif (TipoPesquisa.upper()=='P' or  TipoPesquisa.upper()=='C'):
      
         if (TipoPesquisa.upper()=='P'):
             PlacaChassi = input('Informe a Placa do Veiculo:')
         else:
             PlacaChassi = input('Informe o Chassi do Veiculo:')

         Pesquisar()
      
      else:
         print("Tipo de Pesquisa invalido. Informe o Tipo de Pesquisa: C-chassi ou P-placa.")

driver.quit()

# fim da programa

