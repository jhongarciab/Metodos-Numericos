import math

def punto_fijo(funcion, x_0, max_iter):
    f = lambda x: 7 / x 
    
    errores = []
    iteraciones = []
    x_actual = x_0
    for i in range(max_iter):
        x_siguiente = f(x_actual)
        errores.append(abs(x_siguiente - math.sqrt(7))) 
        iteraciones.append(i + 1)  
        x_actual = x_siguiente
    
    return x_actual, errores, iteraciones
