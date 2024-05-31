# braz/gerar/pis_pasep.py


import random


def gerar_pis_pasep():
    pesos = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pis_pasep = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    
    soma = sum(int(pis_pasep[i]) * pesos[i] for i in range(10))
    resto = 11 - (soma % 11)
    
    if resto == 10 or resto == 11:
        resto = 0
    
    pis_pasep += str(resto)
    
    return pis_pasep
