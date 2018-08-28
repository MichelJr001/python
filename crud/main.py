#!/usr/bin/env python3

# @author: Michel Anderson
# @github: https://github.com/MichelJr001

import sqlite3
import os

# Conecta com o arquivo do banco de dados
con = sqlite3.connect('database.db')
# Define o cursor do banco
c = con.cursor()

# Cria a classe painel
class painel():
    # Define o metodo cadastro com os parametros nome, sobrenome, nascimento, sexo e cpf
     def cadastro(self, nome, sobrenome, nascimento, sexo, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = nascimento
        self.sexo = sexo
        self.cpf = cpf
        
        # Tenta executar os comandos a seguir
        try:
            # Executa o comando SQL para inserir dados na tabela
            c.execute("INSERT INTO clientes (nome, sobrenome, nascimento, sexo, cpf) VALUES ('{}', '{}', '{}', '{}', '{}')".format(nome, sobrenome, nascimento, sexo, cpf))
            # Escreve as alterações no banco
            con.commit()
            print('Cadastrado com sucesso!')

        # Caso a função a cima der erro ele executa os comandos a seguir
        except:
            print('Erro ao cadastrar novo usuario!')
   
    # Define o metodo mostra, que imprime na tela todos o registros
     def mostra(self):
        # Executa o comando SQL e pega todos os registros da tabela
        c.execute('SELECT * FROM clientes;')
        
        # Joga os resultados na variavel resultado
        for resultado in c.fetchall():
            # Imprime na tela a variavel
            print(resultado)
        




# Inicia um loop infinito
while True:
    # Limpa o terminal antes de executar
    os.system('clear')
    # Menu de opções do painel
    esc = str(input('''
            Painel de cadastro
            ------ -- --------
        
        ( 1 ) -> Cadastrar novo cliente.
        ( 2 ) -> Mostrar clientes cadastrados.

    Escolha: '''))

    # Se o usuario digitar algo que não esteja em "12":
    if esc not in '12':
        print('Escolha invalida!')
    # Se não:
    else:
        # Se a escolha for 1:
        if esc == '1':
            # Coleta os dados do novo cliente
            print('[ Novo cliente ]\n')
            nome = input('Nome: ')
            snome = input('Sobrenome: ')
            nasc = input('Data de nascimento dd/mm/yyyy: ')
            sexo = input('Sexo [M/F]: ').upper().strip()[0]
            cpf = input('CPF: ')

            # Chama a fução cadastro da classe painel
            painel.cadastro(painel(), nome, snome, nasc, sexo, cpf)
            
        # Se a escolha for 2:
        elif esc == '2':
            # Chama a função mostra da classe painel
            print('[ Registros ]\n')
            painel.mostra(painel())

        # Pegunta se o usuario deseja continuar operando, coleta a primeira letra da reposta e
        # a tranforma em maiusculo
        cont = input('Deseja continuar operando? [N/S]: ').upper().strip()[0]

        # Se o usuario não deseja continuar ele para o loop
        if cont not in 'SN':
             print('Escolha invalida!')
        else: 
            if cont == 'N':
                os.system('clear')
                break
            else:
                pass
           

