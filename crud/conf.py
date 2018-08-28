#!/usr/bin/env python3

# @author: Michel Anderson
# @github: https://github.com/MichelJr001


import sqlite3
import os

con = sqlite3.connect('database.db')
c = con.cursor()

def criar():
    c.execute("""
CREATE TABLE IF NOT EXISTS clientes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome VARCHAR(20),
sobrenome VARCHAR(50),
nascimento DATE,
sexo VARCHAR(1),
cpf INT
);
    """)
    con.commit()

def deletar():
    c.execute("DROP TABLE IF EXISTS clientes;")
    con.commit()

os.system("clear")
print("""

	Painel de configurações
	------ -- -------------

    Escolha:

      (1) Criar banco.
      (2) Deletar banco.

""")

esc = str(input('>>> '))

if esc not in '12':
	print('Escolha invalida!')
else:
	if esc == '1':
	    criar()
	    print('Criado com sucesso!!')
	elif esc == '2':
	    deletar()
	    print('Deletado com sucesso!')
	else:
	    print("escolha invalida!")


