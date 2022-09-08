"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.1.0"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("English", aula_ingles),
    ("Music", aula_musica),
    ("Dance", aula_danca),
]

for nome_atividade , atividade in atividades:
    
    print(f"Alunos da Atividade - {nome_atividade}\n")

    atividades_sala1 = []
    atividades_sala2 = []
    
    for aluno in atividade:
        if aluno in sala1:
            atividades_sala1.append(aluno)
        elif aluno in sala2:
            atividades_sala2.append(aluno)

    print("Sala 1", atividades_sala1)
    print("Sala 2", atividades_sala2)
    print("\n")