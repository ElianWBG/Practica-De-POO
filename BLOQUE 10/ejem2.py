class ejem2:
    @staticmethod
    def presentar():
        diccio={"nombre":"elian","edad":22,"ciudad":"Duran"}
        print(f"{diccio['nombre']}")
        print(f"{diccio.get("edad","no existe")}")
        print(diccio.get("ciudad"))
    
    @staticmethod
    def presentacion():
        print(f"==== PRESENTACION====")
        diccio={"nombre":"elian","edad":22,"ciudad":"Duran"}

        for indice,conte in(diccio).items():
            print(indice,conte)
    
    @staticmethod
    def demostracion():
        datos = {"nombre": "Juan"}
        copia = datos   #Asignando misma posicion en memoria           
        copia["nuevo"] = 2
        print("=====DEMOSTRACION====")
        print(datos) #Imprime datos con el nuevo dato agregado que es 2 ya que al agregar en copia se agrega en datos              
        print(datos is copia)  #Da true porq aputan hacia la misma posicion en memoria    
            
   


ejem2.presentacion()
print("="*30)
ejem2.presentar()
print("="*30)
ejem2.demostracion()
print("="*30)
cuadrado={x:x**2 for x in range(11)}
print(cuadrado)
