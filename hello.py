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
    key, value = arg.split("=")
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

print((msg[current_language]) * int(arguments["count"]))
