import math
import matplotlib.pyplot as plt
import pandas as pd
from biseccion import biseccion
from newton import newton_raphson
from punto_fijo import punto_fijo
from regula_falsi import regula_falsi
from secante import secante

def graficar_errores():
    """
    Función que ejecuta distintos métodos numéricos para encontrar la raíz de la ecuación x^2 - 7 = 0,
    compara sus errores absolutos y genera visualizaciones para analizar su convergencia.
    
    Se generan:
    1. Una gráfica de error absoluto vs iteraciones en escala logarítmica.
    2. Una tabla comparativa de convergencia mostrando los errores en las primeras 10 iteraciones.
    3. Una tabla con las raíces aproximadas encontradas por cada método.
    """
    
    # Definición de la función y su derivada (para métodos que la requieren)
    funcion = "x**2 - 7"
    derivada = "2*x"
    
    # Parámetros iniciales para los métodos
    a, b = 2, 3  
    x0, x1 = 2.5, 2.7 
    tolerancia = 1e-6 
    max_iter = 50 
    
    # Diccionario con los métodos y sus resultados
    metodos = {
        "Bisección": biseccion(funcion, a, b, tolerancia, max_iter),
        "Regula Falsi": regula_falsi(funcion, a, b, tolerancia, max_iter),
        "Newton-Raphson": newton_raphson(funcion, derivada, x0, max_iter),
        "Punto Fijo": punto_fijo(funcion, x0, max_iter),
        "Secante": secante(funcion, x0, x1, tolerancia, max_iter)
    }
    
    # Gráfica de convergencia (Error vs Iteraciones)
    plt.figure(figsize=(10, 6))
    for nombre, (raiz, errores, iteraciones) in metodos.items():
        plt.plot(iteraciones, errores, label=nombre, marker='o')
    
    plt.yscale("log") 
    plt.xlabel("Iteraciones")
    plt.ylabel("Error absoluto")
    plt.title("Comparación de Convergencia de Métodos Numéricos")
    plt.legend()
    plt.grid()
    plt.show()
    
    # Tabla comparativa de errores (Primeras 10 iteraciones)
    max_len = 12
    tabla_errores = {"Iteración": list(range(1, max_len + 1))}
    
    for nombre, (_, errores, iteraciones) in metodos.items():
        errores_truncados = errores[:max_len] + [None] * (max_len - len(errores))
        tabla_errores[nombre] = errores_truncados
    
    df_errores = pd.DataFrame(tabla_errores)
    print("\nTabla comparativa de convergencia:")
    print(df_errores.to_string(index=False))
    
    # Tabla comparativa de raíces aproximadas
    tabla_raices = {
        "Método": list(metodos.keys()),
        "Raíz Aproximada": [f"{raiz:.20f}" for raiz, _, _ in metodos.values()]
    }
    df_raices = pd.DataFrame(tabla_raices)
    print("\nTabla comparativa de raíces aproximadas:")
    print(df_raices.to_string(index=False))

if __name__ == "__main__":
    graficar_errores()

