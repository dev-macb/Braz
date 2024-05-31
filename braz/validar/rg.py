# braz/validar/rg.py


def validar_rg(rg):
    return rg.isdigit() and len(rg) in [9, 10]
