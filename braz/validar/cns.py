# braz/validar/cns.py


def validar_cns(cns):
    if len(cns) != 15 or not cns.isdigit():
        return False
    
    soma = sum(int(cns[i]) * (15 - i) for i in range(15))
    
    return soma % 11 == 0
