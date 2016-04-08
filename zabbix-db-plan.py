#!/usr/bin/python
# -*- coding: utf-8 -*-
#@author: Janssen

import os, sys
from termcolor import colored

def banner():
    print colored('''
                       _____       _      _      _
                      |__  / __ _ | |__  | |__  (_)__  __
                        / / / _` || '_ \ | '_ \ | |\ \/ /
                       / /_| (_| || |_) || |_) || | >  <
                      /____|\__,_||_.__/ |_.__/ |_|/_/\_\.

                ____          _          _
               |  _ \   __ _ | |_  __ _ | |__    __ _  ___   ___
               | | | | / _` || __|/ _` || '_ \  / _` |/ __| / _ \.
               | |_| || (_| || |_| (_| || |_) || (_| |\__ \|  __/
               |____/  \__,_| \__|\__,_||_.__/  \__,_||___/ \___|

                 ____   _                       _
                |  _ \ | |  __ _  _ __   _ __  (_) _ __    __ _
                | |_) || | / _` || '_ \ | '_ \ | || '_ \  / _` |
                |  __/ | || (_| || | | || | | || || | | || (_| |
                |_|    |_| \__,_||_| |_||_| |_||_||_| |_| \__, |
                                                          |___/

    ''', 'red', attrs=['bold'])
    print

def menu():
    os.system('clear')
    banner()
    print colored("[+] - Bem-vindo ao ZABBIX DATABSE PLANNING - [+]\n"
    "[+] - Este script é baseado na documentação oficial do Zabbix - https://www.zabbix.com/documentation/3.0/manual/installation/requirements - [+]\n"
    "[+] - O objetivo é exibir o tamanho de espaço em disco que você terá que providenciar para uso do Zabbix de acordo com as respostas - [+]\n"
    "[+] - Desenvolvido por Janssen Lima - [+]\n"
    "[+] - Dúvidas/Sugestões envie e-mal para janssen@conectsys.com.br - [+]", 'blue')
    print
    print colored("--- Escolha uma opção do menu ---",'yellow', attrs=['bold'])
    print
    print "[1] - Executar"
    print
    print "[0] - Sair"
    print
    menu_opcao()

def menu_opcao():
    opcao = raw_input( "[+] - Selecione uma opção: ")
    if opcao == '1':
        execucao()
    elif opcao == '0':
        sys.exit()
    else:
        menu()

def execucao():
    print ""
    print colored ('''Entre com os dados:''', 'red', attrs=['bold'])
    print ""
    itens = input("Quantidade de itens que serão monitorados: ")
    intervalo = input("Intervalo de atualização que será utilizado (média. ex.: 60 segundos): ")
    dias_historicos = input("Número de dias de retenção dos dados históricos: ")
    dias_estatisticas = input("Número de dias de retenção dos dados estatísticos: ")
    dias_eventos = input("Número de dias de retenção dos dados de eventos: ")
    quantidade_eventos = input("Digite a quantidade de eventos por segundo (1 no pior cenário): ")
    vps = itens/intervalo

    bytes_h = 90
    bytes_t = 90
    bytes_e = 170
    historico = (dias_historicos * (24 * 3600 * vps * bytes_h)) / 1024 / 1024 / 1024
    estatistica = ((itens / 3600) * (24 * 3600 * dias_estatisticas) * bytes_t) / 1024 / 1024 / 1024
    eventos = (dias_eventos * quantidade_eventos * 24 * 3600 * bytes_e) / 1024 / 1024 / 1024

    total = (historico + estatistica + eventos)

    print "Total de espaço em disco necessário para armazenar os dados na base é:", total, "GB"
    print "A performance requerida do teu servidor será de:", vps, "vps"

    print ""
    raw_input("Pressione ENTER para continuar")
    main()

def main():
    menu()

main()
