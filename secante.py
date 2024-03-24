import math
def secante(funcion, x_0, x_1, tolerancia, max_iter):
    f = lambda x: eval(funcion)
    iter = 0

    while iter < max_iter:
        if abs(f(x_1) - f(x_0)) < tolerancia:
            break

        x_2 = x_1 - f(x_1) * (x_1 - x_0) / (f(x_1) - f(x_0))
        
        x_0 = x_1
        x_1 = x_2

        iter += 1

    return x_2