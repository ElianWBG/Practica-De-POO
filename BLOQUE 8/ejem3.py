class ejem3():
    @staticmethod
    def agregar_productos():
            asd=[]
            asd.append("laptop")
            asd.append("mouse")
            asd.append("teclado")
            asd.append("monitor")
            asd.append("audifonos")
            print(asd)
            asd.sort()
            print(asd)
            asd.reverse()
            print(asd)
            
            
    @staticmethod
    def estadistica():
        precios = [299.99, 15.50, 89.99, 450.00, 35.75, 120.00]
        print(f"Total de precios: {len(precios)}")
        print(f"suma:{sum(precios)}")
        print(f"max:{max(precios)}")
        print(f"minimo:{min(precios) } ")
        print(f"Promedio:{sum(precios)/len(precios)}")

    @staticmethod
    def demostrar():
        inventario = ["laptop", "mouse", "teclado"]
        copia_ref=inventario
        copia_real=inventario.copy()
        copia_ref.append("monitor")



        print(copia_ref)
        print(inventario)
        print(copia_real)
        print(inventario is copia_ref) #apuntan al mismo espacio en memoria en otras palabras esta conectado al inventario
        print(inventario is copia_real)#aputan a otro espacio en memoria 

    
print("="*40)
ejem3.agregar_productos()
print("="*40)
ejem3.estadistica()
print("="*40)
ejem3.demostrar()






            