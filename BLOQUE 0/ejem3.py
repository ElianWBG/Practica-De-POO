class Estudiantes:
    def __init__(self,nombre,precio,stock):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
    def vender(self,cantidad):
        self.stock-=cantidad
        if self.stock < cantidad:
            print("Stock insuficiente")
        else:
            print("Transaccion procesada")
    def reponer(self,cantidad):
        self.stock+=cantidad
        print("stock actualizado")

    def mostrar_info(self):
        valor_total=self.stock * self.precio
        return f" {self.nombre} | {valor_total} "

prod = Estudiantes("Laptop", 1000, 10)
prod.vender(3)    # Stock baja a 7
prod.reponer(5)   # Stock sube a 12
print(prod.mostrar_info())


    
    
    
        


    


        