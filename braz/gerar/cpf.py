# braz/gerar/cpf.py


import random


def gerar_cpf():
    cpf = ''.join([str(random.randint(0, 9)) for _ in range(9)])
    
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    
    resto = soma % 11
    
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto
    
    cpf += str(digito_verificador_1)
    
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    
    resto = soma % 11
    
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto
    
    cpf += str(digito_verificador_2)
    
    return cpf
