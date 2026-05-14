def calculadora_basica():
    number1=int(input("Ingrese primer numerito "))
    number2=int(input("Ingrese segundo numerito "))
    suma=number1+number2
    resta=number1-number2
    multiplicacion=number1*number2
    division=number1/number2
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicacion: {multiplicacion}")
    print(f"Division: {division}")
# calculadora_basica()

def Ficha_personal():
    nombre=str(input("Ingrese su nombre "))
    edad=int(input("Ingrese se edad "))
    altura=float(input("Ingrese se altura "))
    print("======Ficha Personal========")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Altura: {altura}")
    print("="*35)
Ficha_personal()
def error_str():
    numero=input("Ingrese un numero ")
    print(numero+"10") #Segun yo devolveria el numero ingresado en forma de texto mas el 10 ejem si ingresan 1 resultado 110
    print(numero*2) #Imprimira 2 veces el str(numero ingresado)
error_str()



