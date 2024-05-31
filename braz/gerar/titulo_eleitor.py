# braz/gerar/titulo_eleitor.py


import random


def gerar_titulo_eleitor():
    titulo = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    somatorio_1 = sum(int(titulo[i]) * (9 - i % 8) for i in range(8))
    resto_1 = somatorio_1 % 11

    if resto_1 == 10:
        resto_1 = 0

    titulo += str(resto_1)
    somatorio_2 = sum(int(titulo[i]) * (8 - i % 7) for i in range(9))
    resto_2 = somatorio_2 % 11

    if resto_2 == 10:
        resto_2 = 0

    titulo += str(resto_2)

    return titulo
