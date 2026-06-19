'''
15. Mini Relatório de Vendas

 - Considere:

sales = [150, 320, 450, 210, 500]

 - Exiba:

Total vendido
Maior venda
Menor venda
Média de vendas

Dica

 - Pesquise ou utilize os métodos de números:
 - Referências: https://www.w3schools.com/python/python_math.asp

sum()
max()
min()
len()
'''


def mean(iterable):
    # Upgrade: função para calcular a média
    return sum(iterable) / len(iterable)


sales = [150, 320, 450, 210, 500]

print("\n")

print(f'''
Total vendido: ${sum(sales):.2f}
Maior venda ${max(sales):.2f}
Menor venda ${min(sales):.2f}
Média de vendas ${mean(sales):.2f}
''')
