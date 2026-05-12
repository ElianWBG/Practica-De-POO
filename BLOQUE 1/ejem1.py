# class Persona:
#     def __init__(self, nombre,edad):
#         self.nombre = nombre
#         self.edad=edad
    
#     def presentar(self):
#         print(f"{self.nombre} y tengo {self.edad} años")


# elian=Persona("Elian",22)
# jose=Persona("Jose",20)
# jonathan=Persona("Jonathan",21)
# elian.presentar()
# jonathan.presentar()
# jose.presentar()
# print(elian.nombre)
# print(jose.nombre)


print("="*40)
class Producto:
    def __init__(self, codigo, nombre, precio):
        if precio < 0:
            # Si quieres que el programa siga, podrías imprimir un error en lugar de usar raise
            # Pero para aprender, lo dejaremos positivo para que no se detenga
            raise ValueError("El precio no puede ser negativo")
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

# Cambiamos -10 por 10 para que el código no se detenga aquí
p = Producto(1, "Leche", 10) 
pe = Producto(0, "Cola", 10)
print(f"Producto: {p.nombre}, Precio: {p.precio}")
print("="*40)
class Item:
    def __init__(self, Nombre, Estado="Disponible"):
        self.Nombre = Nombre
        self.Estado = Estado

cli = Item("Mouse")
cli2 = Item("Teclado", "Agotado")
print(f"Item: {cli.Nombre}, Estado: {cli.Estado}")
print(f"Item: {cli2.Nombre}, Estado: {cli2.Estado}")
print("="*40)
class Cliente:
    def __init__(self, id_cliente, nombre):
        self.id_cliente = id_cliente
        self.nombre = nombre
    
    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["id_cliente"], datos["nombre"])

datos = {"id_cliente": 1, "nombre": "Daniel"}
cli_final = Cliente.desde_diccionario(datos)
print(f"Cliente: {cli_final.nombre}, ID: {cli_final.id_cliente}")
        
