class Libro:
    def __init__(self,libro,autor,año):
        self.libro=libro
        self.autor=autor
        self.año=año


    @classmethod
    def to_dicc(cls,dato):
        return cls(dato["libro"],dato["autor"],dato["año"])
    
    @classmethod
    def desde_texto(cls,texto):
        partes=texto.split(",")
        libro=partes[0]
        autor=partes[1]
        año=int(partes[2])
        return cls(libro,autor,año)
    
    @classmethod
    def from_text(cls,date):
        parta=date.split(",")
        return cls(parta[0],parta[1],parta[2])
    

dato={"libro":"Principita","autor":"Jose","año":1954}
libro2=Libro.to_dicc(dato)
libro1=Libro.desde_texto("harrypoter,Isaac,2004")
libro3=Libro.from_text("Memoriasdelsubsuelo, Belfor,2001")
print(libro1.libro, libro1.año)
print(libro2.libro, libro2.año)
print(libro3.libro,libro3.autor, libro3.año)




        