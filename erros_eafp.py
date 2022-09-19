#!/usr/bin/env python3

import os
import sys

# EAFP - Easy to Ask Forgiveness than permission
# Atteintion - You need anticipate all possible erros and
# treat them individually. That is goog practice.
try:
    names = open("names.txt").readlines()
except FileNotFoundError:
    print("[Error]  File names.txt noot found!") # Erro se o 
    # arquivo não for encontrado
    sys.exit(1)
    # TODO: Usar um retry
else:
    print("Sucesso!") # É ambíguo o uso de else nesse caso,
    # mas pode ser usado.
finally:
    print("Executa isso sempre!")

try:
    print(names[4])
except IndexError as a:
    print(f"{str(a)}")
    sys.exit(1)

