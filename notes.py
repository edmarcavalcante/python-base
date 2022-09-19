#!/usr/bin/env python3
"""Bloco de notas

$ notes.py new "Minha Nota"
tag: tech
text:
Anotação geral sobre carreira  de tecnologia

$ notes.py read tag
...
...
"""
__version__= "0.1.1"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")
cmds = ("read", "new")

# capturar os argumentos
arguments = sys.argv[1:]
if not arguments:# Aqui não cabe try/exception porque é
    # uma validação.
    print("Invalid usage")
    print(f"You must choose a command: {cmds}")
    sys.exit(1)

if arguments[0] not in cmds: # Aqui não cabe try/exception porque é
    # uma validação.
    print(f"Invalid command {arguments[0]}")

if len(arguments) >= 3:
    print(f"You passed more than two arguments. they were: {arguments}")
    print(f"The program require only two parameter!")
    sys.exit(0)

if arguments[0] == "read":
    # Scrip made for my
    """
    tag = arguments[1]
    print(tag)
    with open(filepath, "r") as file_:
        for lista in file_:
            if tag in lista:
                print(lista)
    """        
    # Script made for teacher
    for line in open(filepath):
        title,tag,text = line.split("\t")
        try:
            read_ = arguments [1].lower #criei a variável read_
            # para poder implementar o try.
            if tag.lower() == read_:
                print(f"title: {title}")
                print(f"text: {text}")
                print("-" * 30)
                print()
            else:
                print(f"This 'tag' doesn't exist yet!")
                sys.exit(0)
        except IndexError as e:
            print(f"{str(e)}")
            print(f"You forgot the second parameter - TITLE!")
            sys.exit(1)

if arguments[0] == "new":
    try:
        title = arguments[1]
        text = [
            f"{title}",
            input("tag:").strip(),
            input("text:\n").strip(),
        ]

        with open (filepath, "a") as file_:
            file_.write("\t".join(text)+"\n")
    
    except IndexError as e:
        print(f"{str(e)}")
        print(f"You forgot the second parameter! - TITLE")
        sys;exit(1)

