'''
8. Contador de Vogais

 - Peça uma palavra ao usuário.
 - Conte quantas vogais existem nela.

Exemplo:

Digite uma palavra: computador
Quantidade de vogais: 4

Dica

 - Percorra cada letra usando um loop.
'''

print("\n")

cont = 0
word = input("Digite a palavra: ")
vogais = "aeiou"

for letra in word:
    if letra.lower() in vogais:
        cont += 1

print(f"Total de {cont} vogais.")
