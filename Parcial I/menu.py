import math
import matplotlib.pyplot as plt
import pandas as pd
from biseccion import biseccion
from newton import newton_raphson
from punto_fijo import punto_fijo
from regula_falsi import regula_falsi
from secante import secante

def graficar_errores():
    funcion = "x**2 - 7"
    derivada = "2*x"
    a, b = 2, 3  # Intervalo para métodos que lo requieren
    x0, x1 = 2.5, 2.7  # Valores iniciales para métodos iterativos
    tolerancia = 1e-6
    max_iter = 50
    
    metodos = {
        "Bisección": biseccion(funcion, a, b, tolerancia, max_iter),
        "Regula Falsi": regula_falsi(funcion, a, b, tolerancia, max_iter),
        "Newton-Raphson": newton_raphson(funcion, derivada, x0, max_iter),
        "Punto Fijo": punto_fijo(funcion, x0, max_iter),
        "Secante": secante(funcion, x0, x1, tolerancia, max_iter)
    }
    
    plt.figure(figsize=(10, 6))
    for nombre, (raiz, errores, iteraciones) in metodos.items():
        plt.plot(iteraciones, errores, label=nombre, marker='o')
    
    plt.yscale("log")  # Escala logarítmica para ver mejor la convergencia
    plt.xlabel("Iteraciones")
    plt.ylabel("Error absoluto")
    plt.title("Comparación de Convergencia de Métodos Numéricos")
    plt.legend()
    plt.grid()
    plt.show()
    
    # Crear una tabla comparativa de errores
    max_len = max(len(iteraciones) for _, (_, _, iteraciones) in metodos.items())
    tabla_errores = {"Iteración": list(range(1, max_len + 1))}
    
    for nombre, (_, errores, iteraciones) in metodos.items():
        errores_extendidos = errores + [None] * (max_len - len(errores))
        tabla_errores[nombre] = errores_extendidos
    
    df_errores = pd.DataFrame(tabla_errores)
    print("\nTabla comparativa de convergencia:")
    print(df_errores.to_string(index=False))
    
    # Crear una tabla comparativa de raíces
    tabla_raices = {"Método": list(metodos.keys()), "Raíz Aproximada": [f"{raiz:.20f}" for raiz, _, _ in metodos.values()]}
    df_raices = pd.DataFrame(tabla_raices)
    print("\nTabla comparativa de raíces aproximadas:")
    print(df_raices.to_string(index=False))

if __name__ == "__main__":
    graficar_errores()

