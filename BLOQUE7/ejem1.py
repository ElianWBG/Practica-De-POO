class ejem1:
    @staticmethod
    def sumar_varios(*numeros):   # *args convierte todo en una tupla
        return sum(numeros)

# print(sumar_varios(1, 2, 3))        # 6
# print(sumar_varios(1, 2, 3, 4, 5))  # 15
    @staticmethod
    def mostrar_datos(**datos):   # **kwargs convierte todo en un diccionario
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_datos(nombre="Ana", edad=25, ciudad="Guayaquil")
# nombre: Ana
# edad: 25
# ciudad: Guayaquil
def dividir(a, b):
    return a // b, a % b   # retorna dos valores

cociente, resto = dividir(10, 3)
print(cociente)  # 3
print(resto)     # 1
# función normal
def cuadrado(x):
    return x**2

# lambda — exactamente igual
cuadrado = lambda x: x**2
print(cuadrado(4))  # 16

# con dos parámetros
sumar = lambda a, b: a + b
print(sumar(3, 5))  # 8

