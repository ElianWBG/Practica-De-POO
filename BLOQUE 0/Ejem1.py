class Persona:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad=edad

def biblioteca():
    return f"Posible clases: Usuario | Libro | Autor | Categoria | Bibliotecario "
def Explicacion():
    return f"Clase: Es un Molde o Plano de un objeto | Objeto: Es la creacion real apartir del molde"
    

elian=Persona("Elian",22)
jose=Persona("Jose",20)
jonathan=Persona("Jonathan",21)

print("="*30)
print(elian.nombre)
print(jose.nombre)
print(jonathan.nombre)
print("="*30)
print(biblioteca())
print("="*30)
print(Explicacion())













