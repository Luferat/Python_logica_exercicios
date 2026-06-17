'''
6. Soma dos Números

 - Utilizando um loop, calcule a soma dos números de 1 até 100.
 - Exemplo de resultado esperado:

5050

Dica

 - Crie uma variável acumuladora:
 
total = 0
'''

total = 0
for num in range(1, 101):
    total += num

print(f"\nTotal: {total}")    