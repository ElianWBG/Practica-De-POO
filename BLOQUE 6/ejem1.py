contador = 1
while contador <= 3:
    print(f"Contador: {contador}")
    contador += 1  # importante: si no incrementas, bucle infinito ♾️

# Contador: 1
# Contador: 2
# Contador: 3
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (paso de 2)
    print(i)

# lista
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)

# enumerate — índice y valor juntos
for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")

# diccionario
persona = {"nombre": "Juan", "edad": 25}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# break — termina el bucle completamente
for i in range(5):
    if i == 3: break
    print(i)        # imprime 0, 1, 2

# continue — salta la iteración actual
for i in range(5):
    if i == 2: continue
    print(i)        # imprime 0, 1, 3, 4

# forma normal
cuadrados = []
for x in range(5):
    cuadrados.append(x**2)

# list comprehension — exactamente igual pero en una línea
cuadrados = [x**2 for x in range(5)]
# [0, 1, 4, 9, 16]

# con condición
pares = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]