a = 20
b = 4

print(a + b)   # 24  → suma
print(a - b)   # 16  → resta
print(a * b)   # 80  → multiplicación
print(a / b)   # 5.0 → división decimal (siempre retorna float)
print(a // b)  # 5   → división entera (sin decimales)
print(a % b)   # 0   → módulo (residuo de la división)
print(a ** b)  # 160000 → potencia (20 elevado a 4)
print("="*60)
print(10 == 10)  # True  → igual
print(10 != 5)   # True  → diferente
print(10 > 5)    # True  → mayor
print(10 < 5)    # False → menor
print(10 >= 10)  # True  → mayor o igual
print(10 <= 9)   # False → menor o igual
print("="*60)
edad = 20
tiene_licencia = True

print(edad >= 18 and tiene_licencia)  # True  → ambas verdaderas
print(edad >= 18 or tiene_licencia)   # True  → al menos una verdadera
print(not tiene_licencia)             # False → invierte el resultado

a = [1, 2]
b = [1, 2]
c = a
print("="*60)
print(a == b)  # True  → mismo contenido
print(a is b)  # False → objetos distintos en memoria
print(a is c)  # True  → misma referencia en memoria