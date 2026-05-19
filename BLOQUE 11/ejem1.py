numeros = {1, 2, 2, 3, 3, 3}
print(numeros)  # {1, 2, 3} ← elimina duplicados automáticamente
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # {1,2,3,4,5,6} → unión — todos los elementos
print(A & B)  # {3,4}         → intersección — los comunes
print(A - B)  # {1,2}         → diferencia — los de A que no están en B
print(A ^ B)  # {1,2,5,6}     → diferencia simétrica — los que no comparten
s = {1, 2, 3}
s.add(4)        # agrega un elemento
s.remove(2)     # elimina — lanza KeyError si no existe
s.discard(99)   # elimina — sin error si no existe
s.pop()         # elimina y retorna uno aleatorio
lista = [1, 2, 2, 3, 3, 3, 4]
sin_duplicados = list(set(lista))
print(sin_duplicados)  # [1, 2, 3, 4]