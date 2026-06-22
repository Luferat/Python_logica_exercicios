'''
1. Criando sua primeira classe: crie uma classe chamada Person, atendendo aos requisitos:

 - Possua os atributos `name` e `age`.
 - Crie um objeto com seus próprios dados.
 - Exiba os valores dos atributos na tela.
 - Saída esperada (exemplo)

Name: João
Age: 25

Dica
 - Atributos podem ser criados dentro do método __init__().
'''

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("João", 25)

print('\n')
print(f'Name: {p1.name}')
print(f'Age: {p1.age}')