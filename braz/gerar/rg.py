# braz/gerar/rg.py


def gerar_rg():
    return ''.join([str(random.randint(0, 9)) for _ in range(9)])
