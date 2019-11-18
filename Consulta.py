# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import os
from re import sub as Expressao

qtacoes = 21
CotacaoInicial = 1.00
valorinicial = qtacoes * CotacaoInicial

pagina = 'https://www.infomoney.com.br/cotacoes/oi-oibr3/'
#pagina = 'https://www.infomoney.com.br/cotacoes/ibovespa/'

valor = 0


while True:
	req = requests.get(pagina)
	soup = BeautifulSoup(req.text, 'html.parser')

	CotacaoAtual = soup.find_all(class_='line-info')

	CotacaoAtual = Expressao('.*">',' ', str(CotacaoAtual))
	CotacaoAtual = Expressao('.*i>','', str(CotacaoAtual))
	CotacaoAtual = Expressao('\\n','', str(CotacaoAtual))
	CotacaoAtual = Expressao(',','.', str(CotacaoAtual))
	CotacaoAtual = Expressao('  <p>(\\d+.?\\d+?.?\\d+?).*','\g<1>', str(CotacaoAtual))
	
	if CotacaoAtual == valor:
		pass
	else:
		
		valoratual = qtacoes * float(CotacaoAtual)
		valor = CotacaoAtual
	os.system('cls')
	#print(f'Capital Inicial {valorinicial}')
	print(f'Saldo Atual: {valoratual}')
	print(f'Cotação Atual: {valor}')
	
	if valorinicial < valoratual:
		resultado = valoratual-valorinicial
		print('Lucro: ' + str(resultado)[:4])
	elif valorinicial == valoratual:
		print('Sem Alteração')
	else:                             
		resultado = valorinicial-valoratual
		print('Perda: ' + str(resultado)[:4])
	
os.system('pause')
