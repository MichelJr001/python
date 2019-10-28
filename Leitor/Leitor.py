# -*- coding: utf-8 -*-
# Versao: 0.5
# Desenvolvido por Michel Anderson
# Data Ultima alteração 28/10/2019
# AllRisk Soluções  © 2019

from tkinter.scrolledtext 	import ScrolledText
from Modulos.Manipulador import *
from tkinter import filedialog
from tkinter import *
import os

Arquivos = os.listdir('Arquivos/')
os.system('cls')

class Principal():
    def __init__(self, janela):
        # Funções do menu
        def Sair():
            self.janela.destroy()
            
        # Configurações do menu
        self.janela = janela
        self.janela = janela
        self.menubar = Menu(self.janela)
        self.janela.config(menu=self.menubar)
		
		
        self.Menu_1 = Menu(self.menubar)
        self.Menu_2 = Menu(self.menubar)
        self.Menu_3 = Menu(self.menubar)

        self.menubar.add_cascade(label='Janela', menu=self.Menu_1)	
        self.menubar.add_cascade(label='Arquivo', menu=self.Menu_2)

        self.Menu_1.add_command(label='Sair', command=Sair)
        
        self.Menu_2.add_command(label='Abrir', command=self.NovoArquivo)
        self.Menu_2.add_command(label='Salvar')
        self.Menu_2.add_command(label='Adicionar pasta', command=self.AdicionarPasta)

        # Corpo do programa
        self.TituloUm = Label(self.janela, text='Selecione o arquivo ou diretorio:')
        self.EntradaLocal = ScrolledText(self.janela, relief='solid')
        self.EntradaLocal.focus()
        self.BotaoSelecionar = Button(self.janela, text='...', borderwidth='0.5', relief='solid', command=self.NovoArquivo)
        self.BotaoProcessar = Button(self.janela, text='Processar arquivos', bg='#008000', fg='#fff', borderwidth='0.5', relief='solid', command=lambda : self.ProcessarTexto(self.EntradaLocal))
        
        # Posição dos widgets
        self.TituloUm.place(x=5,y=0, width=170, height=30)
        self.EntradaLocal.place(x=5,y=30, width=550, height=50)
        self.BotaoSelecionar.place(x=555,y=30,width=55, height=50)
        self.BotaoProcessar.place(x=660,y=5,width=120, height=30)
        
        self.janela.mainloop()

    def NovoArquivo(self):
        self.EntradaLocal.delete('1.0',END)
        self.LocalArquivo =  filedialog.askopenfilename(initialdir = "o:/captura/",title = "Informe o arquivo PDF do Edital",filetypes = (("Arquivos PDF","*.pdf"),("Todos os Arquivos","*.*")))
        self.EntradaLocal.insert(END,self.LocalArquivo + '\n')
    def AdicionarPasta(self):
        self.LocalPasta = filedialog.askdirectory()
        Arquivos = os.listdir(self.LocalPasta)
        for Arquivo in Arquivos:
            self.EntradaLocal.insert(END,self.LocalPasta + '/' + Arquivo + '\n')
        
    def ProcessarTexto(self,Local):
        self.Local = Local
        TextoPDF = PegarTexto(self.Local)
        for Paginas in TextoPDF:
            processado = open('Resultado\\'+NomeArquivo+'.txt', 'a')
            #Decomentar somente quando querer os dados em um só arquivo
            #processado = open('Resultado\\Resultado.txt', 'a')
            processado.write(str(NomeArquivo)+str(Paginas))
            processado.close()        
    def ProcessarImagens(self):
        ExtrairImagens(self.Local)

    
# Configurações da janela
janela = Tk()
janela.title('AllRisk Soluções - Conversor de PDFs')
janela.iconbitmap('Configuracoes/icones/pdf.ico')
janela.geometry('800x500')
Arquivos = []
# Classe principal
Principal(janela)
