#!/usr/bin/env python3

import socket
import os

os.system('clear')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target = ''
port = 8080

try:
    s.connect((target, port))
    while True:
        mensagem = str(input(f'[####]: '))
        if mensagem == "quit":
            s.send(mensagem.encode('utf-8'))
            break
        s.send(mensagem.encode('utf-8'))
    s.close()

except:
    s.close()
    print('[ WARNING ]: Erro ao conectar-se ao servidor')


