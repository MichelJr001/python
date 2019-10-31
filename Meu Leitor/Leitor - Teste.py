# -*- coding: utf-8 -*-
# Versao: 0.1
# Desenvolvido por Michel Anderson
# Data Ultima alteração 30/10/2019
#  © 2019

from Configuracoes.Vizualizador import *
from re import sub as ExpressaoRegular
import os
from tkinter.scrolledtext import *
from json import *
from tkinter import *

# Le orquivo
Arquivo =  LerPDF(open('tab_veiculo_capelinha_1912_2019.pdf', 'rb'))

# Pega o Numero de paginas
Paginas = Arquivo.NumeroPaginas()
Pagina = Arquivo.PegarPagina(0)
Texto = Pagina.ExtrairTexto()

#Texto = ExpressaoRegular('Tabela de Veículos para o Leilão \\d+', '', Texto)
#Texto = ExpressaoRegular('LOTE', '', Texto)
#Texto = ExpressaoRegular('PÁTIO.*', '', Texto)
#Texto = ExpressaoRegular('CONDIÇÃO', '', Texto)
#Texto = ExpressaoRegular('CHASSI', '', Texto)
#Texto = ExpressaoRegular('PLACA', '', Texto)
#Texto = ExpressaoRegular('MARCA', '', Texto)
#Texto = ExpressaoRegular('MOTOR', '', Texto)
#Texto = ExpressaoRegular('COR', '', Texto)
#Texto = ExpressaoRegular('ANO', '', Texto)
#Texto = ExpressaoRegular('AVALIAÇÃO', '', Texto)
#Texto = ExpressaoRegular('\\n', '', Texto)
#Texto = ExpressaoRegular('R\\$ \\d+,\\d+ ', '\\n', Texto)
#Texto = ExpressaoRegular('R\\$ \\d+\\.\\d+,\\d+ ', '\\n', Texto)
#Texto = ExpressaoRegular('^\\s', '', Texto)
#Texto = ExpressaoRegular('           ', '', Texto)

#print(Texto)

def Processar(Arquivo):
        if Arquivo.get() == 'Selecione o Leilão':
                pass
        else:
                saida = open('Configuracoes/Leiloes/{}'.format(Arquivo.get()), encoding='utf8').read()
                cursor = loads(saida)

                expressoes = cursor['expressao']
                for expressao in expressoes:
                        print(expressao)

Janela = Tk()
Janela.geometry('800x500')
inp = ScrolledText(Janela,wrap=NONE)


Selecionada = StringVar(Janela)
Selecionada.set('Selecione o Leilão')
opcoes = os.listdir('Configuracoes/Leiloes/')
w = OptionMenu(Janela, Selecionada, *opcoes).pack()
Button(Janela, text='Processar', command=lambda : Processar(Selecionada)).pack()

#xbar = Scrollbar(orient='horizontal', command=inp.xview)
#inp.place(width=800,height=490)
#inp.configure(xscrollcommand=xbar.set)
#inp.insert(END,Texto)
#xbar.place(x=10, y=490, width=780, height=15)


Janela.mainloop()


