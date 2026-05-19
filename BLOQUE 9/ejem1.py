lista = [1, 2, 3]
lista[0] = 10      # ✅ permitido

tupla = (1, 2, 3)
tupla[0] = 10      # ❌ TypeError: 'tuple' object does not support item assignment
tupla = (1, 2, 3, 2, 4, 2)
print(tupla.count(2))   # 3 → cuántas veces aparece 2
print(tupla.index(3))   # 2 → posición de la primera ocurrencia de 3
# básico
a, b, c = (1, 2, 3)
print(a)  # 1
print(b)  # 2

# con operador * — captura el resto
primero, *medio, ultimo = (1, 2, 3, 4, 5)
print(primero)  # 1
print(medio)    # [2, 3, 4]
print(ultimo)   # 5

# en bucles
coordenadas = [(1, 2), (3, 4), (5, 6)]
for x, y in coordenadas:
    print(f"x={x}, y={y}")

tupla = (1, 2, 3)

# convertir a lista para modificar
lista_temp = list(tupla)
lista_temp.append(4)

# volver a tupla
nueva_tupla = tuple(lista_temp)
print(nueva_tupla)  # (1, 2, 3, 4)