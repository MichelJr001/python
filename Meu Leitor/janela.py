# -*- coding: utf-8 -*-
# Versao: 0.1
# Desenvolvido por Michel Anderson
# Data Ultima alteração 30/10/2019
#  AllRisk Soluções © 2019


from Configuracoes.Vizualizador import *
from re import sub as ExpressaoRegular
from threading import Thread
from tkinter import filedialog
from tkinter.scrolledtext import *
from json import *
from tkinter import *
import os

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
        self.BotaoSelecionar = Button(self.janela, text='...', bg='#ff0018',fg='#fff', borderwidth='0.5', relief='solid', command=self.NovoArquivo)
        self.BotaoProcessar = Button(self.janela, text='Processar arquivos', bg='#008000', fg='#fff', borderwidth='0.5', relief='solid', command=self.Processar)
        self.BotaoLimpar = Button(self.janela, text='Limpar', bg='#fff000', fg='#fff', borderwidth='0.5', relief='solid')
        
        self.Selecionada = StringVar(self.janela)
        self.Selecionada.set('Selecione o Leilão')
        opcoes = os.listdir('Configuracoes/Leiloes/')
        w = OptionMenu(self.janela,self.Selecionada, *opcoes)
        w.config(bg='#fff',borderwidth='0.5', relief='solid',activebackground='#fff')
        w.pack()
        
        # Posição dos widgets
        self.TituloUm.place(x=5,y=20, width=170, height=30)
        self.EntradaLocal.place(x=5,y=50, width=550, height=50)
        self.BotaoSelecionar.place(x=555,y=50,width=55, height=50)
        self.BotaoProcessar.place(x=650,y=50,width=120, height=30)
        self.BotaoLimpar.place(x=650,y=90,width=120, height=30)
        
        self.janela.mainloop()

    def NovoArquivo(self):
        self.LocalArquivo =  filedialog.askopenfilename(initialdir = 'o:/captura/',title = 'Informe o arquivo PDF do Edital',filetypes = (('Arquivos PDF','*.pdf'),('Todos os Arquivos','*.*')))
        Arquivos.append(str(self.LocalArquivo))
        self.EntradaLocal.insert(END,self.LocalArquivo + '\n')

        Arquivo =  LerPDF(open(self.LocalArquivo,'rb'))
        Paginas = Arquivo.NumeroPaginas()
        Pagina = Arquivo.PegarPagina(0)
        self.Texto = Pagina.ExtrairTexto()
        
    def AdicionarPasta(self):
        self.LocalPasta = filedialog.askdirectory()
        ArquivosPasta = os.listdir(self.LocalPasta)
        for NomeArquivo in ArquivosPasta:
            Arquivos.append(self.LocalPasta + '/'+ Arquivo)
            self.EntradaLocal.insert(END,self.LocalPasta + '/' + NomeArquivo + '\n')

            Arquivo =  LerPDF(open('{}/{}'.format(self.LocalPasta,NomeArquivo), 'rb'))
            Paginas = Arquivo.NumeroPaginas()
            Pagina = Arquivo.PegarPagina(0)
            Texto = Pagina.ExtrairTexto()
            
    def Processar(self):	
        th=Thread(target=self.ProcessarTexto)
        th.start()
    def ProcessarTexto(self):
        self.Arquivo = str(self.Selecionada.get())
        Resultado = self.Texto
        if self.Arquivo == 'Selecione o Leilão':
                pass
        else:
                saida = open('Configuracoes/Leiloes/{}'.format(self.Arquivo), encoding='utf8').read()
                cursor = loads(saida)

                expressoes = cursor['expressao']
                # PARA TRATAR OS DADOS
                for expressao in expressoes:
                    #expressao = ExpressaoRegular('\\|(.*)', '$1', expressao)
                    ResultadoExpressao = ExpressaoRegular('.*|', '', expressao)
                    Resultado = ExpressaoRegular(expressao, ResultadoExpressao, Resultado)
                    
                    ResultadoExpressao = ''

                print(Resultado)    
    def LimparDados():
        Arquivos.clear()
        self.EntradaLocal.delete('1.0',END)

        
# Configurações da janela
janela = Tk()
janela.title('Beta')
janela.iconbitmap('Configuracoes/icones/pdf.ico')
janela.geometry('800x500')
Arquivos = []
# Classe principal
Principal(janela)
