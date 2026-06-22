# usando decorators '@'

class Pessoa:

    def __init__(self, nome):
        self.__nome = nome

    # Getter 
    @property
    def nome(self):
        print("getter")
        return self.__nome

    @nome.setter
    def nome(self, nome):
        print("setter")
        self.__nome = nome

p = Pessoa("Joca")

print("--->", p.nome)

p.nome = "Maria"

print("--->", p.nome)