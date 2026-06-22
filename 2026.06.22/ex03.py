'''
3. Calculadora Orientada a Objetos: crie uma classe chamada Calculator com os seguintes requisitos:

Métodos

add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)

Exemplo

calc = Calculator()
print(calc.add(10, 5))

Desafio
Evite divisão por zero.
'''


class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "ERRO: divisão por 0"
        return a / b


calc = Calculator()

print("\n")
print("Soma: ", calc.add(10, 5))
print("Subtração: ", calc.subtract(10, 5))
print("Multiplicação: ", calc.multiply(10, 5))
print("Divisão: ", calc.divide(10, 5))
print("Divisão: ", calc.divide(5, 0))
