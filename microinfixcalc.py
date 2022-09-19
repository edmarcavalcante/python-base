#!/usr/bin/env python3

"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py mul 10 5 
50

$ infixcalc.py sum 5 2 
7

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em infixcalc.log
"""
__version__ = "0.1.0"
__autor__ = "Edmar Almeida"
__license__ = "Unlicense"

#It is need work with sys.argv method.
import sys

#It is necessary import os to salve infixcalc.log
import os

from datetime import datetime

operation = ["sum", "sub", "mul", "div"]
 
list_param = []

for param in sys.argv[1:]:
    list_param.append(param)

if len(list_param) != 3:
    print(f"Three arguments are required!")
    print(f"The first parameter must be {operation} and the other two numbers")
    sys.exit(1)

if list_param[0].lower() not in operation:
    print(f"Invalid Option! {list_param[0]}")
    print(f"You first parameter must be {operation}")
    sys.exit(1)

v1 = float(list_param[1]) 
v2 = float(list_param[2])
op = list_param[0]
result = None

# TODO: Usar dict de funções
if op == operation[0]:
    result = v1 + v2
elif op == operation[1]:
    result = v1 - v2
elif op == operation[2]:
    result = v1 * v2
elif op == operation[3]:
    result = round((v1 / v2),3)



# curdir - current directory 
path = os.curdir
filepath = os.path.join(path, "infixcalc.log")  
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "anonymous")

print(result)

# Tratando erro - PermissionError - caso o usuário não tenha acesso 
# a pasta onde o arquivo de log será salvo.
try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {op}, {v1}, {v2} = {result}\n")
except PermissionError as e:
    # TODO: logging
    print(str(e))
    sys.exit(1)

