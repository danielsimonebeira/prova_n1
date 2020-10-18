# 4 - Expliquei o que é decorator e padrões de projeto. Crie um decorator que mostre
# o tempo de execução de uma função que soma 4 números aleatórios. (2,0)
import time
import random

print(150 * '-' + '\n' + "Decorator: é a forma prática e reusável de adicionarmos "
                         "funcionalidades às nossas funções/métodos/classes, "
                         "sem precisarmos alterar o código delas" + '\n' + 150 * '-')

def calcula_tempo(function):
    def calcula():
        tempo_inicial = time.time()
        function()
        tempo_final = time.time()

        print("[{funcao}] Tempo total de execução: {tempo_total}".format(funcao=function.__name__,
                                                                         tempo_total=str(tempo_final - tempo_inicial)))
    return calcula

@calcula_tempo
def tempo():
    lista = []
    for i in range(0, 4):
        valor = random.randint(1, 50)
        lista.append(valor)
    print("Numeros: ", lista)

tempo()