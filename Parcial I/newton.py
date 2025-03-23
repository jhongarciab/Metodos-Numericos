import math

def newton_raphson(funcion, fderivada, x_0, max_iter):
    f = lambda x: eval(funcion)
    df = lambda x: eval(fderivada)
    
    errores = []
    iteraciones = []
    for i in range(max_iter):
        x_0 = x_0 - (f(x_0) / df(x_0))
        errores.append(abs(x_0 - math.sqrt(7)))  # Guardar error absoluto
        iteraciones.append(i + 1)  # Guardar número de iteración
        
    return x_0, errores, iteraciones
