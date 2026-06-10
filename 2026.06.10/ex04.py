'''
Exercício 4
Mostre os códigos para os seguintes passos:

 - Crie uma lista chamada "colors" com os valores "vermelho", "verde", "azul".
 - Imprima o primeiro item da lista.
 - Mude o segundo item para "amarelo".
 - Adicione "roxo" ao final da lista usando `append()`.
 - Remova "vermelho" da lista usando `remove()`.
 - Imprima a lista.

Referências: https://www.w3schools.com/python/python_lists.asp
'''

# Crie uma lista chamada "colors"
colors = ["vermelho", "verde", "azul"]

# Imprima o primeiro item da lista.
print(colors[0])

# Mude o segundo item para "amarelo".
colors[1] = "amarelo"

# Adicione "roxo" ao final da lista usando `append()`.
colors.append("roxo")

# Remova "vermelho" da lista usando `remove()`.
colors.remove("vermelho")

# Imprima a lista.
print(colors)
        