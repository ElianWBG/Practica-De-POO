lista = [3, 1, 4, 1, 5]

lista.append(9)        # agrega al final → [3,1,4,1,5,9]
lista.extend([7, 8])   # agrega varios   → [3,1,4,1,5,9,7,8]
lista.insert(0, 99)    # inserta en pos 0 → [99,3,1,4,1,5,9,7,8]
lista.pop()            # elimina y retorna el último → 8
lista.pop(0)           # elimina y retorna el de pos 0 → 99
lista.remove(1)        # elimina la PRIMERA ocurrencia de 1
lista.sort()           # ordena de menor a mayor (modifica original)
lista.reverse()        # invierte (modifica original)
lista.clear()          # vacía la lista → []
lista.count(1)         # cuenta cuántas veces aparece 1
lista.index(4)         # posición de la primera ocurrencia de 4
lista.copy()           # copia superficial

nums = [10, 5, 8, 1, 9]

len(nums)      # 5     → cantidad de elementos
sum(nums)      # 33    → suma total
max(nums)      # 10    → mayor valor
min(nums)      # 1     → menor valor
sorted(nums)   # [1,5,8,9,10] → NO modifica original, retorna nueva lista
nums.sort()    # [1,5,8,9,10] → SÍ modifica original