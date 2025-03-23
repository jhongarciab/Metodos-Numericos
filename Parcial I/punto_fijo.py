import math
def punto_fijo(funcion, x_0, max_iter):
    f = lambda x: eval(funcion)
    x_actual = x_0
    for _ in range(max_iter):
        x_siguiente = f(x_actual)
        x_actual = x_siguiente
    return x_actual
