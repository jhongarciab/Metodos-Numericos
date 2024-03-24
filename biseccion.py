import math
def biseccion(funcion, a, b, tolerancia, max_iter):
    f = lambda x: eval(funcion)
    if f(a) * f(b) >= 0:
        print("El intervalo no funciona para este método.")
        return None
    iter = 0
    while abs(a - b) >= tolerancia:
        x_r = (a + b) / 2
        if f(a) * f(x_r) == 0:
            return x_r
        elif f(a) * f(x_r) < 0:
            b = x_r
        else:
            a = x_r
        iter += 1
        if iter >= max_iter:
            break
    return (a + b) / 2