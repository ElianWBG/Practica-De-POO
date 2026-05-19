
    
def Decorador(Funcion_B):
    def wrapper(*args,**kwargs):
        print("Iniciando...")
        resultado=Funcion_B(*args,**kwargs)
        print("Finalizando...")
        return resultado
    return wrapper
@Decorador
def saludar():
    print("Hola Mundo")


def decora(funcion_b):
    def wrapper(a,b):
        if b==0:
            print("Error:DIVISION Por 0")
            return None
        return funcion_b(a,b)
    return wrapper
@decora
def division(a,b):
    return a/b


def log(funcion_b):
    def wrapper(a,b):
        print(f"LLamado a la funcion sumar")
        resultado=funcion_b(a,b)
        return resultado
    return wrapper
@log
def sumar(a,b):
    return a+b

def validar_positivo(funcion_b):
    def wrapper(a):
        if a<0:
            print("Numero negativo")
            return None
        return funcion_b(a)
    return wrapper
@validar_positivo
def Cuadrado(a):
    return a**2

        

    







saludar()
print("="*40)
print(division(5,3))
division(5,0)
print("="*40)
print(sumar(30,45))
print("="*40)
print(Cuadrado(4))
Cuadrado(-30)

    
