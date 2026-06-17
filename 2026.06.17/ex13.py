'''
13. Sistema de Login Simplificado

 - Crie duas variáveis:

username
password

 - Verifique:

Usuário: admin
Senha: 1234

 - Se ambos estiverem corretos:

Acesso permitido

 - Caso contrário:

Acesso negado

Desafio extra

 - Permita até três tentativas.
'''

datauser = [
    "admin", "1234"
]

is_autorized = False

triers = 1
while True:
    print("\n------------------------------")
    username = input("Usuário: ")
    password = input("Senha: ")
    if username == datauser[0] and password == datauser[1]:
        is_autorized = True
        break

    if triers == 3:
        print("Tentativas esgotadas")
        break

    triers += 1
    print("Dados inválidos. Tente novamente.")


if is_autorized:
    print("Acesso permitido")
else:    
    print("Acesso negado")

