import math

def regula_falsi(funcion, a, b, tolerancia, max_iter):
    f = lambda x: eval(funcion)
    if f(a) * f(b) >= 0:
        print("El intervalo no funciona para este método.")
        return None, [], []
    
    errores = []
    iteraciones = []
    iter = 0
    raiz_aprox = (a + b) / 2  
    while abs(a - b) >= tolerancia and iter < max_iter:
        x_r = b - (f(b) * (a - b)) / (f(a) - f(b))
        errores.append(abs(x_r - math.sqrt(7))) 
        iteraciones.append(iter + 1)  
        
        if f(a) * f(x_r) == 0:
            return x_r, errores, iteraciones
        elif f(a) * f(x_r) < 0:
            b = x_r
        else:
            a = x_r
        
        iter += 1
        raiz_aprox = x_r
    
    return raiz_aprox, errores, iteraciones