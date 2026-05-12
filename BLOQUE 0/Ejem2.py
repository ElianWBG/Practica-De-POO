class Auto:
    def __init__(self,marca,color):
        self.marca=marca
        self.color=color
    
    def presetarse(self):
        return f"Nombre: {self.marca} | Color: {self.color}"
    
    def arrancar(self, estado):
        self.estado=estado
        return f"{self.marca} esta {self.estado} su motor "

a1=Auto(" Suzuki "," Negro ")
a2=Auto("Chevrolet","blanco")
a3=Auto("Hyundai", "Rojo")
print(a1.presetarse())
print(a2.presetarse())
print(a3.presetarse())
print(a1.arrancar("Encendido"))
print(a2.arrancar("Apagado"))
        