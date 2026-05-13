class Estudiante:
    def __init__(self, nombre, notas=None):
        self.nombre = nombre
        self.notas = notas if notas is not None else []

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["nombre"], datos["notas"])

    @classmethod
    def desde_texto(cls, texto):              # recibe "Carlos,7,8,9"
        partes = texto.split(",")             # ["Carlos","7","8","9"]
        nombre = partes[0]                    # "Carlos"
        notas = [int(n) for n in partes[1:]] # [7, 8, 9]
        return cls(nombre, notas)

# forma directa
estu1 = Estudiante("Elian", [8, 9, 10])

# desde diccionario
datos = {"nombre": "Luis", "notas": [8, 9, 7]}
estu2 = Estudiante.desde_diccionario(datos)

# desde texto
estu3 = Estudiante.desde_texto("Carlos,7,8,9")

# sin notas
estu4 = Estudiante("Ana")

print(estu1.nombre, estu1.notas)  # Elian [8, 9, 10]
print(estu2.nombre, estu2.notas)  # Luis [8, 9, 7]
print(estu3.nombre, estu3.notas)  # Carlos [7, 8, 9]
print(estu4.nombre, estu4.notas)  # Ana []