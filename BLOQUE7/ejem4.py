class ejem4:
    @staticmethod
    def registrar_pedidos(*productos, **detalles):
        for clave,nombre in(detalles).items():
            print("==== nombre detalle====")
            print(f"Lugar{clave} Nombre:{nombre}")
           
        for indice,nombre in enumerate(productos ,1):
            print("=======Nombre Producto====")
            print( f"Lugar:{indice} Nombre:{nombre}")
         
    
    @staticmethod
    def landita2():
        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() aplica una función a cada elemento
        triples = list(map(lambda x: x*3, numeros))

# filter() filtra según condición
        mayores = list(filter(lambda x: x > 5, numeros))
        pares_cuadrados=list(map(lambda x:x**2,filter(lambda x:x%2==0,numeros)))
        print(triples)
        print(mayores)
        print(pares_cuadrados)
    @staticmethod
    def contar_regresiva(n):
        if n == 0:
            print(0)
            print("¡Despegue! 🚀")
            return          # ← solo para, no retorna valor
        print(n)            # imprime el número actual
        ejem4.contar_regresiva(n-1)
    
        




ejem4.registrar_pedidos("laptop", "mouse", "teclado",
                         cliente="Elian", ciudad="Guayaquil", urgente=True)

ejem4.contar_regresiva(5)
ejem4.landita2()