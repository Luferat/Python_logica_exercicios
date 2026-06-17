'''
7. Lista de Alunos

 - Crie uma lista contendo nomes de alunos.
 - Percorra a lista exibindo:

Aluno: Maria
Aluno: João
Aluno: Pedro

Desafio extra

 - Exiba também a posição de cada aluno, por exemplo:

1 - Maria
2 - João
3 - Pedro
'''

names = ["Maria", "João", "Pedro", "Joca", "Clésio"]

print("\nNomes:\n")

for name in names:
    print(f'Aluno: {name}')

print("\nNúmeros e nomes:\n")

cont = 1
for name in names:
    print(f'{cont} - {name}')
    cont += 1