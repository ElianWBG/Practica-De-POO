try:
    # código que puede fallar
except TipoError as e:
    # se ejecuta si hubo ese error
else:
    # se ejecuta si NO hubo error
finally:
    # se ejecuta SIEMPRE — con o sin error

int("abc")          # ValueError   → valor inválido
"hola" + 5          # TypeError    → tipos incompatibles
lista[99]           # IndexError   → índice fuera de rango
dic["noexiste"]     # KeyError     → clave no existe
10 / 0              # ZeroDivisionError → división por cero
open("noexiste.txt")# FileNotFoundError → archivo no encontrado

# capturar un error específico
try:
    n = int("abc")
except ValueError as e:
    print(f"Error: {e}")

# múltiples errores
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
except TypeError:
    print("Tipo de dato incorrecto")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Esto siempre se ejecuta")

# raise — lanzar error manualmente
def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    return edad

# excepción personalizada
class MiError(Exception):
    pass

raise MiError("Error personalizado")

# assert — verificar condición
assert x > 0, "Debe ser positivo"