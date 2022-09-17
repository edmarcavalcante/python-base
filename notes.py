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
__version__= "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")
cmds = ("read", "new")

# capturar os argumentos
arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"You must choose a command: {cmds}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "read":
    # Scrip made for my
  #  tag = arguments[1]
  #  print(tag)
  #  with open(filepath, "r") as file_:
  #      for lista in file_:
  #          if tag in lista:
  #              print(lista)
            
    # Script made for teacher
    for line in open(filepath):
        title,tag,text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()

if arguments[0] == "new":
    tile = arguments[1] # TODO: tratar exception
    text = [
        f"{tile}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]

    with open (filepath, "a") as file_:
        file_.write("\t".join(text)+"\n")

