#!/usr/bin/env python3

import sqlite3

azul = "\033[36m"
rosa = "\033[35m"
vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
normal = "\033[0m"

class dbadmin():
	def __init__(self):
		print('[{}PyPyzza{}] Conectado com o banco de dados!'.format(vermelho, normal))
	def view(opcao):

		cdb = sqlite3.connect('databases/pizzaria.db')
		con = cdb.cursor()

		if opcao == 'clientes':
			con.execute('SELECT * FROM clientes')
			for resultados in con.fetchall():
				print(resultados)
			cdb.close()
		elif opcao == 'sabores':
			con.execute("SELECT * FROM sabores;")
			for resultados in con.fetchall():
				print(resultados)
			cdb.close()
		elif opcao == 'pedidos':
			con.execute("SELECT * FROM pedidos;")
			for resultados in con.fetchall():
				print(resultados)
			cdb.close()
		else: 
			print('[{}ops{}] Algo deu errado!'.format(vermelho, normal))
			cdb.close()

	def cadastroClientes(nome, tel, end):

		cdb = sqlite3.connect('databases/pizzaria.db')
		con = cdb.cursor()
		con.execute("INSERT INTO clientes (nome, telefone, endereco) VALUES ('{}', '{}', '{}')".format(nome, tel, end))
		cdb.commit()
		cdb.close()

	def cadastroPedidos():
		pass
		
	def cadastroSabores():
		pass

