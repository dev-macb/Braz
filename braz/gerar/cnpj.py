# braz/gerar/cnpj.py


import random


def gerar_cnpj():
    cnpj = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    cnpj += '0001'  # Números fixos para empresas fictícias
    
    pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cnpj[i]) * pesos[i] for i in range(12))
    resto = soma % 11
    
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto
    
    cnpj += str(digito_verificador_1)
    
    pesos.insert(0, 6)
    soma = sum(int(cnpj[i]) * pesos[i] for i in range(13))
    resto = soma % 11
    
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto
    
    cnpj += str(digito_verificador_2)
    
    return cnpj
