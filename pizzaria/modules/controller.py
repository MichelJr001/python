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
			control.view("clientes")
		elif opcao == 2:
			control.view("pedidos")
		elif opcao == 3:
			control.view("sabores")
		else:
			print('[{}ops{}] Opção invalida!'.format(vermelho, normal))