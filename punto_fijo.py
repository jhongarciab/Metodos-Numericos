import math
import numpy as np
import matplotlib.pyplot as plt

def punto_fijo(funcion, x_0, tolerancia, max_iter):
    """
    Método de Punto Fijo para encontrar una raíz de una función dada.

    Parámetros:
    - funcion (str): La función iterativa g(x) en términos de 'x'.
    - x_0 (float): Valor inicial para la iteración.
    - tolerancia (float): Criterio de convergencia basado en el error absoluto.
    - max_iter (int): Número máximo de iteraciones permitidas.

    Retorna:
    - float: Aproximación de la raíz encontrada o None si no converge.
    """
    
    # Definir la función g(x) desde la cadena de entrada
    g = lambda x: eval(funcion)
    
    # Almacenar los valores de iteración para graficar
    iteraciones = [x_0]
    x_actual = x_0
    
    for _ in range(max_iter):
        x_siguiente = g(x_actual)
        iteraciones.append(x_siguiente)
        
        # Verificar convergencia
        if abs(x_siguiente - x_actual) < tolerancia:
            break
        
        x_actual = x_siguiente
    else:
        print("Advertencia: No convergió en las iteraciones dadas.")
        return None
    
    # Graficar la función g(x) y la línea y = x
    x_vals = np.linspace(min(iteraciones) - 0.5, max(iteraciones) + 0.5, 100)
    y_gx = [g(x) for x in x_vals]
    y_identity = x_vals
    
    plt.figure(figsize=(8,6))
    plt.plot(x_vals, y_gx, label=r"$g(x)$", color="g")
    plt.plot(x_vals, y_identity, label=r"$y = x$", color="r", linestyle="--")
    plt.axhline(0, color='k', linewidth=1)
    plt.axvline(0, color='k', linewidth=1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gráfica de $g(x)$ y $y = x$")
    plt.legend()
    plt.grid()
    plt.show()
    
    return x_actual

# Ejemplo de uso
funcion = input("Ingrese la función g(x): ")
x_0 = float(input("Ingrese el valor de x_0: "))
tolerancia = float(input("Ingrese la tolerancia: "))
max_iter = int(input("Ingrese el número máximo de iteraciones: "))
raiz = punto_fijo(funcion, x_0, tolerancia, max_iter)
print(f"La raíz de la función {funcion} es: {raiz}")
