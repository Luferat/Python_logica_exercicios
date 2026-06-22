'''
2. Classe Produto: crie uma classe chamada Product com os sequintes requisitos:
Atributos:

name
price

Método:

show_info()

O método deve exibir os dados do produto. Exemplo

Notebook - R$ 3500.00

Desafio
Crie três produtos diferentes e exiba todos.
'''


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print(f'{self.name} - R$ {self.price}')


print("\n")

prods = [
    Product("Notebook", 3500.00),
    Product("Caneta", 250.99),
    Product("Impressora", 800.99),
]

for prod in prods:
    prod.show_info()
