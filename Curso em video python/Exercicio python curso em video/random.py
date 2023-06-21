import random

valores = [
    "A crise do sistema feudal",
    "A passagem para o capitalismo",
    "As corporações de ofícios e a burguesia",
    "As feiras, os cambistas e as cidades",
    "O aumento da população urbana",
    "A retomada comercial na baixa idade média",
    "Capitalismo e circulação"
]

random.shuffle(valores)  # Embaralha a lista de valores

for posicao, valor in enumerate(valores, start=1):
    print("Na posição", posicao, "temos:", valor)
