#!/usr/bin/env python3

from threading import Thread
from datetime import datetime
import socket
import os

# Configuração do horario
now = str(datetime.now())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

myhost = '' # Ip so servidor alvo
myport = 8080 # Porta do servidor

# Cores do sistema
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
normal = '\033[0m'

# Abre o arquivo de logs para a escrita
logs = open('logs/msg.log', 'a')

# Tenta executar os comandos do bloco
try:
    os.system('clear')
    s.bind((myhost, myport))
    s.listen(1)
    print(f'''\n\t\t\t[ SERVIDOR {myhost}:{myport} ]\n
        \t[ STATUS ]: {verde}ON{normal}
        \tEsperando Clientes...
    ''')

    end, cliente = s.accept()
    print(f'[ Mensagem ]: {cliente[0]}:{cliente[1]} Conectou-se com o servidor \n')

    while True:
        msg = end.recv(1024)

        if msg:
            if msg.decode('utf-8') == 'quit':
                print(f'[ Mensagem ]: Conexão terminada com {cliente[0]}:{cliente[1]}')
                logs.close
                break
            else:
                logs.write(f"[ {now[:19]} ] {cliente[0]}:{cliente[1]} : {msg.decode('utf-8')}\n")
                print(f"[ {cliente[0]}:{cliente[1]} ]: {msg.decode('utf-8')}")
        else:
            pass
except:
    s.close()
    print('[ WARNING ]: Falha durante a conexão!\n')
logs.close
s.close()