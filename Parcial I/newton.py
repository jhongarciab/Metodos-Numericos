import math
def newton_raphson(funcion, fderivada, x_0, max_iter):
    f = lambda x: eval(funcion)
    df = lambda x: eval(fderivada)
    
    for i in range(max_iter):
        x_0 = x_0 - (f(x_0) / df(x_0))
        if i == max_iter -1:
            return x_0