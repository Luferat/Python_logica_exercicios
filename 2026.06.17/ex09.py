'''
9. Função de Saudação

 - Crie uma função chamada `greet()`
 - Ela deve receber um nome como argumento e exibir:

Olá, Maria!

 - Exemplo de uso:

greet("Maria")

Desafio extra

 - Retorne a mensagem em vez de apenas exibi-la.
'''


def greet(name):
    print(f"Olá, {name}!")


print("\n")
greet("Maria")


# Desafio
def greet2(name):
    return f"Olá, {name}!"


greet_out = greet2("Maria")
print(greet_out)
