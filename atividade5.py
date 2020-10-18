# 5 - Duas amigas estabeleceram o código abaixo para que suas mensagens não
# fossem lidas pelas demais pessoas.
# 0 12 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
# ' ' a b c d e f g h i j k l m n o p q r s t u v w x y z
# Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0.
# Faça um método para "traduzir", que recebe uma lista com uma mensagem
# (secreta) e "traduz" a sequência armazenada em uma lista.

dicionario_letras = {0: ' ', 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm',
                     14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
lista = []


def separa_valor_digitado(lista):
    #Obtem o valor agregado em uma lista e separa em mais valores
    lista_valor_separado = []
    for separa_valores in lista:
        lista_valor_separado.append(list(separa_valores))
    return lista_valor_separado

def descriptografa_letra(lista, dicionario_letras):
    lista_valor_separado = separa_valor_digitado(lista)
    nova_lista = []
    strl = ""
    for remove_separador in lista_valor_separado:
        remove_separador.remove('-')
        for conta_lista_string in remove_separador:
            conta_lista_inteiro = int(conta_lista_string)
            for dicionario in dicionario_letras.get(conta_lista_inteiro):
                nova_lista.append(dicionario)
    print("Palavra descriptografada: ", strl.join(nova_lista))

def criptografa_letra(lista, dicionario_letras):
    lista_valor_separado = separa_valor_digitado(lista)
    nova_lista = []
    for conta_lista in lista_valor_separado[0]:
        for chave_dicionario in dicionario_letras.values():
            if conta_lista == chave_dicionario:
                valor_gerado = list(dicionario_letras.keys())[list(dicionario_letras.values()).index(conta_lista)]
        nova_lista.append(valor_gerado)
    print("Palavra criptografada: ", str(nova_lista).replace('[', '').replace(',', '').replace(']', '').rstrip())

while True:
    try:
        menu = int(input("Digite: \n- 1 para descriptografar  \n- 2 para criptografar mensagem \n- 3 sair \n"))
        if menu == 1:
            numero = input("Digite os numeros Separado por ' - ', para que seja gerada sua palavra/frase/texto: \n")
            lista.append(numero)
            descriptografa_letra(lista, dicionario_letras)
            lista.clear()

        elif menu == 2:
            palavra = input("Digite a palavra/frase/texto para gerar os numeros: \n")
            lista.append(palavra.lower())
            criptografa_letra(lista, dicionario_letras)
            lista.clear()
        elif menu == 3:
            exit()
        else:
            print("\n", 30 * "-", "\n  Favor digitar 1 ou 2", "\n", 30 * "-")
    except Exception as ex:
        print("Valor digitado inválido!")
        print(ex)