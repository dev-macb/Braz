# braz/gerar/cns.py


import random


def gerar_cns():
    cns = ''.join([str(random.randint(0, 9)) for _ in range(15)])
    soma = sum(int(cns[i]) * (15 - i) for i in range(15))
    
    if soma % 11 != 0:
        return gerar_cns()  # Tenta novamente se a soma não for múltiplo de 11
    
    return cns
