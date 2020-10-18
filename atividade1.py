# 1 - Darth Vader achou que seu exército de stormtrooper estava prendendo poucos
# rebeldes, então lhe contratou para desenvolver um programa que leia um conjunto
# indeterminado de número de refém presos por mês. Ao final da listagem informe o
# menor e o maior número de capturados, a média e o valor mais próximo a média (não
# utilize funções prontas do python). (2,0)

import random

lista_refem = []

dicionario_mes = {1: "Janeiro",
                  2: "Fevereiro",
                  3: "Março",
                  4: "Abril",
                  5: "Maio",
                  6: "Junho",
                  7: "Julho",
                  8: "Agosto",
                  9: "Setembro",
                  10: "Outubro",
                  11: "Novembro",
                  12: "Dezembro"}

for mes in dicionario_mes.values():
    contador = 1
    dias_do_mes = 30

    while contador < dias_do_mes:
        variavel = random.randint(1, 100)
        lista_refem.append(variavel)
        contador += 1

    media = sum(lista_refem) / len(lista_refem)
    diffs = {value: abs(value - media) for value in lista_refem}

    print(150 * "-", "\nMês de {}".format(mes))
    print("Total de reféns: ", lista_refem)
    print("Total de reféns: ", len(lista_refem))
    print("Maior número de reféns: ", max(lista_refem))
    print("Menor número de reféns: ", min(lista_refem))
    print("Média de reféns: ", media)
    print("Valor aproximado da media: ", min(diffs, key=diffs.get))


    lista_refem.clear()
