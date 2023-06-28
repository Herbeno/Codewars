def summult(inicial,final):
    multiplos = soma = 0

    if inicial <= 0 or final <= 0:
        return "INVALID"

    while multiplos < final:
        multiplos += inicial
        if multiplos >= final:
            break
        soma += multiplos
    return soma

print(summult(2,9))