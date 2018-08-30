#!/usr/bin/env python3

import sqlite3

azul = "\033[36m"
rosa = "\033[35m"
vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
normal = "\033[0m"

cdb = sqlite3.connect('databases/pizzaria.db')
con = cdb.cursor()

class dbadmin():
	def __init__(self):
		print('[{}PyPyzza{}] Conectado com o banco de dados!'.format(vermelho, normal))
	def view(opcao):
		if opcao == 'clientes':
			con.execute('SELECT * FROM clientes')
			for resultados in con.fetchall():
				print(resultados)
		elif opcao == 'sabores':
			con.execute("SELECT * FROM sabores;")
			for resultados in con.fetchall():
				print(resultados)
		elif opcao == 'pedidos':
			con.execute("SELECT * FROM pedidos;")
			for resultados in con.fetchall():
				print(resultados)
		else: 
			print('[{}ops{}] Algo deu errado!'.format(vermelho, normal))

	def cadastroClientes(nome, tel, end):
		self.nome = nome_cliente
		self.tel = telefone
		self.end = endereco

		con.execute("INSERT INTO clientes (nome, telefone, endereco) VALUES ('{}', '{}', '{}')")
		cdb.commit()
	def cadastroPedidos():
		pass
	def cadastroSabores():
		pass