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

__version__ = "0.0.1"
__autor__ = "Edmar Almeida"
__license__ = "Unlicense"

# Impontando o módulo 'os' para poder acessar as variáveis de ambiente.
# Tem como propósito deixar o programa mais dinâmico e não precisar alterar
# a variável 'currente_language' de forma manual.

import os 
# O módulo 'os' serve para poder manipular e acessar varuiáveis do sistema operacional

# Função important getenv("Variável")

current_language = os.getenv("LANG", "en_US")[:5]
# O segundo argumento da função getenv() é o valor padrão
# caso a variável LANG esteja vazia - evita erros.

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Modo!"

print(msg)
