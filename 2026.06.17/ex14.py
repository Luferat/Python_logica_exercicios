'''
14. Função de Cálculo de bmi

 - Crie uma função `calculate_bmi(weight, height)`
 - Retorne `weight / (height ** 2)`
 - Exemplo:

bmi = calculate_bmi(80, 1.75)

Desafio extra

 - Classifique o resultado como:

Abaixo do peso
Peso normal
Sobrepeso
Obesidade
'''

def calculate_bmi(weight, height):
    return weight / (height ** 2)

print('\n')

bmi = calculate_bmi(80, 1.75)

# Formatação de números
# Referências: https://www.w3schools.com/python/python_string_formatting.asp
print(f'{bmi:.2f}')

if bmi < 18.5:
    print("Abaixo do peso")
elif bmi < 25:
    print("Peso normal")
elif bmi < 30:
    print("Sobrepeso")
elif bmi < 35:
    print("Obesidade Grau I")
elif bmi < 40:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")
