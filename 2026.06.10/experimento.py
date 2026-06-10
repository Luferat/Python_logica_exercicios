'''
Acessando itens aninhados
'''


coisas = [
    [
        # Coleção aninhada da coleção "coisas" com o índice [0]
        "vermelho", #[0]
        "verde", #[1]
        "azul", #[2]
    ],  # [0]
    "peteca",  # [1]
    ["amarelo", "roxo", "laranja"],  # [2]
    "casa",
    "motoca",
    2026,
    ("gato", "cachorro", "coelho"),
    "cão",
    {"cor": "preto", "tamanho": "médio"},
    True,
    {"usuario", "senha", "email"}
]

print(coisas[0])
print(coisas[0][1])

print(coisas[6][1])

print(coisas[8]["tamanho"])