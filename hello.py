#!/usr/bin/env python3


# Doc string - boas práticas

"""Hello world multi language.

depending on the language configured in the environment, the program displays 
the corresponding essage.

How use:

Have a properly configured LANG variable  ex:

    export LANNG=pt_BR
     
Execution:

    python3 hello.py
    or
    ./hello.py
"""

#Meta dados -python community conversion
# É uma boa prática

__version__ = "0.1.3"
__autor__ = "Edmar Almeida"
__license__ = "Unlicense"

# Impontando o módulo 'os' para poder acessar as variáveis de ambiente.
# Tem como propósito deixar o programa mais dinâmico e não precisar alterar
# a variável 'currente_language' de forma manual.

import os 
# O módulo 'os' serve para poder manipular e acessar variáveis do sistema operacional
import sys

arguments = {
    "lang": None,
    "count": None,
}

for arg in sys.argv[1:]:
    # TODO: tratar ValueError
    # Tratando erros com o método - EAFP
    try:
        key, value = arg.split("=")
    except ValueError as e:
        # TODO: Logging - o log pode ser importante no reporte de erros.
        print(f"{str(e)}") # É important passar a mensagem do erro para a
        # equipe de suporte analisar.
        print("You need to use `=`")
        print(f"You passed {arg}")
        print(f"Try with --key=value")
        sys.exit(1)
    
    
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid option {key}")
        sys.exit()
    arguments[key] = value

# Função important getenv("Variável")

current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input(
            "Choose a language:"
        )
# O segundo argumento da função getenv() é o valor padrão
# caso a variável LANG esteja vazia - evita erros.
current_language = current_language[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mundo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour Monde"
    }

# >>>>> 3 MÉTODOS DE TRATAR ERROS <<<<<<

# MÉTODO 1 - Tratando erro no método LBYL
"""
if current_language in msg:
    message = msg[current_language]
else:
    print(f"Language is invalid.Please, choose from: {list(msg.keys())}")
    sys.exit(1)
"""
# MÉTODO 2 - Para estruturas de dados DICT
""" 
Outra opção de tratar KeyError em Dicionários é usar o método get()
Dict.get(param1, param2) tenta acessar a key passada como primeiro
parámetro, caso não encontre, usar o valor default passado no segundo
parámetro. 
Seria assim >>> message = msg.get(current_language, msg["pt_BR"])
"""

#MÉTODO 3 - Tratando erro no método EAFP - o código fica mais performático,
# um vez que não precisa fazer a  validação do bloco if.
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[Error] {str(e)}")
    print(f"Language is invalid.Please, choose from: {list(msg.keys())}")
    sys.exit(1)

print(msg * int(arguments["count"]))