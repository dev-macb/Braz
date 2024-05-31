# braz/validar/cpf.py


def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    
    resto = soma % 11
    
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto
    
    if digito_verificador_1 != int(cpf[9]):
        return False
    
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    
    resto = soma % 11
    
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto
    
    return digito_verificador_2 == int(cpf[10])
