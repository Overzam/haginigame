def rendu(somme):
    a, b, c = 0, 0, 0
    while somme > 0:
        if somme > 5:
            a += 1
            somme -= 5
        elif somme > 2:
            b += 1
            somme -= 2
        else:
            c += 1
            somme -= 1
    return(a, b, c)
