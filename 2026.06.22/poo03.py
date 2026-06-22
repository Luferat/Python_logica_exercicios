# usando decorators '@property' e '@attr.setter'

class Pessoa:

    # Construtor
    def __init__(self, nome):
        self.__nome = nome

    # Getter 
    @property
    def nome(self):
        print("getter")
        return self.__nome

    # Setter
    @nome.setter
    def nome(self, nome):
        print("setter")
        self.__nome = nome

p = Pessoa("Joca")

# Obtém o atributo "como atributo"
print("--->", p.nome)

# altera o atributo "como atributo"
p.nome = "Maria"

# Obtém o atributo "como atributo"
print("--->", p.nome)