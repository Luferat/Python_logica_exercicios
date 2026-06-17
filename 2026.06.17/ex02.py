'''
2. Calculadora de Média

 - Crie um programa que receba três notas e calcule a média. Exemplo:

Nota 1: 8
Nota 2: 7
Nota 3: 9

Média: 8.0

Desafio extra

 - Mostre a situação do aluno (Aprovado, Recuperação, Reprovado) conforme:
 
Média >= 7  -> Aprovado
Média >= 5  -> Recuperação
Senão       -> Reprovado
'''

notas = [8, 7, 9]

print("\n")

# Cálculo direto
media = sum(notas) / len(notas)
print(f"Média: {media}")

# Usando um móduulo externo "statistics"
from statistics import mean, median, mode
print(f"Média: {mean(notas)}")
# ou
print(f"Média: {median(notas)}")
# ou
print(f"Média: {mode(notas)}")

# Também podemos usar a biblioteca NumPy
