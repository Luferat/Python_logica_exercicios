'''
Exercício 02
Mostre os códigos para os seguintes passos:

 - Crie um conjunto chamado "colors" com os valores "vermelho", "verde", "azul".
 - Imprima o conjunto.
 - Adicione "amarelo" ao conjunto usando `add()`.
 - Remova o "verde" do conjunto usando `discard()`.
 - Imprima o número de itens usando `len()`.
 
Referências: https://www.w3schools.com/python/python_sets.asp
'''

# Crie um conjunto chamado "colors"
colors = {"vermelho", "verde", "azul"}

# Imprima o conjunto.
print(colors)

# Adicione "amarelo" ao conjunto usando `add()`.
colors.add("amarelo")

# Remova o "verde" do conjunto usando `discard()`.
colors.discard("verde")

# Imprima o número de itens usando `len()`.
print(len(colors))

print(colors)
