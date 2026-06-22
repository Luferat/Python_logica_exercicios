class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    # O decorator transforma o método em um (pseudo) atributo
    # O uso é opcional

    def get_nome(self):
        # Métod "get" para enviar o atributo protegido para o resto do mundo
        return self.__nome

    def set_nome(self, valor):
        # Validações, sanitizações, autenticação...
        self.__nome = valor


p = Pessoa("André")
# print(p.__nome) # Erro
# print(p._Pessoa__nome)  # Não faça isso! É muito feito!

print(" --> ", p.get_nome())
# print(" ---> ", p.nome)

p.set_nome("Luferat")
print(" ---> ", p.get_nome())
