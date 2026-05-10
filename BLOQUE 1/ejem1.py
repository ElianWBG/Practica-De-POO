class Persona:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad=edad
    
    def presentar(self):
        print(f"{self.nombre} y tengo {self.edad} años")


elian=Persona("Elian",22)
jose=Persona("Jose",20)
jonathan=Persona("Jonathan",21)
elian.presentar()
jonathan.presentar()
jose.presentar()
print(elian.nombre)
print(jose.nombre)
