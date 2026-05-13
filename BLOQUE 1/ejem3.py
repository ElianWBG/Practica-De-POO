class Libro:
    def __init__(self,titulo,autor,paginas,generos=None):
        if paginas < 0: raise ValueError("No puede ser negativa")
        self.titulo=titulo
        self.autor=autor
        self.paginas=paginas
        self.generos=generos if generos is not None else []

    @classmethod
    def desde_diccionario(cls,datos):
        return cls(datos["titulo"],datos["autor"],datos["paginas"],datos["generos"])
    @classmethod
    def desde_texto(cls,texto):
        partes=texto.split(",")
        nombre=partes[0]
        autor=partes[1]
        paginas=int(partes[2])
        generos=partes[3:]
        return cls(nombre,autor,paginas,generos)
    


    @classmethod
    def desde_texto2(cls,texto):
        partes=texto.split(",")
        nombre=partes[0]
        autor=partes[1]
        paginas=int(partes[2])
        generos=partes[3:]
        return cls(nombre,autor,paginas,generos)


    


# forma directa
libro1 = Libro("El Principito", "Saint-Exupéry", 96, ["infantil", "filosofía"])

# desde diccionario
datos = {"titulo": "Dune", "autor": "Herbert", "paginas": 412, "generos": ["ciencia ficción"]}
libro2 = Libro.desde_diccionario(datos)

# desde texto
libro3 = Libro.desde_texto("Python 101,Smith,250,tecnología,programación")
libro4 = Libro.desde_texto2("Python 101,Smith,250,tecnología,programación")

print(libro1.titulo, libro1.generos)
print(libro2.titulo, libro2.generos)
print(libro3.titulo, libro3.generos)
print(libro4.titulo, libro4.generos)
