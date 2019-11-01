#!/usr/bin/env python3

# @author: Michel Anderson
# @github: MichelJr001
# @Twitter: _Michel_Jr_

# Criador de arquivos json 1.0

import json
import os

class cadastro():
    def __init__(self, nome, snome, idade, nascionalidade):
        self.nome = nome
        self.snome = snome
        self.idade = idade
        self.nascionalidade = nascionalidade

        new_json = {"Nome": nome, "Sobrenome": snome, "Idade": idade, "Nascionalidade": nascionalidade}

        # Tranforma o json new_json em string
        json_puro = json.dumps(new_json)

        # Tranforma a string json_puro em json
        json_filtrado = json.loads(json_puro)

        dados = open("dados.txt", "a")
        dados.write("\n--------------------------------------------------------------------------------")
        dados.write("\nNome: {}\nSobrenome: {}\nIdade: {}\nNascionalidade: {}\n".format(json_filtrado["Nome"], json_filtrado["Sobrenome"], json_filtrado["Idade"], json_filtrado["Nascionalidade"]))
        dados.close()

        dados_json = open("dados.json", "a")
        dados_json.write(json_puro)
        dados_json.write("\n")
        dados_json.close()

os.system('clear')
print("""
\033[32m
   ###    ##    ##    ###    ##       ##    ## ######## ########               ##  ######   #######  ##    ## v1.0 
  ## ##   ###   ##   ## ##   ##        ##  ##       ##  ##                     ## ##    ## ##     ## ###   ##    
 ##   ##  ####  ##  ##   ##  ##         ####       ##   ##                     ## ##       ##     ## ####  ##    
##     ## ## ## ## ##     ## ##          ##       ##    ######                 ##  ######  ##     ## ## ## ##    
######### ##  #### ######### ##          ##      ##     ##               ##    ##       ## ##     ## ##  ####    
##     ## ##   ### ##     ## ##          ##     ##      ##               ##    ## ##    ## ##     ## ##   ###    
##     ## ##    ## ##     ## ########    ##    ######## ######## #######  ######   ######   #######  ##    ##
\033[0m
 @author: Michel Anderson
 @github: MichelJr001
""")

while True:

        nome_cliente = str(input("[\033[32m NOME DO CLIENTE \033[0m]: "))
        snome_cliente = str(input("[\033[32m SOBRENOME DO CLIENTE \033[0m]: "))
        sexo_cliente = str(input("[\033[32m SEXO DO CLIENTE \033[0m]: "))
        idade_cliente = str(input("[\033[32m DATA DE NASCIMENTO DO CLIENTE \033[0m]: "))
        nacionalidade_cliente = str(input("[\033[32m NACIONALIDADE DO CLIENTE \033[0m]: "))


        try:
                cadastro(nome_cliente, snome_cliente, idade_cliente, nacionalidade_cliente)
                print("[\033[32m SUCESSO \033[0m]: Cadastrado com sucesso!\n")
        except:
                print("[\033[31m ERRO AO CADASTRAR \033[0m]: Algo de errado aconteceu!\n")


        esc = str(input("[\033[32m DESEJA CONTINUAR \033[0m][S/N]: ")).upper().strip()[0]

        if esc not in "SN":
                print("[\033[31m ERRO \033[0m]: Escolha invalida!")
        else:
                if esc == "S":
                        os.system(clear)
                else:
                        break


