'''
12. Cadastro de Produtos

 - Crie uma coleção contendo dicionários de produtos.
 - Exemplo:

products = [
    {
        "name": "Mouse",
        "price": 50
    },
    {
        "name": "Keyboard",
        "price": 120
    }
]

 - Exiba:

Mouse - R$ 50
Keyboard - R$ 120

Dica:

 - Use o método `dict.items()` para iterar o dicionário


Desafio extra

 - Calcule o valor total de todos os produtos.
'''

# Lista de dicionários
products = [
    {
        "name": "Mouse",
        "price": 50
    },
    {
        "name": "Keyboard",
        "price": 120.99
    }
]

print("\n")

total = 0

for product in products:
    total += product['price']
    print(f"{product['name']} - R${product['price']}")

print(f"\nTotal de R${total}")
