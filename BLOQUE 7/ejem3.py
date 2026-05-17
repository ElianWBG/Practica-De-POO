class ejem3:
    @staticmethod
    def crear_perfil(**kwarg):
        for indice, nombre in (kwarg).items():
            print(f" {indice} : {nombre}")

    

    @staticmethod
    def landitas():
        

        cuadrado=lambda x:x**2
        es_par=lambda x:x%2==0
        saludar=lambda x:f"hola,{x}"
        print(cuadrado(5))
        print(es_par(40))
        print(saludar("elian"))
    @staticmethod
    def sumar_hasta(n):
        if n==0:return 0
        return n+ejem3.sumar_hasta(n-1)
    

# nombre: Elian
# edad: 22
# ciudad: Guayaquil
# carrera: Sistemas
ejem3.crear_perfil(nombre="Elian", edad=22, ciudad="Guayaquil", carrera="Sistemas")
print("="*40)
# ejem3.landitas()
print(ejem3.sumar_hasta(20))
print("="*40)
ejem3.landitas()

