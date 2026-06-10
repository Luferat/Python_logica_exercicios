'''
Exercício 01
Mostre os códigos para os seguintes passos:

 - Crie um dicionário chamado "car" com as chaves "marca", "modelo", "ano"
   e valores "Ford", "Mustang", 2024.
 - Imprima o valor da chave "modelo".
 - Adicione uma nova chave "cor" com o valor "vermelho".
 - Remova a chave "marca" usando `pop()`.
 - Imprima o dicionário.

Referências: https://www.w3schools.com/python/python_dictionaries.asp
'''

# Crie um dicionário chamado "car"
car = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 2024
}

# Imprima o valor da chave "modelo".
print(car["modelo"])

# Adicione uma nova chave "cor" com o valor "vermelho".
car["cor"] = "vermelho"

# Remova a chave "marca" usando `pop()`.
car.pop("marca")

# ou usando `del`
# del car["marca"]

# Imprima o dicionário.
print(car)