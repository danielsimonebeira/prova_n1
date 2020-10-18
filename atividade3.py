# 3 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
# caso o valor seja inválido e continue pedindo até que o usuário informe um valor
# válido.(2,0)
nota = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

contador = 1
while True:
    valor = int(input("Digite de 1 a 10: "))
    for i in nota:
        if i == valor:
            print("valor {} Digitado corretamente".format(valor))
            exit()
    contador += 1
