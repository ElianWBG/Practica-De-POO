def mi_decorador(funcion_original):
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar")           # ← se ejecuta primero
        resultado = funcion_original(*args, **kwargs)  # ← ejecuta la función original
        print("Después de ejecutar")         # ← se ejecuta al final
        return resultado
    return wrapper

@mi_decorador
def saludar():
    print("Hola mundo")

saludar()
# Antes de ejecutar
# Hola mundo
# Después de ejecutar
def mi_decorador(funcion_original):
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar")           # ← se ejecuta primero
        resultado = funcion_original(*args, **kwargs)  # ← ejecuta la función original
        print("Después de ejecutar")         # ← se ejecuta al final
        return resultado
    return wrapper

@mi_decorador
def saludar():
    print("Hola mundo")

saludar()
# Antes de ejecutar
# Hola mundo
# Después de ejecutar