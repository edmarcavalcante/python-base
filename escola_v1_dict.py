"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.1"

# Dados

salas = {
  "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
  "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]
}

atividades = {
"Ingles": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
"Música": ["Erik", "Carlos", "Maria"],
"Dança": ["Gustavo", "Sofia", "Joana", "Antonio"],
}

for chave, valor in atividades.items():
    un_sala1 = set(salas["sala1"]) & set(atividades[chave])
    un_sala2 = set(salas["sala2"]) & set(atividades[chave])
    print(f"Turma de  {chave}:")
    print(f"Sala 01 - {un_sala1}")
    print(f"Sala 02 - {un_sala2}")
    print("\n")

 