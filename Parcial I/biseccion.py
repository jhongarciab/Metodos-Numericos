import math

def biseccion(funcion, a, b, tolerancia, max_iter):
    f = lambda x: eval(funcion)
    if f(a) * f(b) >= 0:
        print("El intervalo no funciona para este método.")
        return None, []
    
    errores = []
    iteraciones = []
    iter = 0
    raiz_aprox = (a + b) / 2  # Inicialización
    while abs(a - b) >= tolerancia and iter < max_iter:
        x_r = (a + b) / 2
        errores.append(abs(x_r - math.sqrt(7)))  # Guardar error absoluto
        iteraciones.append(iter + 1)  # Guardar número de iteración
        
        if f(a) * f(x_r) == 0:
            return x_r, errores, iteraciones
        elif f(a) * f(x_r) < 0:
            b = x_r
        else:
            a = x_r
        
        iter += 1
        raiz_aprox = x_r
    
    return raiz_aprox, errores, iteraciones

