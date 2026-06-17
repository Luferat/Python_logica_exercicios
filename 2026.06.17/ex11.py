'''
11. Função com Argumentos Nomeados

 - Crie uma função `create_user(name, age, city)`
 - Exemplo de chamada:

 # kwargs
create_user(
    age=22,
    name="Maria",
    city="Rio de Janeiro"
)

 - Saída esperada:

Nome: Maria
Idade: 22
Cidade: Rio de Janeiro

Desafio

 - Praticar argumentos posicionais e nomeados, para isso, teste também:

create_user("Maria", 22, "Rio de Janeiro")
'''

def create_user(name, age, city):
    print(f'''
 - Nome: {name}
 - Idade: {age}
 - Cidade: {city}
    ''')

print("\nArgmentos nomeados")    
create_user(
    age=22,
    name="Maria",
    city="Rio de Janeiro"
)

print("\nArgumentos ordenados")
create_user("Maria", 22, "Rio de Janeiro")
