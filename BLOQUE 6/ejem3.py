class Ejercicio3:
    
    @staticmethod
    def tabla_multiplicar():
        print("\n=== TABLA DE MULTIPLICAR ===")
        num1 = int(input("Ingrese un número: "))
        contador = 1
        while contador <= 10:          
            print(f"{num1} x {contador} = {num1 * contador}")  
            contador += 1              
            
    @staticmethod
    def filtrar_nota():
        print("\n=== FILTRADO DE NOTAS ===")
        notas = [45, 78, 90, 55, 88, 32, 70, 65, 95, 40]
        notasA = [x for x in notas if x >= 70]
        notasR = [x for x in notas if x < 70]
        
        print("=== APROBADOS ===")
        for indice, nota in enumerate(notasA, 1):
            print(f"{indice}--{nota}")
            
        print("==== REPROBADOS ====")
       
        for indice, nota in enumerate(notasR, 1):
            print(f"{indice}--{nota}")
            
    @staticmethod
    def buscar_producto():
        print("\n=== BUSCADOR DE PRODUCTOS ===")
        prod = ["laptop", "mouse", "teclado", "monitor", "audifonos"]
        busq = input("Ingrese el nombre del producto: ").lower() 
        encontrado = False

        for indice, nombre in enumerate(prod):
            if nombre == busq:
                print(f"Encontrado en posición {indice}")
                encontrado = True
                break

        if not encontrado:
            print("Producto no encontrado")


Ejercicio3.tabla_multiplicar()
Ejercicio3.filtrar_nota()
Ejercicio3.buscar_producto()