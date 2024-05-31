# braz/validar/cnpj.py


def validar_cnpj(cnpj):
    if len(cnpj) != 14 or not cnpj.isdigit():
        return False
    
    pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma = sum(int(cnpj[i]) * pesos[i] for i in range(12))
    resto = soma % 11
    
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto
    
    if digito_verificador_1 != int(cnpj[12]):
        return False
    
    pesos.insert(0, 6)
    soma = sum(int(cnpj[i]) * pesos[i] for i in range(13))
    resto = soma % 11
    
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto
    
    return digito_verificador_2 == int(cnpj[13])
