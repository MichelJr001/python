#!/usr/bin/env python3

from modules.model import dbadmin as control

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
			print("[!] Opção invalida")