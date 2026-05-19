persona = {
    "nombre": "Juan",
    "edad": 25,
    "hobbies": ["música", "deportes"]  # el valor puede ser cualquier tipo
}

# acceso
print(persona["nombre"])                    # Juan — lanza KeyError si no existe
print(persona.get("telefono", "No existe")) # acceso seguro con valor por defecto

# modificar
persona["edad"] = 26          # modifica valor existente

# agregar
persona["telefono"] = "099"   # agrega clave nueva

# eliminar
del persona["telefono"]       # elimina sin retornar
persona.pop("edad")           # elimina y retorna el valor
print(persona.keys())    # dict_keys(['nombre', 'edad', 'hobbies'])
print(persona.values())  # dict_values(['Juan', 25, [...]])
print(persona.items())   # dict_items([('nombre','Juan'), ...])

persona.update({"apellido": "Pérez"})  # agrega o actualiza varios a la vez
copia = persona.copy()                 # copia independiente
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

cuadrados = {x: x**2 for x in range(5)}
# {0:0, 1:1, 2:4, 3:9, 4:16}

universidad = {
    "estudiante": {"nombre": "María", "edad": 20},
    "profesor":   {"nombre": "Carlos", "materia": "POO"}
}

print(universidad["estudiante"]["nombre"])  # María
print(universidad["profesor"]["materia"])   # POO