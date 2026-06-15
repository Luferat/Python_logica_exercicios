def my_function(operacao, *numbers):
  total = 0
  if operacao == "*":
    total = 1
  for num in numbers:
    total = eval(f'{total} {operacao} {num}')
  return total

print(my_function('+', 1, 2, 3))
print(my_function('*', 10, 20, 30, 40))
print(my_function('+', 5))
print(my_function('/', 10, 2))

'''
Desafio
Ajuste o código para permitir a divisão de uma quantidade arbitrária de números. Exemplo: 10 / 2 / 5
'''
