def solicitar_datos():
    nombre=str(input(" Ingrese su nombre "))
    edad=int(input(" Ingrese su edad "))
    return print(f"Nombre: {nombre} | Edad: {edad}")
# solicitar_datos()

def sumar_promedio():
    num1=int(input("ingrese un numero "))
    num2=int(input("ingrese un numero "))
    suma=num1+num2
    promedio=suma/2
    return print(f"{promedio}")
# sumar_promedio()

def sin_convertir():
    numero = input("Ingrese un número: ")  # ← sin int(), queda como str
    return print(numero + "5")                     # ← qué pasa aquí?
# sin_convertir()