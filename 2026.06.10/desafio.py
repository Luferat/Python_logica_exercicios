'''
Desafio. Observe a variável abaixo:

```
users = [
	{
		"name": "Joca da Silva",
		"email": "jocasilva@email.com",
		"birth": "1980-10-25",
		"password": "Q1w2e3r4t5"
	},
	{
		"name": "Marineuza Siriliano",
		"email": "sirineuza@email.com",
		"birth": "2000-09-14",
		"password": "A1s2d3f4g5"
	},
	{
		"name": "Hermenildo Sagassuga",
		"email": "hermesaga@email.com",
		"birth": "1979-12-20",
		"password": "Z1x2c3v4b5"
	},
	{
		"name": "Setembrino Trocatapas",
		"email": "setbrino@email.com",
		"birth": "2002-04-18",
		"password": "P0o9i8u7y6"
	}
]
```

Mostre os códigos necessários para:

 - Mostrar todos os dados do primeiro e último usuário cadastrados.
 - Mostrar a senha do "Hermenildo Sagassuga".
 - Mostrar o e-mail do "Setembrino Trocatapas".
 - Criar uma lista contendo todos os e-mails e exibir.
 - Mostrar apenas o primeiro nome de todos os usuários.
 - Mostrar quantos usuários existem na lista.
 - Criar uma lista contendo apenas os nomes e exibir em ordem alfabética.
 - Alterar o e-mail de "Marineuza Siriliano".
 - Adicionar um novo usuário à lista.
 - Remover o usuário "Setembrino Trocatapas".
 - Adicionar a chave "active": True em todos os usuários.
 - Mostrar o dicionário atualizado.

'''

import pprint

# Lista de dicionários representando os usuários
users = [
	{
		"name": "Joca da Silva",
		"email": "jocasilva@email.com",
		"birth": "1980-10-25",
		"password": "Q1w2e3r4t5"
	},
	{
		"name": "Marineuza Siriliano",
		"email": "sirineuza@email.com",
		"birth": "2000-09-14",
		"password": "A1s2d3f4g5"
	},
	{
		"name": "Hermenildo Sagassuga",
		"email": "hermesaga@email.com",
		"birth": "1979-12-20",
		"password": "Z1x2c3v4b5"
	},
	{
		"name": "Setembrino Trocatapas",
		"email": "setbrino@email.com",
		"birth": "2002-04-18",
		"password": "P0o9i8u7y6"
	}
]

# Mostrar todos os dados do primeiro e último usuário cadastrados.
print("\n")
print("Primeiro usuário:", users[0])
print("Último usuário:", users[-1])

# Mostrar a senha do "Hermenildo Sagassuga".
print("\n")
print("Senha:", users[2]["password"])

# Mostrar o e-mail do "Setembrino Trocatapas".
print("\n")
print("E-mail:", users[3]["email"])

# Criar uma lista contendo todos os e-mails e exibir.
print("\n")
emails = [] # inicializa a lista de e-mails
# Iterador para extrair os usuários
for user in users:
    emails.append(user["email"]) # adiciona o e-mail do usuário atual à lista de e-mails
    # ou imprima diretamente o e-mail do usuário atual
    print(" • Nome:", user["name"])
    print("       • E-mail:", user["email"])
    
print("\nEmails: ", emails)

# Mostrar apenas o primeiro nome de todos os usuários.
print("\n")
print("Primeiros nomes:")
for user in users:
	first_name = user["name"].split(" ")[0] # divide o nome completo e pega o primeiro elemento
	print(" • ", first_name)
      
# Mostrar quantos usuários existem na lista.
print("\n")	  
print("Quantidade de usuários:", len(users))

# Criar uma lista contendo apenas os nomes e exibir em ordem alfabética.
print("\n")	
names = [] # inicializa a lista de nomes
for user in users:	
	names.append(user["name"]) # adiciona o nome do usuário atual à lista de nomes
print("Nomes na ordem obtida: ", names)
names.sort() # ordena a lista de nomes em ordem alfabética
print("Nomes em ordem alfabética: ", names)

# Alterar o e-mail de "Marineuza Siriliano".
print("\n")
users[1]["email"] = "marineuzinha.siriliano@email.com" # altera o e-mail do segundo usuário (índice 1)
print("E-mail atualizado de Marineuza Siriliano:", users[1]["email"])

# Adicionar um novo usuário à lista.
print("\n")	
new_user = {
	"name": "Carlos Eduardo",
	"email": "carlinhos@email.com",
	"birth": "1995-07-30",
	"password": "C1a2r3l4o5s6"
}
users.append(new_user) # adiciona o novo usuário à lista de usuários

# Remover o usuário "Setembrino Trocatapas".
print("\n")
users.pop(3) # remove o usuário no índice 3 (Setembrino Trocatapas)
# ou
# users.remove(users[3]) # remove o usuário no índice 3 (Setembrino Trocatapas)
# ou
# del users[3] # remove o usuário no índice 3 (Setembrino Trocatapas)

# Adicionar a chave "active": True em todos os usuários.
print("\n")
for user in users:	
	user["active"] = True # adiciona a chave "active" com o valor True para cada usuário

# Mostrar o dicionário atualizado.
print("\nUsuários atualizado:")
print(users)

# Motrar o dicionário atualizado de forma mais legível
pprint.pprint(users)
