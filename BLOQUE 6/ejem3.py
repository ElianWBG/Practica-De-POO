def tabla_multiplicar():
    num1=int(input("Ingrese un numero "))

    contador = 1
    while contador <= 10:          
        print(f"{num1} x {contador} = {num1*contador}")  
        contador += 1              
        
tabla_multiplicar()

def filtrar_nota():
    notas=[45,78,90,55,88,32,70,65,95,40]
    notasA=[x for x in (notas)  if x>=70 ]
    notasR=[x for x in (notas)  if x<70 ]
    print("===APROBADOS===")
    for indice,nota in enumerate(notasA,1):
    
        print(f"{indice}--{nota}")
    print("====REPROBADOS====")
    for indice,nota in enumerate(notasR,):
        print(f"{indice}--{nota}")
    
   
filtrar_nota()

def buscar_producto():
    prod=["laptop","mouse","teclado","monitor","audifonos"]
    busq=input("Ingrese el nombre del producto ")
    encontrado = False

    for indice, nombre in enumerate(prod):
        if nombre == busq:
            print(f"Encontrado en posición {indice}")
            encontrado = True
            break          # ← sale del for

    # este if va FUERA del for
    if not encontrado:
        print("Producto no encontrado")

buscar_producto()



