#!/usr/bin/env python3
"""
Faça um programa de terminal que exibe ao usuário uma lista dos quartos
disponíveis para alugar e o preço de cada quarto. Esta informação está 
disponível em um arquivo de texto separado por vírgulas.

'quartos.txt'
# código, nome, preço
1,Suite Master,500
2,Quarto Família,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias.No final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

'reservas.txt'
# Cliente,quarto,dias
Edmar,3,12

Se outro usuário tentar reservar o mesmo quarto, o programa deve exibir uma
mensagem informando que já está reservado.
"""

from datetime import datetime
import os
import sys

#arguments = sys.argv[1:]
quartos = {}

arq = open("quartos.txt", "r")
for line in arq:
    cod,name,price = line.split(",")
    quartos[cod] = [name,price.strip("\n")]
    #print(cod)
    #print(name)
    #print(price)
arq.close()

print("--"*20)
print(f'Welcome, Our available rooms are these:\n'.upper())
for k, v in quartos.items():
    if k == "código":
        pass
    else:
        print(f"Cod: {k}\nType: {quartos[k][0]}\nPrice$: {quartos[k][1]}")
        print("="*30)


question = input(f"\nWelcome! Which room would you like to book?\n")

user = input(f"What is your name? ")
room = input(f"Which room do you prefer? Enter the cod (1, 2, 3, 4) ")
start_book = input(f"Enter start date >>> Format = dd/mm/yyyy: ")
end_book = input(f"Enter end date >>> Format = dd/mm/yyyy: ")

start_obj = datetime.strptime(start_book, '%d/%m/%Y')
end_obj = datetime.strptime(end_book, '%d/%m/%Y')

# Preciso converter obj datetime para int para pode realizar os cálculos
amount_day = end_obj - start_obj 

print(amount_day)
