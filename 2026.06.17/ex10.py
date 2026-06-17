'''
10. Calculadora com Funções

Crie as funções:

add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)

 - Cada função deve retornar o resultado da operação. Exemplo:

print(add(10, 5))

Desafio extra

 - Trate divisão por zero.
'''


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    return "Error: divide by zero"


print("\n")

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 0))
