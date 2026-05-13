palabra_uno:str="Mi Nombre"
num_entero:int=50
num_decimal:float=3.1415
num_Booleano:bool=False
Valor_vacio=None

tupla:tuple=("Elian",22,"Duran")
Conjunto:set={1,3,4}


class Inventario:
    def mostrar_info(self):
        producto = "Laptop Gaming"
        precios  = [450.99, 899.50, 1200.00, 75.25, 320.00]
        stock    = {"laptops": 15, "mouses": 42, "teclados": 8}
        print(producto[0:6])
        print(precios[0])
        print(precios[-1])
        print(precios[1:3])
        print(stock["mouses"])

asd=Inventario()
asd.mostrar_info()


