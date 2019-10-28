# -*- coding: utf-8 -*-
# Versao: 0.1
# Desenvolvido por Michel Anderson
# AllRisk Soluções  © 2019

import os
import sys
import re
import subprocess

def ContarPaginas(NomeArquivo):  
	# NOTA: Não esta funcionando 100% Ainda
	rxContarPaginas = re.compile(r"/Type\s*/Page([^s]|$)", re.MULTILINE|re.DOTALL)
	Dados = open(NomeArquivo,"r", encoding = "ISO-8859-1").read()
	return len(rxContarPaginas.findall(Dados))

def PegarTexto(LocalArquivo, page_nums = True):
	if os.path.isabs(LocalArquivo):
		TodoLocalArquivo = LocalArquivo
	else:
		cd = os.getcwd()
		TodoLocalArquivo = os.path.join(cd, LocalArquivo)

	text = ''
	actual_count = 0

	# If page numbers are to be inserted
	if page_nums:
		# Count number of pages
		num = ContarPaginas(TodoLocalArquivo)
		# Accounts for errors occuring in ContarPaginas function
		if num == 0:
			num = 100
		for i in range(num):
			actual = i + 1
			# Calls xpdf 
			subprocess.call(['Modulos/pdftotext', '-f', str(actual),'-l', str(actual), TodoLocalArquivo])
			# Opens file saved to disk 
			saved_file = TodoLocalArquivo.replace('.pdf','.txt')
			file = open(saved_file,'r', encoding = "ISO-8859-1")
			t = file.read()
			# If the page is blank, it is not a real page
			if t == '':
				continue
			else:
				actual_count += 1
			# Insere o texto no arquivo
			text += '{}'.format(t)
			file.close()
	else:
		# Para desenvolver
		pass

	# Remove file saved to disk
	os.remove(saved_file)

	return text, actual_count
	
def ExtrairImagens(LocalArquivo):
	if os.path.isabs(LocalArquivo):
		TodoLocalArquivo = LocalArquivo
	else:
		cd = os.getcwd()
		TodoLocalArquivo = os.path.join(cd, LocalArquivo)
	subprocess.call('Modulos\\pdfimages.exe -j {} Resultado/Imagens/Foto'.format(TodoLocalArquivo))        








	
	
