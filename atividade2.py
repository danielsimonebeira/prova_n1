# 2 - Crie um classe Funcionário com os atributos nome, idade e salário. Deve ter
# um método aumenta_salario. Crie duas subclasses da classe funcionário,
# programador e analista, implementando o método nas duas subclasses. Para
# o programador some ao atributo salário mais 20 e ao analista some ao salário
# mais 30, mostrando na tela o valor. Depois disso, crie uma classe de testes
# instanciando os objetos programador e analista e chame o método
# aumenta_salario de cada um.
import unittest

class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
    def aumenta_salario(self, salario, percentual):
        percentual = percentual / 100.0
        aumento = percentual * salario
        novo_salario = salario + aumento
        return novo_salario

class Programador(Funcionario):
    def __init__(self, salario):
        novo_salario = self.aumenta_salario(salario, 20)
        print("salário do programador: ", novo_salario)

class Analista(Funcionario):
    def __init__(self, salario):
        novo_salario = self.aumenta_salario(salario, 30)
        print("salário do analista: ", novo_salario)

dado = Funcionario("Maria", 21, 900)
print("Nome: ", dado.nome)
print("Idade: ", dado.idade)
print("Salário: ", dado.salario)
print("--- Aumento ---")
Programador(dado.salario)
Analista(dado.salario)



# Depois disso, crie uma classe de testes instanciando os objetos programador e analista e chame o método aumenta_salario de cada um.
class Testa(unittest.TestCase):
    def test_inclusao_dados_funcionario(self):
        dado = Funcionario("Maria", 21, 900)
        self.assertEqual(dado.nome, "Maria")
        self.assertEqual(dado.idade, 21)
        self.assertEqual(dado.salario, 900)

    def test_retorno_metodo_aumenta_salario(self):
        novo_salario = Funcionario.aumenta_salario(self, 900, 20)
        self.assertEqual(novo_salario, 1080.0)

if __name__ == '__main__':
        unittest.main()