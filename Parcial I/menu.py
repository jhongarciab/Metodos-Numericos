from biseccion import biseccion
from newton import newton_raphson
from punto_fijo import punto_fijo
from regula_falsi import regula_falsi
from secante import secante

while True:
    print("---- Seleccione un método ----")
    print("1. Bisección")
    print("2. Regula Falsi")
    print("3. Newton-Raphson")
    print("4. Iteración simple del punto fijo")
    print("5. Secante")
    print("6. Salir")

    seleccion = input("Seleccione una opción: ")

    if seleccion == "1":
        funcion = input("Ingrese la función en términos de x: ")
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        tolerancia = float(input("Ingrese la tolerancia: "))
        max_iter = int(input("Ingrese el número máximo de iteraciones: "))
        raiz = biseccion(funcion, a, b, tolerancia, max_iter)
        print(f"La raíz de la función {funcion} es: {raiz}")

    elif seleccion == "2":
        funcion = input("Ingrese la función en términos de x: ")
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        tolerancia = float(input("Ingrese la tolerancia: "))
        max_iter = int(input("Ingrese el número máximo de iteraciones: "))
        raiz = regula_falsi(funcion, a, b, tolerancia, max_iter)
        print(f"La raíz de la función {funcion} es: {raiz}")

    elif seleccion == "3":
        funcion = input("Ingrese la función en términos de x: ")
        fderivada = input("Ingrese la derivada de la función en términos de x: ")
        x_0 = float(input("Ingrese el valor de x_0: "))
        max_iter = int(input("Ingrese el número máximo de iteraciones: "))
        raiz = newton_raphson(funcion, fderivada, x_0, max_iter)
        print(f"La raíz de la función {funcion} es: {raiz}")

    elif seleccion == "4":
        funcion = input("Ingrese la función en términos de x: ")
        x_0 = float(input("Ingrese el valor de x_0: "))
        max_iter = int(input("Ingrese el número máximo de iteraciones: "))
        raiz = punto_fijo(funcion, x_0, max_iter)
        print(f"La raíz de la función {funcion} es: {raiz}")

    elif seleccion == "5":
        funcion = input("Ingrese la función en términos de x: ")
        x_0 = float(input("Ingrese el valor de X_1: "))
        x_1 = float(input("Ingrese el valor de X_2: "))
        tolerancia = float(input("Ingrese la tolerancia: "))
        max_iter = int(input("Ingrese el número máximo de iteraciones: "))
        raiz = secante(funcion, x_0, x_1, tolerancia, max_iter)
        print(f"La raíz de la función {funcion} es: {raiz}")
        
    elif seleccion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente de nuevo.")