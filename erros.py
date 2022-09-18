#!/usr/bin/env python3

import os
from re import I
import sys

# LBYL - LOOK BEFORE YOU LEAP

if os.path.exists("names.txt"):
    print("O arquivo existe!")
    input("...") #Race Condition - O arquivo poderá ser apagado
    # ou modificado por outro programa durante essa espera de 
    # entrada (input), mas a condição de existência já foi satisfeita.
    # Isso mostra a fragilidade desse método de controle de erros (LBYL)
    names = open("names.txt").readlines()

else:
    print("[Error] File names.txt not found.")
    sys.exit(1)

if len(names) >= 3:
    print(names[2])
else:
    print("[Erro] Missing name  in the list")
    sys.exit(1)
