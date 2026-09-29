# CÓDIGO NO REFACTORIZADO
def calc(t, a, b=0):
    if t == 1:
        res = a * b
        return res
    elif t == 2:
        res = (a * b) / 2
        return res
    elif t == 3:
        res = 3.14159 * (a * a)
        return res

print(calc(1, 5, 10))