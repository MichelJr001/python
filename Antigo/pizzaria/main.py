#!/usr/bin/env python3

from modules.controller import pizzaria as commands
import os

# tabela de cores do sistema

azul = "\033[36m"
rosa = "\033[35m"
vermelho = "\033[31m"
verde = "\033[32m"
amarelo = "\033[33m"
normal = "\033[0m"

def banner():
    os.system("clear")
    print('''
        {}██████╗ ██╗   ██╗██████╗ ██╗███████╗███████╗ █████╗{} v0.1{}
        {}██╔══██╗╚██╗ ██╔╝██╔══██╗██║╚══███╔╝╚══███╔╝██╔══██╗{}
        ██████╔╝ ╚████╔╝ ██████╔╝██║  ███╔╝   ███╔╝ ███████║
        ██╔═══╝   ╚██╔╝  ██╔═══╝ ██║ ███╔╝   ███╔╝  ██╔══██║{}
        ██║        ██║   ██║     ██║███████╗███████╗██║  ██║
        ╚═╝        ╚═╝   ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
        -------------------[ {}Michel Anderson{} ]--------------{}
    '''.format(azul, amarelo, normal, azul, normal, azul, amarelo, azul, normal))

os.system("clear")
while True:
    banner()
    print('''
        {}[ 1 ]{} -> Novo Cliente
        {}[ 2 ]{} -> Novo Pedido
        {}[ 3 ]{} -> Visualizar
        {}[ 4 ]{} -> Sair

    '''.format(azul, normal, azul, normal, azul, normal, azul, normal))
    esc = int(input('[ {}Opção{} ]: '.format(amarelo, normal)))

    if esc == 1:
        os.system('clear')
        banner()
        nome = str(input('[Nome do cliente]: '))
        tel = str(input('[Telefone do cliente]: '))
        end = str(input('[Endereço do cliente]: '))

        commands.cadastroClientes(nome, tel, end)
    elif esc == 2:
        pass
    elif esc == 3:
        os.system('clear')
        banner()
        print('''
            {}[ 1 ]{} -> Clientes
            {}[ 2 ]{} -> Pedidos
            {}[ 3 ]{} -> Sabores
        '''.format(azul, normal, azul, normal, azul, normal))

        opcao = str(input('[ {}Opção{} ]: '.format(amarelo, normal)))

        if opcao not in '123':
            print('[ {}Pypizza{} ]: Opção invaliada, tente novamente!'.format(vermelho, normal))
        else:
            if opcao == '1':
                commands.ver(1)
                pass
            elif opcao == '2':
                commands.ver(2)
                pass
            elif opcao == '3':
                commands.ver(3)
                pass
            
    elif esc == 4:
        banner()
        print('{}\t# Github: https://github.com/MichelJr001\n\t# Twitter: https://twitter.com/_Michel_Jr_\n\n\tObrigado por usar!\n{}'.format(azul, normal))
        break
    else: 
        print('[ {}Pypizza{} ]: Opção invaliada, tente novamente!'.format(vermelho, normal))
    
    cont = input('[ {}Pypizza{} ]: Deseja continuar? [S/N]: '.format(amarelo, normal)).upper().strip()[0]

    if cont == 'S':
        os.system('clear')
        pass
    elif cont == 'N':
        banner()
        print('{}\t# Github: https://github.com/MichelJr001\n\t# Twitter: https://twitter.com/_Michel_Jr_\n\n\tObrigado por usar!\n{}'.format(azul, normal))
        break
    else:
        banner()
        print('{}\t# Github: https://github.com/MichelJr001\n\t# Twitter: https://twitter.com/_Michel_Jr_\n\n\tObrigado por usar!\n{}'.format(azul, normal))
        break

    
