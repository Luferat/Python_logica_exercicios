class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    # Método "get" para enviar o atributo protegido para o resto do mundo
    def get_nome(self):
        return self.__nome

    # Método "set" para alterar o valor do atributo de forma segura
    def set_nome(self, valor):
        # Aqui, faremos validações, sanitizações, autenticação...
        self.__nome = valor


p = Pessoa("André")
# print(p.__nome) # Erro

# print(p._Pessoa__nome)  # Finciona, mas, não faça isso em produção! É muito feito!

# Obtendo o atributo com o método 'get'
print(" --> ", p.get_nome())

# alterando o atributo com o método 'set'
p.set_nome("Luferat")

# Obtendo o atributo com o método 'get'
print(" ---> ", p.get_nome())
