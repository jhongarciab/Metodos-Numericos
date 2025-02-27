import math
import numpy as np
import matplotlib.pyplot as plt

def biseccion(funcion, a, b, tolerancia, max_iter):
    """
    Método de Bisección para encontrar una raíz de una función en un intervalo dado.

    Parámetros:
    - funcion (str): La función a evaluar, expresada en términos de 'x'.
    - a (float): Límite inferior del intervalo.
    - b (float): Límite superior del intervalo.
    - tolerancia (float): Criterio de convergencia basado en el error absoluto.
    - max_iter (int): Número máximo de iteraciones permitidas.

    Retorna:
    - float: Aproximación de la raíz encontrada.
    - None: Si el intervalo no es válido o si no converge en las iteraciones dadas.
    """
    
    # Definir la función a partir de la cadena de entrada usando eval
    f = lambda x: eval(funcion)

    # Graficar la función para visualizar el punto de corte con el eje X
    x_vals = np.linspace(a - 2, b + 2, 1000)
    y_vals = [f(x) for x in x_vals]
    
    plt.figure(figsize=(10,6))
    plt.plot(x_vals, y_vals, label=f"f(x) = {funcion}", linewidth=2)
    plt.axhline(0, color='black', linestyle='--', linewidth=1)
    plt.axvline(0, color='black', linestyle='--', linewidth=1) 
    plt.axvline(a, color='red', linestyle='--', linewidth=1, label='a')
    plt.axvline(b, color='blue', linestyle='--', linewidth=1, label='b')
    plt.legend()
    plt.title("Visualización de la función y su punto de corte con el eje X")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    plt.show()
    
    # Verificar que el intervalo sea válido para la bisección (f(a) y f(b) deben tener signos opuestos)
    if f(a) * f(b) >= 0:
        print("El intervalo no es válido para el método de bisección. Asegúrese de que f(a) y f(b) tengan signos opuestos.")
        return None
    
    iteraciones = 0
    while abs(a - b) >= tolerancia and iteraciones < max_iter:
        x_r = (a + b) / 2  # Punto medio del intervalo
        
        # Si la función evalúa exactamente a cero, encontramos la raíz
        if f(x_r) == 0:
            return x_r
        
        # Determinar en qué subintervalo se encuentra la raíz
        if f(a) * f(x_r) < 0:
            b = x_r  # La raíz está en [a, x_r]
        else:
            a = x_r  # La raíz está en [x_r, b]
        
        iteraciones += 1
    
    # Retornar la mejor aproximación de la raíz encontrada
    return (a + b) / 2

# Ejemplo de uso 
funcion = input("Ingrese la función en términos de x: ")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
tolerancia = float(input("Ingrese la tolerancia: "))
max_iter = int(input("Ingrese el número máximo de iteraciones: "))
raiz = biseccion(funcion, a, b, tolerancia, max_iter)
print(f"La raíz de la función {funcion} es: {raiz}")
