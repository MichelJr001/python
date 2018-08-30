#!/usr/bin/env python3

from modules.model import dbadmin as control

azul = "\033[36m"
rosa = "\033[35m"
vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
normal = "\033[0m"

class pizzaria():
	def __init__(self):
		print("Só testando")
	def ver(opcao):
		if opcao == 1:
			try:
				control.view("clientes")
			except:
				print('[{}ops{}] Não temos clientes cadastrados!'.format(vermelho, normal))
		elif opcao == 2:
			try:
				control.view("pedidos")
			except:
				print('[{}ops{}] Não temos pedidos!'.format(vermelho, normal))
		elif opcao == 3:
			control.view("sabores")
		else:
			print('[{}ops{}] Opção invalida!'.format(vermelho, normal))

	def cadastro(opcao):
		pass
