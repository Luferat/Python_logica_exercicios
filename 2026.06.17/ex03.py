'''
3. Lista de Compras

 - Crie uma lista contendo pelo menos cinco itens de supermercado.
 - Em seguida, exiba:
    - Todos os itens
    - Quantidade de itens na lista
    - Primeiro item
    - Último item

Desafio extra

 - Permita adicionar um novo item ao final da lista.
'''

print('\n')

items = ["banana", "leite", "ovos", "azeitonas", "arroz"]

# Todos os itens
print(items)
# ou
print("Já temos:")
for item in items:
    print(f' - {item}')

print("\n")
# loop de input de usuário
while True:
    new = input("Digite o novo item ou [Enter] para concluir: ")
    if new == "":
        break
    items.append(new)

print("\n")
# Mostra os itens atuais    
for item in items:
    print(f' - {item}')