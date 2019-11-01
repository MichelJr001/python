# -*- coding: utf-8 -*-

from tkinter 				import *
from tkinter.scrolledtext 	import ScrolledText
from tkinter 				import messagebox

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import sys
import re
import codecs
import threading
import json


class Consulta_GUI():
	def __init__(self,janela):
		
		def sair():
			driver.quit()
			self.janela.destroy()

		self.janela = janela
		self.menubar = Menu(self.janela)
		self.janela.config(menu=self.menubar)
		
		
		self.Menu_1 = Menu(self.menubar)
		self.Menu_2 = Menu(self.menubar)
		self.Menu_3 = Menu(self.menubar)
		
		self.menubar.add_cascade(label='Opcões', menu=self.Menu_1)
		self.menubar.add_cascade(label='Ajuda', menu=self.Menu_3)
		
		self.Menu_1.add_command(label="Sair", command=sair),
		
		self.cancelou = BooleanVar()
		self.cancelou.set(False)
		self.tipo = IntVar()
		self.tipo.set(1)
		
		def mudartipo(x):
			self.tipo.set(x)

		self.r1 = Radiobutton(self.janela,text="Placa ",value=1,variable=self.tipo, command=lambda : mudartipo(1)).place(x=65,y=10,width=70, height=25)
		self.r2 = Radiobutton(self.janela,text="Chassi",value=2,variable=self.tipo, command=lambda : mudartipo(2)).place(x=140,y=10,width=70, height=25)
		self.LabelDados = Label(self.janela,text='Dados:',fg="#000").place(x=10,y=10,width=50, height=25)
		self.Entrada_Dados = ScrolledText(self.janela, fg="#000")
		self.Entrada_Dados.place(x=10,y=36,width=630, height=190)
		self.Saida_Dados = ScrolledText(self.janela, fg="#000", wrap=NONE)
		self.xbar = Scrollbar(orient='horizontal', command=self.Saida_Dados.xview )
		self.LabelResultado = Label(self.janela,text='Resultado da Pesquisa:',fg="#000").place(x=10,y=225,width=120, height=25)
		self.Saida_Dados.place(x=10,y=252,width=780, height=237)
		self.Saida_Dados.configure(xscrollcommand=self.xbar.set)
		self.xbar.place(x=10, y=490, width=780, height=15)
		self.Btn_Consultar = Button(self.janela, text="Processar",bg='#228B22',fg='#fff', command=self.Atualizar).place(x=650,y=40,width=120, height=25)
		self.Btn_Cancelar  = Button(self.janela, text="Cancelar" ,bg='red',fg='#fff', command=self.Cancelar).place(x=650,y=75,width=120, height=25)
		self.Btn_LimparDados = Button(self.janela, text="Limpar Dados", bg='blue',fg='#fff', command=self.LimparDados).place(x=650,y=110,width=120, height=25)
		self.Btn_LimparResultado = Button(self.janela, bg='#B0C4DE',fg='#fff',text="Limpar Resultado", command=self.LimparResultado).place(x=650,y=145,width=120, height=25)
		self.Btn_LimparTudo = Button(self.janela, bg='yellow',fg='black',text="Limpar Tudo", command=self.LimparTudo).place(x=650,y=180,width=120, height=25)

		self.BarraStatus = Label(self.janela,text='Informe a Placa ou chassi...',fg="#000")
		self.BarraStatus.place(x=10,y=510, height=15)
		self.BarraStatusVersao = Label(self.janela,text='versão: ' + versao + ' - ' + dataversao,fg="#000")
		self.BarraStatusVersao.place(x=650,y=510,height=15)

		self.PlacaChassi = ''
		
		janela.mainloop()

	def LimparDados(self):
		self.Entrada_Dados.delete('1.0',END)
	
	def LimparResultado(self):
		self.Saida_Dados.delete('1.0',END)

	def LimparTudo(self):
		self.Entrada_Dados.delete('1.0',END)
		self.Saida_Dados.delete('1.0',END)

	def Cancelar(self):
		self.cancelou.set(True)
		
	def Pesquisar(self):
		driver.get('https://portal.sesp.mt.gov.br/portaldaseguranca/pages/veiculo/consultaVeiculoRoubado.seam');
		#time.sleep(0.5) # Let the user actually see something!
		if (self.tipo.get() == 1):
			driver.find_element_by_css_selector("#consultaVeiculo\:busca\:veiculoOpcao [value='PLACA']").click()
			time.sleep(0.1)
			oplaca = driver.find_element_by_css_selector("#consultaVeiculo\\:j_id46\\:placa")
			oplaca.send_keys(self.PlacaChassi)
		else:
			ochassi = driver.find_element_by_css_selector("#consultaVeiculo\:chassi\:descricao")
			ochassi.send_keys(self.PlacaChassi)
	
		driver.find_element_by_css_selector("#consultaVeiculo\:consultar").click()
		
		strMarcaModelo = ''
		strPlaca = ''
		strAnos = ''
		strCor = ''
		strChassi = ''
		strMensagem = ''
		time.sleep(0.5)
		
		# marca/modelo
		try:
			elemento = driver.find_element_by_xpath('//*[@id="situacao-veiculo"]/div[2]/ul/li[2]')
			strMarcaModelo = elemento.get_attribute("innerText")
			pattern = re.compile('\n', re.MULTILINE)
			strMarcaModelo = pattern.sub('', strMarcaModelo)
			pattern = re.compile('Marca\/Modelo:', re.MULTILINE)
			strMarcaModelo = pattern.sub('', strMarcaModelo)
			
		except:
			pass
		# placa
		try:
			elemento = driver.find_element_by_xpath('//*[@id="situacao-veiculo"]/div[2]/ul/li[3]')
			strPlaca = elemento.get_attribute("innerText")
			pattern = re.compile('\n', re.MULTILINE)
			strPlaca = pattern.sub('', strPlaca)    
			pattern = re.compile('Placa:', re.MULTILINE)
			strPlaca = pattern.sub('', strPlaca)
		except:
			pass
		# anos
		try:
			elemento = driver.find_element_by_xpath('//*[@id="situacao-veiculo"]/div[2]/ul/li[4]')
			strAnos = elemento.get_attribute("innerText")
			pattern = re.compile('\n', re.MULTILINE)
			strAnos = pattern.sub('', strAnos)
			pattern = re.compile('Ano:', re.MULTILINE)
			strAnos = pattern.sub('', strAnos)
			pattern = re.compile(' \/ ', re.MULTILINE)
			strAnos = pattern.sub('\t', strAnos)
			
		except:
			pass
		# cor
		try:
			elemento = driver.find_element_by_xpath('//*[@id="situacao-veiculo"]/div[2]/ul/li[5]')
			strCor = elemento.get_attribute("innerText")
			pattern = re.compile('\n', re.MULTILINE)
			strCor = pattern.sub('', strCor)
			pattern = re.compile('Cor:', re.MULTILINE)
			strCor = pattern.sub('', strCor)
			
		except:
			pass
		# chassi
		try:
			elemento = driver.find_element_by_xpath('//*[@id="situacao-veiculo"]/div[2]/ul/li[6]')
			strChassi = elemento.get_attribute("innerText")
			pattern = re.compile('\n', re.MULTILINE)
			strChassi = pattern.sub('', strChassi)
			pattern = re.compile('Chassi:', re.MULTILINE)
			strChassi = pattern.sub('', strChassi)
			
		except:
			pass
	
		# REGISTRO NAO ENCONTRADO
		try:
			elemento = driver.find_element_by_xpath('//*[@id="gritter-item-1"]/div/div[1]/span')
			strMensagem = elemento.get_attribute("innerText")
			
		except:
			pass
	
		# REGISTRO NAO ENCONTRADO
		try:
			elemento = driver.find_element_by_xpath('//*[@id="consultaVeiculo:statusVeiculo"]')
			if strMensagem =='':
				strMensagem = 'Veículo Roubado/Furtado: ' + elemento.get_attribute("innerText")
			else:
				strMensagem = strMensagem + ' / Veículo Roubado/Furtado: ' + elemento.get_attribute("innerText")
			
		except:
			pass
		
	
		
		self.Saida_Dados.insert(END,self.PlacaChassi + '\t' + '=>\t' + strPlaca + '\t' + strMarcaModelo + '\t' + strAnos + '\t' + strCor + '\t' + strChassi + '\t' + strMensagem + '\n')
	
	def Atualizar(self):
		#self.Btn_Consultar.configure(state = 'DISABLED')
		self.cancelou.set(False)
		th=threading.Thread(target=self.Processar)
		th.start()
		#self.Btn_Consultar.configure(state = 'NORMAL')
	
	def Processar(self):
		
		dados = self.Entrada_Dados.get('1.0',END)
		valores = dados.split('\n')
		# remove itens em branco
		valores = [i for i in valores if i]
		
		try:
			i =0
			for x in valores:
				if self.cancelou.get() == True: break
				
				i += 1
				self.BarraStatus.configure(text='Processando...' + str(i) + ' de ' + str(len(valores)) + ': ' + x)
				x = x.replace(' ','')
				x = x.replace('-','')
				
				self.PlacaChassi = x
				
				try:
					self.Pesquisar()
				except:
					self.Pesquisar()

			if self.cancelou.get() == True:
				self.BarraStatus.configure(text='Cancelado pelo usuário')
			else:
				self.BarraStatus.configure(text='Informe Placa ou Chassi...')
			
		except Exception as e:
			self.BarraStatus.configure(text="Favor reprocessar")
			messagebox.showinfo("ALLRisk - Consulta Placa MT - erro", e)
		
		
	

# opções para o selenium
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--start-maximized") 
options.add_argument('-headless')

driver = webdriver.Chrome('chromedriver.exe',options=options)

# arquivo de configuração
arq_config = open("Conf.json").read()
arq_config = json.loads(arq_config)
versao = arq_config["Versao"]
dataversao = arq_config["Data Versao"]


# parametros da janela TK
janela = Tk()
janela.title('AllRisk - Consulta Placa Detran - MT')
janela.iconbitmap('allrisk-logo.ico')
janela.geometry('800x550')
janela.resizable(0, 0)
	
Consulta_GUI(janela)
driver.quit()