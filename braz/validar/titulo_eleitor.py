# braz/validar/titulo_eleitor.py


def validar_titulo_eleitor(titulo):
    if len(titulo) != 12 or not titulo.isdigit():
        return False
    
    digito_verificador_1 = int(titulo[-2])
    digito_verificador_2 = int(titulo[-1])
    
    somatorio_1 = sum(int(titulo[i]) * (9 - i % 8) for i in range(8))
    resto_1 = somatorio_1 % 11
    
    if resto_1 == 10:
        resto_1 = 0
    
    if resto_1 != digito_verificador_1:
        return False
    
    somatorio_2 = sum(int(titulo[i]) * (8 - i % 7) for i in range(9))
    resto_2 = somatorio_2 % 11
    
    if resto_2 == 10:
        resto_2 = 0
    
    return resto_2 == digito_verificador_2
