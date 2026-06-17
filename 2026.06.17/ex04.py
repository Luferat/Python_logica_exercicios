'''
4. Verificador de Número

 - Peça um número ao usuário.
 - Informe se ele é:
    - Positivo
    - Negativo
    - Zero

Dica

 - Use: `if...elif...else`

Desafio extra

 - Informe também se o número é par ou ímpar.
'''

print('\n')
num = int(input("Digite um numero inteiro: "))

# Positivo, negativo ou zero
if num > 0:
    print(f'{num} é positivo...')
elif num < 0:
    print(f'{num} é negativo...')
else:
    print("É zero...")


# Par ou ímpar
if num % 2 == 0:
    print("... e é par")
else:
    print("... e é ímpar")
