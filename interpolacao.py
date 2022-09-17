#!/usr/bin/env python3

"""Impreme amensagem de um e-mail

NÃO MANDE SPAL!!!
"""
__version__ = "0.1.0"

# Dica - para desacomplar ainda mais  o email, o template de email
# será guardado em um outro arquivo chamado "email_tmpl.txt".

email_tmpl = """
Olá, %(nome)s

Tem interesse em comprar %(produto)s?

Clique agora em %(link)s

Apenas %(quantidade)d disponíveis!

Preço promocional %(preco).2f
"""
import sys
import os

# Importamos o sys para permitir que o programa possa trabalhar
# via linha de comando com a passagem de um argumento(lista de emails)
arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de email.")
    sys.exit()

# Serão os dois argumentos exigidos na chamada do programa no shell.
filename = arguments[0]
tamplatename = arguments[1]

# os.curdir - current directory
path = os.curdir

filepath = os.path.join(path, filename)
templatepath = os.path.join(path, tamplatename)

clientes = []
for line in open(filepath):
    # TODO:substituir por list comprehension
    name, email = line.split(",")
    print(
        open(templatepath).read()
        %{
            "nome": name,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "http//canetaslegais.com",
            "quantidade": 1,
            "preco": 50.5,
            "email": email
        })
    print("-"*50)
    
