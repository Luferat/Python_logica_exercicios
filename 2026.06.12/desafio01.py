"""
Desafio 01
Mostre a tabuada de multiplicação do número 5 à partir de 5 x 0 até 5 x 10.
"""

print("\n----------------------\n")

mult = int(input("Digite um número inteiro: "))
i = 0
while i <= 10:
    resultado = mult * i
    print(f"{mult} x {i} = {resultado}")
    i += 1