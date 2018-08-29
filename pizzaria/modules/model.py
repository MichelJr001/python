#!/usr/bin/env python3

import sqlite3

class dbadmin():
	def __init__(self):
		cdb = sqlite3.connect("../databases/pizzaria.db")
		con = cdb.cursor()
	def view(opcao):
		print(opcao)
		
	def cadastro():
		pass
